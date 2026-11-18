import csv, json, os, time
from datetime import datetime
from statistics import mean

CAMPOS = ["data", "origem", "pergunta", "id_orientacao", "encontrou", "ajudou",
          "tentativas", "tempo_segundos", "sessao", "nota_facilidade"]

class Assistente:
    """Conversa com o cidadão, guarda o histórico e calcula indicadores."""
    def __init__(self, nome, base, arq_historico="data/historico.json", arq_csv="data/atendimentos.csv"):
        self.nome = nome
        self.base = base
        self.arq_historico = arq_historico
        self.arq_csv = arq_csv
        self.sessao = datetime.now().strftime("%Y%m%d%H%M%S")
        self.nova = []
        self.historico = self._ler_historico()

    # ---------- entrada segura ----------
    def _ler_historico(self):
        try:
            with open(self.arq_historico, encoding="utf-8") as f:
                dados = json.load(f)
            return dados if isinstance(dados, list) else []
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _salvar_historico(self):
        with open(self.arq_historico, "w", encoding="utf-8") as f:
            json.dump(self.historico, f, ensure_ascii=False, indent=1)

    def ler_opcao(self, prompt, minimo, maximo):
        while True:
            txt = input(prompt).strip()
            if txt.isdigit() and minimo <= int(txt) <= maximo:
                return int(txt)
            print(f"Opção inválida. Digite um número de {minimo} a {maximo}.")

    def ler_sn(self, prompt):
        while True:
            r = input(prompt).strip().lower()
            if r in ("s", "n"):
                return r == "s"
            print("Responda apenas com s ou n.")

    @staticmethod
    def tem_dado_pessoal(texto):
        return sum(c.isdigit() for c in texto) >= 8 or "@" in texto

    @staticmethod
    def confianca(pontos):
        return "ALTA" if pontos >= 6 else "MÉDIA" if pontos >= 3 else None

    # ---------- atendimento ----------
    def perguntar(self):
        inicio = time.time(); tentativas = 0; ultima = ""
        while True:
            texto = input("\nDigite sua dúvida (0 para voltar): ").strip()
            if texto == "0":
                if tentativas > 0:
                    self.registrar("pergunta", ultima, None, False, False, tentativas, round(time.time() - inicio, 1))
                return
            if not texto:
                print("Você não digitou nada. Escreva sua dúvida."); continue
            if self.tem_dado_pessoal(texto):
                print("Atenção: não digite CPF, telefone ou e-mail. Reescreva."); continue
            tentativas += 1; ultima = texto
            res = self.base.buscar(texto)
            if not res or self.confianca(res[0][0]) is None:
                print("Não encontrei uma orientação para isso. Tente outras palavras (ex.: 'cartão SUS', 'conta de luz')")
                print("ou volte (0) e use a navegação por categorias: " + ", ".join(self.base.categorias()))
                continue
            pontos, o = res[0]
            print(f"\nConfiança da resposta: {self.confianca(pontos)} ({pontos} pontos)")
            o.exibir()
            alternativas = res[1:3]
            if alternativas:
                print("\nOutras orientações parecidas: " + "; ".join(a.titulo for _, a in alternativas))
            ajudou = self.ler_sn("\nEssa orientação respondeu sua dúvida? (s/n): ")
            self.registrar("pergunta", texto, o.id, True, ajudou, tentativas, round(time.time() - inicio, 1))
            return

    def navegar(self):
        cats = self.base.categorias()
        while True:
            print("\nCategorias:")
            for i, c in enumerate(cats, 1):
                print(f"  {i}. {c}")
            print("  0. Voltar")
            op = self.ler_opcao("Escolha: ", 0, len(cats))
            if op == 0:
                return
            cat = cats[op - 1]
            lista = self.base.por_categoria(cat)
            while True:
                print(f"\n[{cat}]")
                for i, o in enumerate(lista, 1):
                    print(f"  {i}. {o.titulo}")
                print("  0. Voltar")
                n = self.ler_opcao("Escolha: ", 0, len(lista))
                if n == 0:
                    break
                inicio = time.time()
                o = lista[n - 1]
                o.exibir()
                ajudou = self.ler_sn("\nEssa orientação respondeu sua dúvida? (s/n): ")
                self.registrar("categoria", f"({cat}) {o.titulo}", o.id, True, ajudou, 1, round(time.time() - inicio, 1))

    # ---------- histórico e indicadores ----------
    def registrar(self, origem, pergunta, id_o, encontrou, ajudou, tentativas, tempo):
        reg = {"data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "origem": origem, "pergunta": pergunta,
               "id_orientacao": id_o, "encontrou": encontrou, "ajudou": ajudou,
               "tentativas": tentativas, "tempo_segundos": tempo, "sessao": self.sessao, "nota_facilidade": None}
        self.historico.append(reg); self.nova.append(reg)
        self._salvar_historico()

    def indicadores(self):
        h = self.historico
        if not h:
            print("\nAinda não há atendimentos registrados."); return
        enc = [r for r in h if r["encontrou"]]
        notas = {r["sessao"]: r["nota_facilidade"] for r in h if r.get("nota_facilidade")}
        print("\n===== INDICADORES =====")
        print(f"Atendimentos: {len(h)}")
        print(f"Resposta encontrada (%): {100 * len(enc) / len(h):.1f}")
        print(f"Taxa de acerto: ajudou (%): {100 * sum(r['ajudou'] for r in enc) / len(enc):.1f}" if enc else "Taxa de acerto: ajudou (%): 0.0")
        print(f"Tempo médio para encontrar (s): {mean(r['tempo_segundos'] for r in enc):.1f}" if enc else "Tempo médio: -")
        print(f"Tentativas por atendimento: {mean(r['tentativas'] for r in h):.2f}")
        print(f"Facilidade de uso (1 a 5): {mean(notas.values()):.1f}" if notas else "Facilidade de uso (1 a 5): sem notas")
        sem = [r["pergunta"] for r in h if not r["encontrou"]]
        print("Dúvidas sem solução: " + ("; ".join(sem) if sem else "nenhuma"))

    def exportar_csv(self):
        os.makedirs(os.path.dirname(self.arq_csv) or ".", exist_ok=True)
        with open(self.arq_csv, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CAMPOS)
            w.writeheader()
            w.writerows(self.historico)
        print(f"CSV exportado: {self.arq_csv} ({len(self.historico)} atendimentos)")

    def menu(self):
        print(f"\n=== {self.nome} ===\nEu oriento sobre transporte, saúde, documentos, consumo e energia.")
        print("Não peço nem guardo dados pessoais. Este assistente NÃO é um canal oficial.")
        while True:
            print("\n1. Perguntar em texto livre\n2. Navegar por categorias\n3. Ver indicadores\n4. Exportar CSV\n0. Sair")
            op = self.ler_opcao("Escolha: ", 0, 4)
            if op == 1: self.perguntar()
            elif op == 2: self.navegar()
            elif op == 3: self.indicadores()
            elif op == 4: self.exportar_csv()
            else: break
        if self.nova:
            nota = self.ler_opcao("Dê uma nota de facilidade de uso (1 a 5): ", 1, 5)
            for r in self.nova:
                r["nota_facilidade"] = nota
            self._salvar_historico()
        self.indicadores(); self.exportar_csv()
        print("Obrigado! Até logo.")
