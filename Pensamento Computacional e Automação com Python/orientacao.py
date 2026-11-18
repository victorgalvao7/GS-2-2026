class Orientacao:
    """Uma orientação da base (um registro do JSON)."""
    def __init__(self, d):
        self.id = d["id"]; self.categoria = d["categoria"]; self.titulo = d["titulo"]
        self.palavras_chave = d["palavras_chave"]; self.resposta = d["resposta"]
        self.documentos = d["documentos"]; self.onde = d["onde"]
        self.fonte = d["fonte"]; self.verificado_em = d["verificado_em"]

    def exibir(self):
        print(f"\n>> {self.titulo}  [{self.categoria}]")
        print(self.resposta)
        print("Documentos necessários:")
        for doc in self.documentos:
            print(f"  - {doc}")
        print(f"Onde: {self.onde}")
        print(f"Fonte: {self.fonte} (verificado em {self.verificado_em})")
        print("Aviso: este assistente NÃO é um canal oficial.")
