import time
import numpy as np
import matplotlib.pyplot as plt
import sys
from functools import wraps
from matplotlib.ticker import ScalarFormatter

# Aumenta o limite de recursão para Quick Sort e Merge Sort em listas grandes
sys.setrecursionlimit(20000)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_recursive(arr, low, high):
    if low < high:
        pi = quick_sort_partition(arr, low, high)
        quick_sort_recursive(arr, low, pi - 1)
        quick_sort_recursive(arr, pi + 1, high)
    return arr

def quick_sort(arr):
    return quick_sort_recursive(arr, 0, len(arr) - 1)


def time_it(func, arr):
    """Mede o tempo de execução de uma função de ordenação."""
    arr_copy = arr.copy()
    start_time = time.perf_counter()
    func(arr_copy)
    end_time = time.perf_counter()
    return end_time - start_time

#gera cenarios
def generate_random_data(n):
    return np.random.randint(0, n, n)

def generate_sorted_data(n):
    return np.arange(n)

def generate_reversed_data(n):
    return np.arange(n, 0, -1)

def generate_data_with_repetitions(n):
    return np.random.randint(0, n // 10, n) # Garante muitas repetições


#func principal e plotagem
def run_and_plot_scenario(scenario_name, data_generator, sizes):
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }
    
    results = {name: [] for name in algorithms}
    
    print(f"--- Iniciando Teste: {scenario_name} ---")

    for n in sizes:
        print(f"  Testando com lista de tamanho n = {n}...")
        data = data_generator(n)
        
        for name, func in algorithms.items():
            if name in ["Bubble Sort", "Selection Sort", "Insertion Sort"] and n > 5000:
                time_taken = float('inf')
            else:
                time_taken = time_it(func, data)
            
            results[name].append(time_taken)
            print(f"    {name}: {time_taken:.6f} segundos")

    # Plotagem
    plt.style.use('seaborn-v0_8-darkgrid') # Usando o estilo corrigido
    fig, ax = plt.subplots(figsize=(12, 8))

    for name, times in results.items():
        plot_sizes = [s for s, t in zip(sizes, times) if t != float('inf')]
        plot_times = [t for t in times if t != float('inf')]
        ax.plot(plot_sizes, plot_times, marker='o', linestyle='-', label=name)

    ax.set_xlabel("Tamanho da Lista (n)", fontsize=12)
    ax.set_ylabel("Tempo de Execução (segundos)", fontsize=12)
    ax.set_title(f"Comparativo de Desempenho - {scenario_name}", fontsize=16)
    ax.legend()
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.grid(True, which="both", ls="--")


    #converte rotulos log em numero normal
    ax.xaxis.set_major_formatter(ScalarFormatter())
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.set_xticks(sizes)
    plt.show()


if __name__ == "__main__":
    list_sizes = [100, 500, 1000, 2500, 5000, 10000]
    run_and_plot_scenario("Dados Aleatórios", generate_random_data, list_sizes)
    run_and_plot_scenario("Dados Já Ordenados", generate_sorted_data, list_sizes)
    run_and_plot_scenario("Dados Ordenados Inversamente", generate_reversed_data, list_sizes)
    run_and_plot_scenario("Dados com Muitas Repetições", generate_data_with_repetitions, list_sizes)