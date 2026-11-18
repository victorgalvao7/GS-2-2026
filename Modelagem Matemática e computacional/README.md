# Mobilidade Urbana Inteligente — Modelagem Matemática e Computacional (GS 2026.2)
Integrantes: **[Victor Vieira Galvão - 571483]**, **[Miguel Silverio de Avila - 568873]**, **[Artur Souza Pereira - 570880]**
Vídeo: **[LINK YOUTUBE]** | Executar: `pip install numpy` e `python frota.py`

## Etapa 1 — Diagnóstico
Variáveis: N, S, L, O = nº de ônibus em Norte, Sul, Leste, Oeste (inteiros ≥ 0).
Sistema `A·x = b`:

| | N | S | L | O | = |
|---|---|---|---|---|---|
| frota total | 1 | 1 | 1 | 1 | 72 |
| N + O + 2S | 1 | 2 | 0 | 1 | 76 |
| S + 2L | 0 | 1 | 2 | 0 | 52 |
| N + L + 2O | 1 | 0 | 1 | 2 | 76 |

**Unicidade:** det(A) = 3 ≠ 0, logo posto(A) = 4 = nº de incógnitas (A inversível) e o sistema tem **solução única**: x = A⁻¹b.
Resolução à mão: de (2) N+O = 76−2S; em (1): L = S−4; em (3): 3S = 60 → S = 20, L = 16; em (4): N+2O = 60 e N+O = 36 → O = 24, N = 12.
**Resultado: N=12, S=20, L=16, O=24.** Verificação: 12+20+16+24=72 ✓; 12+24+40=76 ✓; 20+32=52 ✓; 12+16+48=76 ✓. (o código também verifica `A@x == b`).

## Etapa 2 — Redistribuição
Necessidade = ⌈passageiros / 40⌉ → N=14, S=19, L=18, O=21 (total 72 = frota, sem folga).
Saldo atual − necessário: N −2, S +1, L −2, O +3 → Norte e Leste têm déficit; Sul e Oeste têm excedente (4 ônibus).

**Política (critério: eliminar o déficit mantendo a frota e mexendo o mínimo):** só regiões com excedente cedem ônibus, só regiões com déficit recebem.
T(x) = M·x, com M (coluna j = destino dos ônibus da região j; ordem N,S,L,O):

```
      N    S     L    O
N [  1    0     0   1/12 ]
S [  0  19/20   0    0   ]
L [  0   1/20   1   1/24 ]
O [  0    0     0   7/8  ]
```
Significado: `M[i][j]` = fração dos ônibus da região j que passa a operar na região i. Ex.: 1/12 dos ônibus do Oeste (2 ônibus) vão ao Norte; 1/20 do Sul (1) e 1/24 do Oeste (1) vão ao Leste; a diagonal é a fração que fica.

**Linearidade:** T(αu+βv) = M(αu+βv) = αMu + βMv (produto de matriz por vetor).
**Preserva o total:** cada coluna soma 1 (1; 19/20+1/20; 1; 1/12+1/24+7/8 = 2/24+1/24+21/24 = 1), então 1ᵀM = 1ᵀ e 1ᵀ(Mx) = 1ᵀx = 72.
**Sem alocação negativa:** todos os coeficientes são ≥ 0 e x ≥ 0 ⇒ Mx ≥ 0.
**Resultado:** M·(12,20,16,24) = (14,19,18,21) — inteiros e igual à necessidade.

## Avaliação
| | Passageiros sem vaga (N,S,L,O) | Total | Ocupação % |
|---|---|---|---|
| Antes | 80, 0, 80, 0 | 160 | 116,7 / 95 / 112,5 / 87,5 |
| Depois | 0, 0, 0, 0 | 0 | 100 / 100 / 100 / 100 |

## Limitações
Dados hipotéticos; M foi calibrada para este x (para outro vetor, o resultado pode não ser inteiro e M precisa de novo ajuste); com frota = demanda não há folga para picos reais; ignora distância entre centros e tempo de deslocamento.
