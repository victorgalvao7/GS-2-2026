import os
from base_conhecimento import BaseConhecimento
from assistente import Assistente

AQUI = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(AQUI, "data"), exist_ok=True)

base = BaseConhecimento(os.path.join(AQUI, "data", "base_conhecimento.json"))
base.carregar()  # lê o JSON e cria os objetos Orientacao
assistente = Assistente("Citizen Assist AI", base,
                        os.path.join(AQUI, "data", "historico.json"),
                        os.path.join(AQUI, "data", "atendimentos.csv"))
if base.orientacoes:
    try:
        assistente.menu()
    except (KeyboardInterrupt, EOFError):
        print("\nEncerrado.")
