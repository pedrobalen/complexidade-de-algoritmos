import random
import time
import matplotlib.pyplot as plt
def cria_vetor_py(tamanho):
    return [random.random() for _ in range(tamanho)]

def cria_matriz_py(tamanho):
    return [[random.random() for _ in range(tamanho)] for _ in range(tamanho)]

def soma_vetores_py(v1, v2):
    tamanho = len(v1)
    resultado = [0] * tamanho
    for i in range(tamanho):
        resultado[i] = v1[i] + v2[i]
    return resultado

def vetor_matriz_py(vetor, matriz):
    num_linhas = len(vetor)
    num_colunas = len(matriz[0])
    resultado = [0] * num_colunas
    
    for j in range(num_colunas):
        soma = 0
        for i in range(num_linhas):
            soma += vetor[i] * matriz[i][j]
        resultado[j] = soma
    return resultado

def matriz_matriz_py(m1, m2):
    num_linhas_m1 = len(m1)
    num_colunas_m2 = len(m2[0])
    num_colunas_m1 = len(m1[0]) 
 
    resultado = [[0 for _ in range(num_colunas_m2)] for _ in range(num_linhas_m1)]
    
    for i in range(num_linhas_m1):
        for j in range(num_colunas_m2):
            for k in range(num_colunas_m1):
                resultado[i][j] += m1[i][k] * m2[k][j]
    return resultado

def comparar_operacoes_py(max_tamanho=150):
    tamanhos = []
    tempos_soma_vetores = []
    tempos_vetor_matriz = []
    tempos_matriz_matriz = []

    print("--- Iniciando comparação com Python puro ---")

    for n in range(1, max_tamanho + 1):
        tamanhos.append(n)

        vetor1 = cria_vetor_py(n)
        vetor2 = cria_vetor_py(n)
        matriz1 = cria_matriz_py(n)
        matriz2 = cria_matriz_py(n)

 
        ini = time.perf_counter_ns()
        soma_vetores_py(vetor1, vetor2)
        fim = time.perf_counter_ns()
        tempos_soma_vetores.append(fim - ini)

        ini = time.perf_counter_ns()
        vetor_matriz_py(vetor1, matriz1)
        fim = time.perf_counter_ns()
        tempos_vetor_matriz.append(fim - ini)

        ini = time.perf_counter_ns()
        matriz_matriz_py(matriz1, matriz2)
        fim = time.perf_counter_ns()
        tempos_matriz_matriz.append(fim - ini)

        if n % 10 == 0:
            print(f"Processado para dimensão n = {n}")


    plt.figure(figsize=(12, 8))
    plt.plot(tamanhos, tempos_soma_vetores, label='Soma de Vetores ($O(n)$)', marker='.')
    plt.plot(tamanhos, tempos_vetor_matriz, label='Vetor * Matriz ($O(n^2)$)', marker='.')
    plt.plot(tamanhos, tempos_matriz_matriz, label='Matriz * Matriz ($O(n^3)$)', marker='.')

    plt.xlabel('Dimensão (n)')
    plt.ylabel('Tempo de Execução (nanossegundos)')
    plt.title('Comparação de Complexidade com Python Puro')
    plt.legend()
    plt.grid(True)
    plt.show()


comparar_operacoes_py(max_tamanho=1000)