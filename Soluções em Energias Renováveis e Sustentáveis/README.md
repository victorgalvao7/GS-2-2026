# Energias Renováveis e Sustentáveis — contribuição ao Citizen Assist AI

Integrantes: **Victor Vieira Galvão - 571483**, **Miguel Silverio de Avila - 568873**, **Artur Souza Pereira - 570880** | Vídeo (máx. 3 min): **[\[LINK DO VÍDEO\]](https://youtu.be/B_g2C736j9Y)**

Repositório do assistente completo: **https://github.com/victorgalvao7/GS-2-2026/tree/main/Pensamento%20Computacional%20e%20Automa%C3%A7%C3%A3o%20com%20Python** (as orientações de energia estão na categoria "Energia", IDs 11 e 12).

## Público e necessidade

Moradores de casas com chuveiro elétrico que querem reduzir a conta de luz. O banho é um dos consumos relevantes de uma residência, e a análise compara a redução do tempo de banho com a adoção de aquecimento solar de água.

## Como executar

`python calculo_energia.py` (mostra os cálculos e gera `resultados_energia.json`) e `python gerar_orientacoes.py` (gera `orientacoes_energia.json`, que alimenta a base do assistente).

## Cálculo (E = P × t)

A energia mensal foi estimada por: E (kWh/mês) = número de pessoas × (minutos de banho ÷ 60) × potência do chuveiro (kW) × 30 dias.

Premissas utilizadas: 4 pessoas, chuveiro elétrico de 5.500 W (5,5 kW), banho de 8 minutos no cenário atual ou 5 minutos na alternativa A, e mês de 30 dias. Para a alternativa solar, foi considerada uma fração solar estimada de 70%, com o chuveiro elétrico como apoio. A tarifa de referência adotada é **R$ 0,78938/kWh**, correspondente à soma de TE (R$ 0,31696/kWh) e TUSD (R$ 0,47242/kWh), antes de impostos, bandeiras e demais componentes da conta. Para facilitar a leitura, os valores monetários abaixo estão arredondados para centavos.

| Cenário | kWh/mês | R$/mês | Economia R$/mês | CO2 evitado kg/ano | Investimento | Retorno simples |
|---|---:|---:|---:|---:|---:|---:|
| Atual (8 min) | 88,0 | R$ 69,47 | — | — | — | — |
| A) Banho 5 min | 55,0 | R$ 43,42 | R$ 26,05 | 15,2 | R$ 0 | imediato |
| B) Aquecedor solar (renovável) | 26,4 | R$ 20,84 | R$ 48,63 | 28,5 | R$ 5.500 | ~113 meses (9,4 anos) |
| A+B | 16,5 | R$ 13,03 | R$ 56,44 | 33,0 | R$ 5.500 | ~97 meses (8,1 anos) |

**Como interpretar o retorno:** é uma estimativa simples, calculada dividindo o investimento pelo valor de economia mensal de cada cenário em comparação ao cenário atual. Na alternativa B, R$ 5.500 ÷ R$ 48,63 ≈ 113 meses. Na combinação A+B, R$ 5.500 ÷ R$ 56,44 ≈ 97 meses. O retorno real pode ser diferente e depende do custo instalado, uso, clima, manutenção e tarifa.

## Análise: custos, viabilidade e impacto ambiental

- **A — banho de 5 minutos:** custo inicial zero e aplicação simples, mas exige mudança de hábito. A economia estimada é de R$ 26,05 por mês em relação ao banho de 8 minutos.
- **B — aquecedor solar:** utiliza uma fonte renovável e reduz a energia elétrica necessária para aquecer a água. Foi adotado investimento estimado de **R$ 5.500 para um sistema residencial de referência de aproximadamente 300 litros**. O valor é uma premissa de estudo, não um orçamento confirmado para um imóvel específico. A viabilidade depende de telhado adequado, insolação, instalação e necessidade de apoio elétrico em períodos nublados.
- **A+B:** combina banho mais curto com aquecimento solar. É o cenário de menor consumo elétrico estimado e maior economia mensal entre os cenários analisados.
- **Ambiental:** os valores de CO2 evitado são estimativas calculadas a partir da energia elétrica economizada e de um fator de emissão de referência. O resultado é relativamente pequeno porque a matriz elétrica brasileira possui participação elevada de fontes renováveis. O benefício principal do projeto é a redução do consumo e do custo de energia.
- **Recomendação:** começar pela redução do tempo de banho, que não exige investimento. Considerar o aquecedor solar após comparar orçamentos e avaliar por quanto tempo a família pretende permanecer no imóvel. Com as premissas adotadas, o retorno estimado do sistema solar isolado é de aproximadamente 9,4 anos; portanto, a decisão depende do custo final e do horizonte de permanência.

