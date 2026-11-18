# Energias Renováveis e Sustentáveis — contribuição ao Citizen Assist AI
Integrantes: **[Victor Vieira Galvão - 571483]**, **[Miguel Silverio de Avila - 568873]**, **[Artur Souza Pereira - 570880]** | Vídeo (máx. 3 min): **[LINK]**
Repositório do assistente completo: **[https://github.com/victorgalvao7/GS-2-2026/tree/main/Pensamento%20Computacional%20e%20Automa%C3%A7%C3%A3o%20com%20Python]** (as orientações de energia estão na categoria "Energia", ids 11 e 12).

## Público e necessidade
Moradores de casas com chuveiro elétrico que querem reduzir a conta de luz. O banho é um dos maiores consumos residenciais.

## Como executar
`python calculo_energia.py` (mostra cálculos e gera `resultados_energia.json`) e `python gerar_orientacoes.py` (gera `orientacoes_energia.json`, que entra na base do assistente).

## Cálculo (E = P × t)
E(kWh/mês) = pessoas × minutos/60 × potência(kW) × 30 dias. Mesma necessidade (água quente de 4 pessoas) e mesmo período (1 mês).

| Cenário | kWh/mês | R$/mês | Economia R$/mês | CO2 evitado kg/ano | Investimento | Retorno |
|---|---|---|---|---|---|---|
| Atual (8 min) | 88,0 | 79,20 | — | — | — | — |
| A) Banho 5 min | 55,0 | 49,50 | 29,70 | 15,2 | R$ 0 | imediato |
| B) Aquecedor solar (renovável) | 26,4 | 23,76 | 55,44 | 28,5 | R$ 4.000 | ~72 meses |
| A+B | 16,5 | 14,85 | 64,35 | 33,0 | R$ 4.000 | ~62 meses |

## Análise: custos, viabilidade, impacto ambiental
- **A:** custo zero e viabilidade total, mas exige mudança de hábito; menor economia.
- **B:** maior economia, mas investimento alto, retorno de ~6 anos (vida útil estimada 15 anos → ganho líquido ~R$ 6.000), exige telhado com sol e espaço; não funciona igual em dias nublados (por isso 70% de fração solar e chuveiro elétrico de apoio).
- **Ambiental:** o ganho de CO2 é pequeno porque a matriz elétrica brasileira é majoritariamente renovável; o benefício principal é financeiro e de redução de demanda.
- **Recomendação:** começar por A; considerar B se for ficar na casa por mais de 6 anos. Combinação A+B tem o melhor resultado.

## Dados, origem e premissas
Ver `dados_energia.json` (campo `origem_e_status`). **ESTIMADOS:** pessoas, minutos, tarifa, custo e fração solar. **A CONFIRMAR antes da entrega:** tarifa (conta de luz/ANEEL), fator de emissão (MCTI), potência do chuveiro (etiqueta Procel/Inmetro), 3 orçamentos de aquecedor solar.
Referências: ANEEL (https://www.gov.br/aneel), MME (https://www.gov.br/mme), MCTI (https://www.gov.br/mcti), Procel/Inmetro.

## Limitações
Estimativas, não garantias: variam com tarifa (bandeiras), clima, instalação e hábitos. Não considera manutenção, financiamento nem inflação da tarifa.

## Integração com o assistente
`gerar_orientacoes.py` transforma os resultados nas orientações do assistente (com fonte, data e aviso de estimativa). Se mudar uma premissa, rode de novo: a resposta do assistente muda junto.

## Testes com usuários (PREENCHER com testes reais)
| Situação testada | Comentário recebido | Ajuste feito |
|---|---|---|
| ex.: "como economizar no chuveiro" | ... | ... |
