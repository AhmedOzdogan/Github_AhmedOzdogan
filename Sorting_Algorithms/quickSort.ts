// Sorting_Algorithms/quickSort.ts

// Quick Sort
//
// Idea:
// Selects a 'pivot' element and partitions the array into elements less than
// the pivot and elements greater than the pivot, then recursively sorts the partitions.
//
// Time Complexity:
//   Best:    O(n log n)
//   Average: O(n log n)
//   Worst:   O(n^2)    (rare, occurs with poor pivot choices)
// Space Complexity: O(log n) (due to recursion stack)
//
// NOTE:
// Quick sort is generally faster in practice compared to other O(n log n)
// algorithms like merge sort and heap sort, especially for large datasets.
// However, it is not a stable sort.

import {
    randomDatasetSmall,
    randomDatasetMedium,
    randomDatasetLarge,
    randomDatasetHuge,
    increasingDatasetSmall,
    increasingDatasetMedium,
    increasingDatasetLarge,
    increasingDatasetHuge,
    decreasingDatasetSmall,
    decreasingDatasetMedium,
    decreasingDatasetLarge,
    decreasingDatasetHuge,
} from "./data.ts";

// Deterministic PRNG for reproducible benchmarks
function mulberry32(seed: number) {
    let t = seed >>> 0;
    return function next() {
        t += 0x6d2b79f5;
        let r = Math.imul(t ^ (t >>> 15), 1 | t);
        r ^= r + Math.imul(r ^ (r >>> 7), 61 | r);
        return ((r ^ (r >>> 14)) >>> 0) / 4294967296;
    };
}

/** Partitions the array around a pivot and returns the pivot index. */
function partition(
    arr: number[],
    low: number,
    high: number,
    pivot: 'first' | 'middle' | 'last' | 'random',
    rand: () => number
): number {
    let pivotIndex: number;
    switch (pivot) {
        case 'first':
            pivotIndex = low;
            break;
        case 'middle':
            pivotIndex = Math.floor((low + high) / 2);
            break;
        case 'last':
            pivotIndex = high;
            break;
        case 'random':
            pivotIndex = Math.floor(rand() * (high - low + 1)) + low;
            break;
    }
    const pivotValue = arr[pivotIndex];
    // Move pivot to end
    [arr[pivotIndex], arr[high]] = [arr[high], arr[pivotIndex]];
    let storeIndex = low;

    for (let i = low; i < high; i++) {
        if (arr[i] < pivotValue) {
            [arr[i], arr[storeIndex]] = [arr[storeIndex], arr[i]];
            storeIndex++;
        }
    }
    // Move pivot to its final place
    [arr[storeIndex], arr[high]] = [arr[high], arr[storeIndex]];
    return storeIndex;
}

/** Sorts an array of numbers in ascending order using Quick Sort. */
export function quickSort(
    arr: number[],
    low = 0,
    high = arr.length - 1,
    pivot: 'first' | 'middle' | 'last' | 'random' = 'middle',
    rand: () => number = Math.random
): number[] {
    if (low < high) {
        const pivotIndex = partition(arr, low, high, pivot, rand);
        quickSort(arr, low, pivotIndex - 1, pivot, rand);
        quickSort(arr, pivotIndex + 1, high, pivot, rand);
    }
    return arr;
}

/**
 * Benchmarks Quick Sort by sorting a fresh copy of the dataset multiple times.
 * We must copy because quickSort mutates arrays.
 */
function benchmarkQuickSort(name: string, dataset: number[], runs: number, pivot: 'first' | 'middle' | 'last' | 'random' = 'middle'): void {
    const rand = mulberry32(12345 + dataset.length + (pivot === 'first' ? 1 : pivot === 'middle' ? 2 : pivot === 'last' ? 3 : 4));
    // warm-up
    quickSort([...dataset], 0, dataset.length - 1, pivot, rand);

    const label = `Quick Sort (${pivot} pivot) ${name} (n=${dataset.length}, runs=${runs})`;
    console.time(label);
    let out: number[] = [];
    for (let i = 0; i < runs; i++) {
        // fresh PRNG for each run so the pivot sequence is identical across runs
        const runRand = mulberry32(12345 + dataset.length + (pivot === 'first' ? 1 : pivot === 'middle' ? 2 : pivot === 'last' ? 3 : 4) + i);
        out = quickSort([...dataset], 0, dataset.length - 1, pivot, runRand);
    }
    console.timeEnd(label);


    // quick correctness check
    const isSorted = out.every((val, index, array) => index === 0 || array[index - 1] <= val);
    console.log(`Dataset size: ${dataset.length}`);
    console.log(`Sorted correctly: ${isSorted}`);
    console.log("-");
}

// ----------------------------
// Run benchmarks
// ----------------------------

const randomDatasets = {
    small: randomDatasetSmall,
    medium: randomDatasetMedium,
    large: randomDatasetLarge,
    huge: randomDatasetHuge,
};
const increasingDatasets = {
    small: increasingDatasetSmall,
    medium: increasingDatasetMedium,
    large: increasingDatasetLarge,
    huge: increasingDatasetHuge,
};
const decreasingDatasets = {
    small: decreasingDatasetSmall,
    medium: decreasingDatasetMedium,
    large: decreasingDatasetLarge,
    huge: decreasingDatasetHuge,
};
const RUNS = {
    small: 1000,
    medium: 100,
    large: 10,
    huge: 5,
};

const sizes = ["small", "medium", "large"] as const;
const pivots = ["first", "middle", "last", "random"] as const;

console.log("\n========== Quick Sort Benchmarks (random datasets) ==========");
for (const size of sizes) {
    for (const pivotValue of pivots) {
        benchmarkQuickSort(size, randomDatasets[size], RUNS[size], pivotValue);
    }
}

