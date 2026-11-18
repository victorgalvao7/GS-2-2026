"""Mobilidade urbana: diagnóstico (Etapa 1), redistribuição (Etapa 2) e avaliação.
Ordem das variáveis: x = (Norte, Sul, Leste, Oeste). Uso: python frota.py"""
import numpy as np
from fractions import Fraction as F

# ---------- ETAPA 1: sistema Ax = b ----------
A = np.array([[1, 1, 1, 1],    # N + S + L + O = 72
              [1, 2, 0, 1],    # N + 2S + O    = 76
              [0, 1, 2, 0],    # S + 2L        = 52
              [1, 0, 1, 2]], dtype=float)  # N + L + 2O = 76
b = np.array([72, 76, 52, 76], dtype=float)
print("det(A) =", round(np.linalg.det(A), 6), "| posto(A) =", np.linalg.matrix_rank(A),
      "| posto([A|b]) =", np.linalg.matrix_rank(np.column_stack([A, b])))
x = np.linalg.solve(A, b)
x = np.round(x).astype(int)
print("Distribuição atual (N,S,L,O):", x.tolist(), "| verificação A@x == b:", np.allclose(A @ x, b))

# ---------- ETAPA 2: demanda e política ----------
dem = np.array([560, 760, 720, 840]); cap = 40
nec = np.ceil(dem / cap).astype(int)
print("Ônibus necessários:", nec.tolist(), "| total:", nec.sum(), "| frota:", x.sum())
print("Saldo (frota - necessário):", (x - nec).tolist())

# Matriz de transformação T(x) = M x. Coluna j = para onde vai cada ônibus da região j.
M = [[F(1), F(0),     F(0), F(1, 12)],   # Norte recebe 1/12 dos ônibus do Oeste
     [F(0), F(19, 20), F(0), F(0)],      # Sul mantém 19/20
     [F(0), F(1, 20), F(1), F(1, 24)],   # Leste recebe 1/20 do Sul e 1/24 do Oeste
     [F(0), F(0),     F(0), F(7, 8)]]    # Oeste mantém 7/8
Mn = np.array([[float(c) for c in l] for l in M])
print("\nSoma de cada coluna:", [str(sum(M[i][j] for i in range(4))) for j in range(4)],
      "| menor coeficiente:", min(c for l in M for c in l))
y = Mn @ x
print("Nova distribuição M@x:", np.round(y, 6).tolist(), "| total:", round(y.sum(), 6))
y = np.round(y).astype(int)

# ---------- AVALIAÇÃO ----------
def avalia(nome, v):
    sem_vaga = np.maximum(dem - v * cap, 0)
    ocup = np.minimum(dem / (v * cap), 9.99) * 100
    print(f"{nome}: passageiros sem vaga = {sem_vaga.tolist()} (total {sem_vaga.sum()}) | ocupação % = {np.round(ocup, 1).tolist()}")
avalia("Antes ", x); avalia("Depois", y)
