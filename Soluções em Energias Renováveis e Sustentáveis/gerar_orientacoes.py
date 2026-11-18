"""Gera as orientações de ENERGIA a partir da análise (integração com o Citizen Assist AI)."""
import json, os
from calculo_energia import calcular, AQUI
HOJE = "2026-11-18"
AVISO = " Valores são ESTIMATIVAS (família de 4 pessoas, tarifa e custos de exemplo); não são garantia de economia."

def gerar():
    p = json.load(open(os.path.join(AQUI, "dados_energia.json"), encoding="utf-8"))["premissas"]
    r = list(calcular(p).values()); a, b, ab = r[1], r[2], r[3]
    return [
     {"categoria": "Energia", "titulo": "Economizar energia no chuveiro elétrico",
      "palavras_chave": ["chuveiro", "banho", "conta de luz alta", "economizar energia"],
      "resposta": f"O chuveiro é um dos maiores gastos de luz da casa. Reduzir o banho de {p['minutos_banho_atual']} para {p['minutos_banho_reduzido']} minutos pode economizar cerca de {a['economia_kwh_mes']} kWh (R$ {a['economia_rs_mes']:.2f}) por mês, sem custo.{AVISO}",
      "documentos": ["Sua conta de luz (para ver a tarifa e o consumo)"],
      "onde": "Em casa; consumo e tarifa na conta da sua distribuidora",
      "fonte": "https://www.gov.br/aneel", "verificado_em": HOJE},
     {"categoria": "Energia", "titulo": "Aquecedor solar de água: vale a pena?",
      "palavras_chave": ["energia solar", "aquecedor solar", "placa solar", "fonte renovavel"],
      "resposta": f"O aquecedor solar usa o sol para esquentar a água. Estimativa: cobre cerca de {int(p['fracao_solar']*100)}% do banho, economiza {b['economia_kwh_mes']} kWh (R$ {b['economia_rs_mes']:.2f}) por mês e se paga em cerca de {b['retorno_meses']} meses (investimento de exemplo R$ {p['custo_aquecedor_solar_rs']}). Banho curto + solar chega a R$ {ab['economia_rs_mes']:.2f} por mês. Evita CO2, mas a rede elétrica do Brasil já é bastante limpa, então o ganho principal é financeiro. Peça orçamentos e veja se há espaço e sol no telhado.{AVISO}",
      "documentos": ["Orçamentos de empresas", "Comprovante de propriedade ou autorização do imóvel"],
      "onde": "Empresas instaladoras (procure selo PROCEL/Inmetro)",
      "fonte": "https://www.gov.br/mme", "verificado_em": HOJE},
    ]

if __name__ == "__main__":
    json.dump(gerar(), open(os.path.join(AQUI, "orientacoes_energia.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("orientacoes_energia.json gerado")
