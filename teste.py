import random
import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(2000)

def criaListaCrescente(numero):
    return [i for i in range(numero)]

def criaListaInvertida(numero):
    return [numero - i for i in range(numero)]

def bubblesort_ascendente(lista):
    tamanho = len(lista)
    for i in range(tamanho - 1):
        for j in range(tamanho - 1 - i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def bubblesort_descendente(lista):
    tamanho = len(lista)
    for i in range(tamanho - 1):
        for j in range(tamanho - 1 - i):
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def quicksort(lista, inicio=None, fim=None):
    if inicio is None:
        inicio = 0
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        posicao_pivo = particao(lista, inicio, fim)
        quicksort(lista, inicio, posicao_pivo - 1)
        quicksort(lista, posicao_pivo + 1, fim)
    return lista

def particao(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1

def comparar_pior_caso(max_elementos=1500, passo=50):
    tamanhos = []
    tempos_bubble_asc = []
    tempos_bubble_desc = []
    tempos_quicksort = []


    for i in range(10, max_elementos, passo):
        tamanhos.append(i)

        lista_pior_caso_bs_asc = criaListaInvertida(i)
        ini = time.time_ns()
        bubblesort_ascendente(lista_pior_caso_bs_asc)
        fim = time.time_ns()
        tempos_bubble_asc.append(fim - ini)

        lista_pior_caso_bs_desc = criaListaCrescente(i)
        ini = time.time_ns()
        bubblesort_descendente(lista_pior_caso_bs_desc)
        fim = time.time_ns()
        tempos_bubble_desc.append(fim - ini)

        lista_pior_caso_qs = criaListaCrescente(i)
        ini = time.time_ns()
        quicksort(lista_pior_caso_qs)
        fim = time.time_ns()
        tempos_quicksort.append(fim - ini)
        
    plt.figure(figsize=(12, 8))
    plt.plot(tamanhos, tempos_bubble_asc, label='Bubble Sort (Crescente) - Pior Caso', marker='.')
    plt.plot(tamanhos, tempos_bubble_desc, label='Bubble Sort (Decrescente) - Pior Caso', marker='.')
    plt.plot(tamanhos, tempos_quicksort, label='Quick Sort - Pior Caso', marker='.')

    plt.xlabel('Número de Elementos na Lista')
    plt.ylabel('Tempo de Execução (nanossegundos)')
    plt.title('Comparação de Pior Caso de Cada Algoritmo')
    plt.legend()
    plt.grid(True)
    plt.show()

comparar_pior_caso()