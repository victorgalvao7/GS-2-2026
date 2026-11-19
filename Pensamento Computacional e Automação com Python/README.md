# Citizen Assist AI — Assistente Digital de Orientação ao Cidadão
**Integrantes:** [Victor Vieira Galvão - 571483], [Miguel Silverio de Avila - 568873], [Artur Souza Pereira - 570880]
**Vídeo técnico:** [[LINK YOUTUBE](https://youtu.be/MXPuTdmol1U)] | **Outras disciplinas:** ver abaixo

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

## Teste com usuários
Testado com **3 pessoas de fora da equipe** (4 sessões de uso), somando **21 atendimentos**. Nenhum nome ou dado pessoal foi registrado; as pessoas aparecem como Usuário 1, 2 e 3.

**Indicadores (opção 3 do menu):**

| Indicador | Resultado |
|---|---|
| Atendimentos | 21 (3 com ajuda da IA) |
| Resposta encontrada (%) | 81,0 (17 de 21) |
| Taxa de acerto: ajudou (%) | 100,0 (17 de 17 encontradas) |
| Tempo médio para encontrar | 17,2 s |
| Tentativas por atendimento | 1,24 |
| Facilidade de uso (1 a 5) | 3,25 (notas 4, 3, 5 e 1 nas 4 sessões) |

**Dúvidas sem solução (busca por pontuação, sem IA):**
- "como faço pra tirar o cartão do ônibus?"
- "comprei uma coisa e veio com defeito, o que eu faço?"
- "minha conta de luz veio alta"
- "comprei um produto com deifeito aonde reclamo" (erro de digitação)

**Comentários recebidos:**
- **Usuário 1:** "Achei fácil de usar e ele respondeu todas as minhas perguntas sem problema nenhum. Ajudaria bastante no dia a dia."
- **Usuário 2:** "Gostei do sistema. Ele conseguiu responder a maioria das minhas perguntas; as que ele não encontrou sozinho, a IA ligada conseguiu responder. Recomendaria para outras pessoas usarem quando tiverem dúvidas."
- **Usuário 3:** "Mesmo sem entender muito de tecnologia, consegui usar, e o app respondeu algumas das minhas perguntas e outras não. Achei bom, mas não achei fácil de usar."

**Melhorias feitas a partir do teste:**
- Novas palavras-chave na orientação 1 (ônibus): `cartao do onibus`, `cartao onibus`, `busao`, `tirar cartao`.
- Novas palavras-chave na orientação 9 (consumidor): `defeito`, `veio com defeito`, `com defeito`, `defeituoso`.
- As perguntas sobre cartão do ônibus e produto com defeito, que não eram encontradas, passaram a ser encontradas só pela pontuação.
- Alteração ao vivo (vídeo): palavra-chave `conta de luz` na orientação 11, para "minha conta de luz veio alta".

**Observação:** com a IA ligada, "minha conta de luz veio alta" foi ligada à Tarifa Social (orientação 10), que não é a orientação mais adequada. Por isso a palavra-chave foi adicionada.

## Limitações
Busca por palavras-chave (não entende sinônimos não cadastrados); base pequena (12 orientações); links apontam para páginas iniciais dos órgãos; não é canal oficial.

## Integração com IA (OpenAI) — opcional

**Como funciona:** a busca por pontuação (+3 palavra-chave, +1 título) continua sendo a 1ª etapa. Só quando ela não encontra
(menos de 3 pontos) a pergunta é enviada à API da OpenAI (`ia.py`). A IA **não responde sozinha**: ela apenas escolhe, entre as
orientações verificadas do JSON, quais respondem à dúvida e resume em linguagem simples usando só o texto da base. Ids inventados são descartados.
Assim a regra "proibido inventar informações" continua valendo, e a fonte, a data de verificação e o aviso aparecem do mesmo jeito.

**Privacidade:** o bloqueio de dados pessoais roda ANTES; perguntas com CPF/telefone/e-mail nunca chegam à API nem ao histórico.

**Como ativar:** copie `.env.example` para `.env` e coloque a chave (o `.env` está no `.gitignore`, não vai pro GitHub). Sem chave ou sem internet,
o assistente funciona normalmente só com a pontuação. No menu, a opção 5 liga/desliga a IA.
Modelo padrão: `gpt-4o-mini` (troque com `OPENAI_MODEL` no `.env`).

**Limitações:** a IA depende de internet e da chave; só escolhe entre as orientações existentes (se o assunto não está na base, ela responde "não encontrei").