console.log("\n========== Quick Sort Benchmarks (increasing datasets) ==========");
for (const size of sizes) {
    for (const pivotValue of pivots) {
        benchmarkQuickSort(size, increasingDatasets[size], RUNS[size], pivotValue);
    }
}

console.log("\n========== Quick Sort Benchmarks (decreasing datasets) ==========");
for (const size of sizes) {
    for (const pivotValue of pivots) {
        benchmarkQuickSort(size, decreasingDatasets[size], RUNS[size], pivotValue);
    }
}

// Timings will vary based on machine performance.
// Huge datasets with O(n^2) pivot choices (first/last on sorted data) are avoided here.

/* Example Output:
========== Quick Sort Benchmarks (random datasets) ==========
Quick Sort (first pivot) small (n=20, runs=1000): 3.72ms
Dataset size: 20
Sorted correctly: true
-
Quick Sort (middle pivot) small (n=20, runs=1000): 3.616ms
Dataset size: 20
Sorted correctly: true
-
Quick Sort (last pivot) small (n=20, runs=1000): 2.162ms
Dataset size: 20
Sorted correctly: true
-
Quick Sort (random pivot) small (n=20, runs=1000): 4.501ms
Dataset size: 20
Sorted correctly: true
-
Quick Sort (first pivot) medium (n=200, runs=100): 3.447ms
Dataset size: 200
Sorted correctly: true
-
Quick Sort (middle pivot) medium (n=200, runs=100): 1.39ms
Dataset size: 200
Sorted correctly: true
-
Quick Sort (last pivot) medium (n=200, runs=100): 0.548ms
Dataset size: 200
Sorted correctly: true
-
Quick Sort (random pivot) medium (n=200, runs=100): 1.543ms
Dataset size: 200
Sorted correctly: true
-
Quick Sort (first pivot) large (n=2000, runs=10): 0.837ms
Dataset size: 2000
Sorted correctly: true
-
Quick Sort (middle pivot) large (n=2000, runs=10): 1.312ms
Dataset size: 2000
Sorted correctly: true
-
Quick Sort (last pivot) large (n=2000, runs=10): 0.803ms
Dataset size: 2000
Sorted correctly: true
-
Quick Sort (random pivot) large (n=2000, runs=10): 1.968ms
Dataset size: 2000
Sorted correctly: true
-

========== Quick Sort Benchmarks (increasing datasets) ==========
Quick Sort (first pivot) small (n=20, runs=1000): 0.485ms
Dataset size: 20
Sorted correctly: true
-
Quick Sort (middle pivot) small (n=20, runs=1000): 0.394ms
Dataset size: 20
Sorted correctly: true
-
Quick Sort (last pivot) small (n=20, runs=1000): 0.647ms
Dataset size: 20
Sorted correctly: true
-
Quick Sort (random pivot) small (n=20, runs=1000): 1.077ms
Dataset size: 20
Sorted correctly: true
-
Quick Sort (first pivot) medium (n=200, runs=100): 2.791ms
Dataset size: 200
Sorted correctly: true
-
Quick Sort (middle pivot) medium (n=200, runs=100): 0.435ms
Dataset size: 200
Sorted correctly: true
-
Quick Sort (last pivot) medium (n=200, runs=100): 4.584ms
Dataset size: 200
Sorted correctly: true
-
Quick Sort (random pivot) medium (n=200, runs=100): 1.165ms
Dataset size: 200
Sorted correctly: true
-
Quick Sort (first pivot) large (n=2000, runs=10): 22.418ms
Dataset size: 2000
Sorted correctly: true
-
Quick Sort (middle pivot) large (n=2000, runs=10): 0.477ms
Dataset size: 2000
Sorted correctly: true
-
Quick Sort (last pivot) large (n=2000, runs=10): 40.029ms
Dataset size: 2000
Sorted correctly: true
-
Quick Sort (random pivot) large (n=2000, runs=10): 1.197ms
Dataset size: 2000
Sorted correctly: true
-

========== Quick Sort Benchmarks (decreasing datasets) ==========
Quick Sort (first pivot) small (n=20, runs=1000): 0.655ms
Dataset size: 20
Sorted correctly: true
-
Quick Sort (middle pivot) small (n=20, runs=1000): 0.336ms
Dataset size: 20
Sorted correctly: true
-
Quick Sort (last pivot) small (n=20, runs=1000): 0.585ms
Dataset size: 20
Sorted correctly: true
-
Quick Sort (random pivot) small (n=20, runs=1000): 1.099ms
Dataset size: 20
Sorted correctly: true
-
Quick Sort (first pivot) medium (n=200, runs=100): 3.591ms
Dataset size: 200
Sorted correctly: true
-
Quick Sort (middle pivot) medium (n=200, runs=100): 0.536ms
Dataset size: 200
Sorted correctly: true
-
Quick Sort (last pivot) medium (n=200, runs=100): 3.67ms
Dataset size: 200
Sorted correctly: true
-
Quick Sort (random pivot) medium (n=200, runs=100): 1.227ms
Dataset size: 200
Sorted correctly: true
-
Quick Sort (first pivot) large (n=2000, runs=10): 31.18ms
Dataset size: 2000
Sorted correctly: true
-
Quick Sort (middle pivot) large (n=2000, runs=10): 0.645ms
Dataset size: 2000
Sorted correctly: true
-
Quick Sort (last pivot) large (n=2000, runs=10): 30.886ms
Dataset size: 2000
Sorted correctly: true
-
Quick Sort (random pivot) large (n=2000, runs=10): 1.465ms
Dataset size: 2000
Sorted correctly: true
-*/
