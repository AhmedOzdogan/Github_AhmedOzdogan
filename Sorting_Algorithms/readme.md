

# Sorting Algorithms (Top 5)

This folder contains **5 classic sorting algorithms** implemented in **TypeScript** with benchmarking output across different dataset sizes.

## ✅ Implemented algorithms

1. **Bubble Sort** (`bubbleSort.ts`)
2. **Selection Sort** (`selectionSort.ts`)
3. **Insertion Sort** (`insertionSort.ts`)
4. **Merge Sort** (`mergeSort.ts`)
5. **Quick Sort** (`quickSort.ts`) — includes **different pivot strategies**

---

## Datasets (`data.ts`)

All sorting algorithms import datasets from `data.ts`.

### Dataset sizes

| Size | Range | Length |
|------|-------|--------|
| small | `1 .. 20` | 20 |
| medium | `1 .. 200` | 200 |
| large | `1 .. 2000` | 2000 |
| huge | `1 .. 20000` | 20000 |

### Dataset patterns

- **random** → deterministic shuffled permutation of `1..n` (all values exist exactly once, unordered)
- **increasing** → already sorted `1..n`
- **decreasing** → reverse sorted `n..1`

> ⚠️ Most sorting algorithms **mutate arrays**. For fair benchmarking, each benchmark sorts a **copy** of the dataset using `[...dataset]`.

---

## Quick complexity overview

| Algorithm | Best Time | Average Time | Worst Time | Space | Stable? |
|----------|-----------|--------------|------------|-------|---------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ No |

---

## Algorithm summaries

### 1) Bubble Sort

**Idea:** repeatedly compares and swaps adjacent elements.

- Very slow on random/large input (**O(n²)**)
- With early exit optimization, best case becomes **O(n)** on sorted input

---

### 2) Selection Sort

**Idea:** repeatedly finds the smallest element in the unsorted region and swaps it to the front.

- Always **O(n²)** comparisons regardless of input order
- Fewer swaps than bubble sort, but still slow for large inputs

---

### 3) Insertion Sort

**Idea:** builds a sorted prefix by inserting each new element into its correct position.

- Excellent for **nearly sorted** arrays
- Best case **O(n)** when already sorted
- Worst case **O(n²)** on reverse sorted arrays

---

### 4) Merge Sort

**Idea:** divide array in half, sort halves recursively, then merge.

- Always **O(n log n)** (best/avg/worst)
- Requires extra memory (**O(n)**)
- Great for large datasets

---

### 5) Quick Sort (with pivot strategies)

**Idea:** choose a pivot, partition array into smaller/larger parts, recursively sort both sides.

Pivot strategies included:
- `first`
- `middle`
- `last`
- `random` (seeded deterministic PRNG for reproducible benchmarks)

Notes:
- Quick sort is fast in practice, but can degrade to **O(n²)** with bad pivots.
- Worst case often occurs on sorted input if using `first` or `last` pivot.
- Huge datasets with worst-case pivot choices are avoided in benchmarks to prevent stack overflow.

---

## ▶️ Running the algorithms

From the `Sorting_Algorithms/` folder:

```bash
node bubbleSort.ts
node selectionSort.ts
node insertionSort.ts
node mergeSort.ts
node quickSort.ts
```

If your environment does not support running `.ts` directly:

```bash
npx ts-node bubbleSort.ts
```

---

## 📊 Benchmark notes

- A warm-up run is included to reduce first-run JIT noise.
- Each algorithm is run multiple times (`runs`) depending on dataset size.
- **Timings vary** depending on CPU/runtime load.

The learning goal is to observe how runtime scales:
- **O(n²)** sorts become extremely slow as size grows
- **O(n log n)** sorts remain fast even for large sizes

---

## ✅ Example results

These are sample outputs from this project (your numbers will differ).

### Bubble Sort (shows best vs worst case)

```txt
========== Bubble Sort Benchmarks (random datasets) ==========
Bubble Sort huge (n=20000, runs=5): 2.351s
...

========== Bubble Sort Benchmarks (increasing datasets) ==========
Bubble Sort huge (n=20000, runs=5): 0.443ms
...

========== Bubble Sort Benchmarks (decreasing datasets) ==========
Bubble Sort huge (n=20000, runs=5): 2.348s
...
```

### Insertion Sort (adaptive algorithm)

```txt
Insertion Sort Random Huge (n=20000, runs=5): 622.292ms
Insertion Sort Increasing Huge (n=20000, runs=5): 0.442ms
Insertion Sort Decreasing Huge (n=20000, runs=5): 1.372s
```

### Merge Sort (consistent O(n log n))

```txt
Merge Sort Random Huge (n=20000, runs=1): 9.326ms
Merge Sort Increasing Huge (n=20000, runs=1): 8.704ms
Merge Sort Decreasing Huge (n=20000, runs=1): 6.643ms
```

### Quick Sort with different pivots

```txt
========== Quick Sort Benchmarks (increasing datasets) ==========
Quick Sort (first pivot) large (n=2000, runs=10): 22.418ms
Quick Sort (middle pivot) large (n=2000, runs=10): 0.477ms
Quick Sort (last pivot) large (n=2000, runs=10): 40.029ms
Quick Sort (random pivot) large (n=2000, runs=10): 1.197ms
```

This example shows how pivot choice can make quick sort much faster or much slower on sorted data.

---