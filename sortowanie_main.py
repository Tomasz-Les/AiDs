import random
import time
import matplotlib.pyplot as plt

# ==========================================
# GENERATORY TABLIC
# ==========================================
def gen_random(n): return [random.randint(0, n) for _ in range(n)]
def gen_ascending(n): return list(range(n))
def gen_descending(n): return list(range(n, 0, -1))
def gen_constant(n): return [5] * n
def gen_v_shape(n): 
    mid = n // 2
    return list(range(mid, 0, -1)) + list(range(1, n - mid + 1))
def gen_a_shape(n): 
    mid = n // 2
    return list(range(1, mid + 1)) + list(range(n - mid, 0, -1))

# ==========================================
# ALGORYTMY SORTOWANIA - CZĘŚĆ I
# ==========================================

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]: largest = l
    if r < n and arr[r] > arr[largest]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

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

# ==========================================
# ALGORYTMY SORTOWANIA - CZĘŚĆ II
# ==========================================
# Implementacja iteracyjna Quicksort (z własnym stosem)

def partition(arr, l, h, pivot_type):
    if pivot_type == 'right':
        p_idx = h
    elif pivot_type == 'middle':
        p_idx = (l + h) // 2
    elif pivot_type == 'random':
        p_idx = random.randint(l, h)
    
    # Zamiana wybranego pivotu z ostatnim elementem (standardowy podział Lomuto)
    arr[p_idx], arr[h] = arr[h], arr[p_idx]
    pivot = arr[h]
    
    i = l - 1
    for j in range(l, h):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1

def quicksort_iterative(arr, pivot_type='right'):
    size = len(arr)
    stack = [0] * (size)
    top = -1
    
    top = top + 1
    stack[top] = 0
    top = top + 1
    stack[top] = size - 1

    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        p = partition(arr, l, h, pivot_type)

        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


# ==========================================
# FUNKCJE POMIAROWE I RYSUJĄCE
# ==========================================

def measure_time(sort_func, data):
    start = time.perf_counter()
    sort_func(data)
    end = time.perf_counter()
    return end - start

def run_part_1():
    # 15 punktów pomiarowych, od n=200 do n=3000 (dostosuj dla szybszych/wolniejszych PC)
    n_values = [i * 200 for i in range(1, 16)]
    
    algorithms = {
        'Insertion Sort': insertion_sort,
        'Selection Sort': selection_sort,
        'Heap Sort': heap_sort,
        'Merge Sort': merge_sort
    }
    
    generators = {
        'Losowa': gen_random,
        'Rosnąca': gen_ascending,
        'Malejąca': gen_descending,
        'Stała': gen_constant,
        'V-kształtna': gen_v_shape
    }

    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Część I: Porównanie 4 metod sortowania t = f(n)')
    axs = axs.flatten()

    for idx, (algo_name, algo_func) in enumerate(algorithms.items()):
        print(f"Pomiary dla: {algo_name}")
        for gen_name, gen_func in generators.items():
            times = []
            for n in n_values:
                # Tworzymy kopię danych, aby sortować za każdym razem świeżą tablicę
                data = gen_func(n)
                t = measure_time(algo_func, data)
                times.append(t)
            axs[idx].plot(n_values, times, label=gen_name, marker='o', markersize=4)
        
        axs[idx].set_title(algo_name)
        axs[idx].set_xlabel('Liczba elementów (n)')
        axs[idx].set_ylabel('Czas (s)')
        axs[idx].legend()
        axs[idx].grid(True)

    plt.tight_layout()
    plt.show()

def run_part_2():
    # 15 punktów pomiarowych, n od 500 do 7500
    n_values = [i * 500 for i in range(1, 16)]
    pivot_types = ['right', 'middle', 'random']
    
    plt.figure(figsize=(10, 6))
    plt.title('Część II: Quicksort dla tablicy A-kształtnej wg wyboru pivotu')
    
    for pt in pivot_types:
        print(f"Pomiary Quicksort dla pivotu: {pt}")
        times = []
        for n in n_values:
            data = gen_a_shape(n)
            start = time.perf_counter()
            quicksort_iterative(data, pivot_type=pt)
            end = time.perf_counter()
            times.append(end - start)
        plt.plot(n_values, times, label=f'Pivot: {pt}', marker='s')

    plt.xlabel('Liczba elementów (n)')
    plt.ylabel('Czas (s)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    print("Rozpoczynam pomiary Części I...")
    run_part_1()
    print("Rozpoczynam pomiary Części II...")
    run_part_2()