## Dados, origem e premissas

Os dados utilizados devem estar registrados em `dados_energia.json`, no campo `origem_e_status`.

- **Tarifa:** R$ 0,78938/kWh, referência calculada pela soma de TE e TUSD da tarifa residencial convencional da área de concessão da Enel São Paulo, antes de impostos, bandeiras e outros itens da fatura. A tarifa efetivamente paga na Vila Formosa pode variar conforme classe, modalidade, tributos, bandeira e regras vigentes. Para uma conta real, conferir a fatura do imóvel e a tabela tarifária vigente da distribuidora.
- **Potência do chuveiro:** 5.500 W, valor nominal adotado como referência para um chuveiro elétrico residencial 220 V. Conferir a etiqueta do aparelho instalado; a potência varia conforme modelo e tensão.
- **Aquecedor solar:** R$ 5.500, estimativa de investimento para um sistema residencial de referência de aproximadamente 300 litros. É necessário confirmar o preço com orçamentos de fornecedores, incluindo coletores, reservatório, instalação e eventuais adaptações hidráulicas.
- **Demais premissas:** 4 moradores, 8 ou 5 minutos de banho, 30 dias por mês e fração solar de 70% são hipóteses de simulação, não medições de uma residência específica.
- **CO2:** estimativa baseada em fator de emissão de referência; deve ser atualizada com o fator oficial do período estudado.

## Referências para consulta

- ANEEL — tarifas e processos tarifários: https://www.gov.br/aneel/pt-br/assuntos/tarifas
- Enel São Paulo — informações e tarifas para clientes: https://www.enel.com.br/pt-saopaulo.html
- MCTI — fatores de emissão de gases de efeito estufa: https://www.gov.br/mcti/
- Procel/Inmetro — informações sobre eficiência e etiquetagem de equipamentos: https://www.gov.br/inmetro/
- Lorenzetti — fabricante; consultar a ficha técnica do modelo de chuveiro utilizado: https://www.lorenzetti.com.br/

**Importante:** o investimento de R$ 5.500 e a potência de 5.500 W são premissas de referência para a simulação. Antes da entrega, confirmem o preço do sistema solar com cotações e a potência na etiqueta do chuveiro. A tarifa deve ser conferida na fatura ou na tabela vigente da distribuidora. Não apresentem esses valores como medição real da residência.

## Limitações

Os resultados são estimativas, não garantias. Variam com a tarifa efetiva, bandeiras, impostos, clima, orientação e área do telhado, dimensionamento e instalação do sistema, temperatura da água, hábitos de banho e eficiência dos equipamentos. O cálculo não considera manutenção, financiamento, inflação tarifária nem custos extras de instalação. O retorno é simples e não representa uma análise financeira completa.

## Integração com o assistente

`gerar_orientacoes.py` transforma os resultados nas orientações do assistente (com fonte, data e aviso de estimativa). Se uma premissa for alterada, executar novamente `calculo_energia.py` e `gerar_orientacoes.py` para atualizar os resultados e as orientações exibidas ao usuário.

## Testes com usuários

Testado com 3 pessoas de fora da equipe (sem registro de nomes ou dados pessoais), junto com os testes do assistente (21 atendimentos no total).

| Situação testada | Comentário recebido | Ajuste feito |
|---|---|---|
| "como gasto menos no chuveiro?" | Encontrou a orientação 11 em 4,7 s e a pessoa disse que ajudou. | Nenhum necessário. |
| "vale a pena o aquecedor solar?" | Encontrou a orientação 12 em 7,8 s e a pessoa disse que ajudou. | Nenhum necessário. |
| "minha conta de luz veio alta" | Sem a IA, não foi encontrada. Com a IA ligada, foi ligada à Tarifa Social, que não responde sobre economia. | Palavra-chave `conta de luz` adicionada à orientação 11 (feita na gravação do vídeo). |
| Comentários gerais | Usuário 1: fácil de usar e respondeu tudo. Usuário 2: respondeu a maioria, e a IA ajudou nas outras. Usuário 3: conseguiu usar sem entender de tecnologia, mas não achou fácil. | Mantida a linguagem simples; palavras-chave novas para perguntas não encontradas. |
