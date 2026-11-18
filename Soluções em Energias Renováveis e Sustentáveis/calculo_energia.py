"""Análise energética: banho (chuveiro elétrico) em uma casa. Compara cenários
para a MESMA necessidade (água quente) e MESMO período (1 mês, 30 dias).
Uso: python calculo_energia.py"""
import json, os
AQUI = os.path.dirname(os.path.abspath(__file__))

def calcular(p):
    kwh = lambda minutos: p["pessoas"] * minutos / 60 * p["potencia_chuveiro_w"] / 1000 * p["dias_mes"]
    atual = kwh(p["minutos_banho_atual"])
    reduzido = kwh(p["minutos_banho_reduzido"])
    fs = p["fracao_solar"]
    invest = p["custo_aquecedor_solar_rs"]
    brutos = {
        "Atual (banho de %d min)" % p["minutos_banho_atual"]: (atual, 0),
        "A) Banho de %d min (sem custo)" % p["minutos_banho_reduzido"]: (reduzido, 0),
        "B) Aquecedor solar (renovável)": (atual * (1 - fs), invest),
        "A+B) Banho curto + solar": (reduzido * (1 - fs), invest),
    }
    res = {}
    for nome, (k, inv) in brutos.items():
        eco_kwh = atual - k
        eco_rs = eco_kwh * p["tarifa_rs_kwh"]
        res[nome] = {
            "kwh_mes": round(k, 1), "custo_mes_rs": round(k * p["tarifa_rs_kwh"], 2),
            "economia_kwh_mes": round(eco_kwh, 1), "economia_rs_mes": round(eco_rs, 2),
            "co2_evitado_kg_ano": round(eco_kwh * 12 * p["fator_emissao_kgco2_kwh"], 1),
            "investimento_rs": inv,
            "retorno_meses": round(inv / eco_rs, 1) if inv and eco_rs > 0 else None,
            "economia_liquida_vida_util_rs": round(eco_rs * 12 * p["vida_util_anos"] - inv, 2) if inv else None,
        }
    return res

if __name__ == "__main__":
    with open(os.path.join(AQUI, "dados_energia.json"), encoding="utf-8") as f:
        p = json.load(f)["premissas"]
    r = calcular(p)
    print("E (kWh) = P (kW) x t (h). Premissas:", p, "\n")
    for nome, d in r.items():
        print(nome)
        for k, v in d.items():
            print("   ", k, "=", v)
    with open(os.path.join(AQUI, "resultados_energia.json"), "w", encoding="utf-8") as f:
        json.dump(r, f, ensure_ascii=False, indent=1)
