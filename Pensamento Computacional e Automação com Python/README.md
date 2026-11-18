# Citizen Assist AI — Assistente Digital de Orientação ao Cidadão
**Integrantes:** [Victor Vieira Galvão - 571483], [Miguel Silverio de Avila - 568873], [Artur Souza Pereira - 570880]
**Vídeo técnico:** [LINK YOUTUBE] | **Outras disciplinas:** ver abaixo

## Público e problema
Moradores de bairros periféricos de São Paulo que perdem tempo procurando orientações de **transporte, saúde, documentos, consumo e energia** em sites confusos ou falsos. O assistente responde só com a base verificada, mostra fonte, data e aviso, e não coleta dados pessoais.
**ODS:** 7 (energia limpa e acessível), 10 (redução das desigualdades), 11 (cidades e comunidades sustentáveis), 16 (instituições eficazes).

## Como executar
`python main.py` (Python 3, sem bibliotecas externas).

## Regra de pontuação
+3 por palavra-chave da orientação na pergunta; +1 por palavra da pergunta (4+ letras) no título. ≥6 pontos = ALTA; 3–5 = MÉDIA; <3 = "não encontrei". `buscar()` devolve lista de tuplas `(pontos, orientacao)`; mostramos a melhor e até 2 alternativas. Pesos originais do enunciado, sem alteração.

## Integração com outras disciplinas
- **Energias Renováveis:** categoria "Energia" gerada pela análise de consumo do chuveiro (repo: [https://github.com/victorgalvao7/GS-2-2026/tree/main/Solu%C3%A7%C3%B5es%20em%20Energias%20Renov%C3%A1veis%20e%20Sustent%C3%A1veis]).
- **Modelagem Matemática:** orientação "Redistribuição de ônibus" usa o resultado da simulação da frota (repo: [https://github.com/victorgalvao7/GS-2-2026/tree/main/Modelagem%20Matem%C3%A1tica%20e%20computacional]).

## Fontes consultadas
SPTrans, gov.br/saude, Receita Federal, gov.br/trabalho-e-emprego, TSE, Consumidor.gov.br, ANEEL, MME. Cada orientação traz fonte e data de verificação no JSON.

## Teste com usuários (PREENCHER)
Pessoas externas: [3+] | Atendimentos: [10+] | Indicadores: [colar saída da opção 3] | Dúvidas sem solução: [...] | Melhoria feita: [ex.: nova palavra-chave X]

## Limitações
Busca por palavras-chave (não entende sinônimos não cadastrados); base pequena (12 orientações); links apontam para páginas iniciais dos órgãos; não é canal oficial.
