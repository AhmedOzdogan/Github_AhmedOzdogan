This folder contains finding algorithms
# Finding Algorithms (Search Methods)

This folder contains **5 classic searching algorithms** implemented in **TypeScript** and benchmarked using datasets of different sizes.

## ✅ Implemented algorithms

1. **Linear Search** (`linearSearch.ts`)
2. **Binary Search** (`binarySearch.ts`)
3. **Jump Search** (`jumpSearch.ts`)
4. **Interpolation Search** (`interpolationSearch.ts`)
5. **Exponential Search** (`exponentialSearch.ts`)

---

## Datasets (`data.ts`)

All search algorithms use datasets defined in `data.ts`.

### Dataset sizes

| Size | Range | Length |
|------|-------|--------|
| small | `1 .. 20` | 20 |
| medium | `1 .. 200` | 200 |
| large | `1 .. 2000` | 2000 |
| huge | `1 .. 20000` | 20000 |

### Dataset types

- **random** → deterministic shuffled permutation of `1..n` (every value exists exactly once, but unordered)
- **increasing** → sorted ascending `1..n`
- **decreasing** → sorted descending `n..1`

✅ Because datasets contain **exactly the values `1..n`**, you can always practice searching for any number in that range.

---

## Quick complexity overview

| Algorithm | Requires Sorted? | Needs Uniform Distribution? | Average Time | Worst Time | Space |
|----------|-------------------|-----------------------------|--------------|------------|-------|
| Linear Search | ❌ No | ❌ No | **O(n)** | **O(n)** | O(1) |
| Binary Search | ✅ Yes | ❌ No | **O(log n)** | **O(log n)** | O(1) |
| Jump Search | ✅ Yes | ❌ No | **O(√n)** | **O(√n)** | O(1) |
| Interpolation Search | ✅ Yes | ✅ Best case | **O(log log n)** | **O(n)** | O(1) |
| Exponential Search | ✅ Yes | ❌ No | **O(log n)** | **O(log n)** | O(1) |

---

## 1) Linear Search

**File:** `linearSearch.ts`

### Idea
Checks each element one-by-one until the target is found.

### When to use
- Dataset is **unsorted** (random datasets)
- Dataset is small
- You want the simplest method

### Complexity
- Best: `O(1)`
- Average/Worst: `O(n)`
- Space: `O(1)`

---

## 2) Binary Search

**File:** `binarySearch.ts`

### Idea
Repeatedly divides the array in half and eliminates half of the remaining search range each step.

### Requirements
- Array must be **sorted** (usually increasing)

### Complexity
- Average/Worst: `O(log n)`
- Space: `O(1)`

---

## 3) Jump Search

**File:** `jumpSearch.ts`

### Idea
Jumps ahead by blocks of size `√n` until it finds a block where the target may exist, then performs linear search in that block.

### Requirements
- Array must be **sorted**

### Complexity
- Average/Worst: `O(√n)`
- Space: `O(1)`

---

## 4) Interpolation Search

**File:** `interpolationSearch.ts`

### Idea
Estimates where the target should be based on its value relative to the current low/high bounds.

### Requirements
- Array must be **sorted**
- Best results when values are **uniformly distributed** (like `1..n`)

### Complexity
- Best: `O(1)`
- Average (uniform): `O(log log n)`
- Worst: `O(n)`
- Space: `O(1)`

---

## 5) Exponential Search

**File:** `exponentialSearch.ts`

### Idea
Finds a search range by checking indices `1, 2, 4, 8, 16, ...` (doubling each time), then runs binary search inside the discovered range.

### Requirements
- Array must be **sorted**

### Complexity
- Average/Worst: `O(log n)`
- Space: `O(1)`

---

## ▶️ Running the algorithms

From the `Finding_Algorithms/` folder:

```bash
node linearSearch.ts
node binarySearch.ts
node jumpSearch.ts
node interpolationSearch.ts
node exponentialSearch.ts
```

> If your environment does not support running `.ts` directly with Node, use `ts-node`:

```bash
npx ts-node linearSearch.ts
```

---

## 📊 Benchmark notes

- Each algorithm includes a benchmark function that repeats the search multiple times.
- A warm-up run is included to reduce JIT first-run noise.
- **Timings will vary** depending on:
  - CPU speed
  - current system load
  - Node/TypeScript runtime

The main learning goal is comparing **how runtime scales** as dataset size increases.

---

## ✅ Example results

Below are **real sample outputs** (your numbers may differ).

### Linear Search (random datasets)

```txt
========== Linear Search Benchmarks (target=1) ==========
Linear Search small (target=1, runs=50000): 1.73ms
Dataset size: 20
Target found at index: 18
-
Linear Search medium (target=1, runs=20000): 2.19ms
Dataset size: 200
Target found at index: 161
-
Linear Search large (target=1, runs=5000): 1.845ms
Dataset size: 2000
Target found at index: 568
-
Linear Search huge (target=1, runs=500): 5.253ms
Dataset size: 20000
Target found at index: 15851
-

========== Linear Search Benchmarks (target=10) ==========
Linear Search small (target=10, runs=50000): 0.986ms
Dataset size: 20
Target found at index: 17
-
Linear Search medium (target=10, runs=20000): 2.264ms
Dataset size: 200
Target found at index: 164
-
Linear Search large (target=10, runs=5000): 6.269ms
Dataset size: 2000
Target found at index: 1884
-
Linear Search huge (target=10, runs=500): 4.954ms
Dataset size: 20000
Target found at index: 15118
```

### Jump Search (sorted increasing datasets)

```txt
**************************************************
Searching for last elements:
**************************************************
Jump Search small (target=20, runs=100): 0.104ms
Dataset size: 20
Target found at index: 19
-
Jump Search medium (target=200, runs=100): 0.061ms
Dataset size: 200
Target found at index: 199
-
Jump Search large (target=2000, runs=100): 0.163ms
Dataset size: 2000
Target found at index: 1999
-
Jump Search huge (target=20000, runs=100): 0.17ms
Dataset size: 20000
Target found at index: 19999
```

### Interpolation Search (sorted + uniformly distributed)

```txt
**************************************************
Searching for middle elements:
**************************************************
Interpolation Search small (target=11, runs=100000): 0.504ms
Dataset size: 20
Target found at index: 10
-
Interpolation Search medium (target=101, runs=100000): 0.504ms
Dataset size: 200
Target found at index: 100
-
Interpolation Search large (target=1001, runs=100000): 0.643ms
Dataset size: 2000
Target found at index: 1000
-
Interpolation Search huge (target=10001, runs=100000): 0.918ms
Dataset size: 20000
Target found at index: 10000
```

### Exponential Search (sorted increasing datasets)

```txt
**************************************************
Searching for first elements:
**************************************************
Exponential Search small (target=1, runs=100000): 0.287ms
Dataset size: 20
Target found at index: 0
-
Exponential Search medium (target=1, runs=100000): 0.251ms
Dataset size: 200
Target found at index: 0
-
Exponential Search large (target=1, runs=100000): 0.252ms
Dataset size: 2000
Target found at index: 0
-
Exponential Search huge (target=1, runs=100000): 0.298ms
Dataset size: 20000
Target found at index: 0
```

---

## Learning goal

Try searching for:
- first element
- middle element
- last element

and observe how each algorithm scales.
