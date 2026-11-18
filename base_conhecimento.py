import json
from orientacao import Orientacao

ACENTOS = {"á": "a", "à": "a", "ã": "a", "â": "a", "é": "e", "ê": "e",
           "í": "i", "ó": "o", "õ": "o", "ô": "o", "ú": "u", "ç": "c"}

def normalizar(texto):
    texto = texto.lower().strip()
    for letra, troca in ACENTOS.items():
        texto = texto.replace(letra, troca)
    for sinal in "?!.,;:()":
        texto = texto.replace(sinal, " ")
    return " " + " ".join(texto.split()) + " "

class BaseConhecimento:
    """Conjunto de orientações: lê o JSON, lista categorias e busca por pontuação."""
    def __init__(self, caminho):
        self.caminho = caminho
        self.orientacoes = []

    def carregar(self):
        try:
            with open(self.caminho, encoding="utf-8") as f:
                self.orientacoes = [Orientacao(d) for d in json.load(f)]
            return True
        except (FileNotFoundError, json.JSONDecodeError, KeyError, TypeError) as erro:
            print(f"Não foi possível carregar a base ({erro.__class__.__name__}). Verifique {self.caminho}.")
            self.orientacoes = []
            return False

    def categorias(self):
        return sorted({o.categoria for o in self.orientacoes})

    def por_categoria(self, categoria):
        return [o for o in self.orientacoes if o.categoria == categoria]

    def pontuar(self, orientacao, pergunta):
        """+3 por palavra-chave na pergunta; +1 por palavra (4+ letras) da pergunta no título."""
        p = normalizar(pergunta)
        pontos = 0
        for kw in orientacao.palavras_chave:
            if normalizar(kw) in p:
                pontos += 3
        titulo = normalizar(orientacao.titulo)
        for palavra in set(p.split()):
            if len(palavra) >= 4 and " " + palavra + " " in titulo:
                pontos += 1
        return pontos

    def buscar(self, pergunta):
        """Devolve lista de tuplas (pontos, orientacao), da maior para a menor."""
        res = [(self.pontuar(o, pergunta), o) for o in self.orientacoes]
        res = [t for t in res if t[0] > 0]
        res.sort(key=lambda t: t[0], reverse=True)
        return res
