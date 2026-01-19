// Sorting_Algorithms/selectionSort.ts
//
// Selection Sort
//
// Idea:
// Repeatedly selects the smallest (or largest) element from the unsorted portion
// of the array and moves it to the beginning (or end).
//
// Time Complexity:
//   Best:    O(n^2)
//   Average: O(n^2)
//   Worst:   O(n^2)
// Space Complexity: O(1) (in-place)
//
// NOTE:
// Selection sort is not a stable sort. It is mainly for learning purposes and
// is inefficient on large datasets.

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

/**
 * Sorts an array of numbers in ascending order using Selection Sort.
 * Mutates the input array (in-place).
 */
export function selectionSort(arr: number[]): number[] {
    const n = arr.length;
    for (let i = 0; i < n - 1; i++) {
        let minIndex = i;
        for (let j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        if (minIndex !== i) {
            [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
        }
    }
    return arr;
}

/**
 * Benchmarks Selection Sort by sorting a fresh copy of the dataset multiple times.
 * We must copy because selectionSort mutates arrays.
 */
function benchmarkSelectionSort(name: string, dataset: number[], runs: number): void {
    // warm-up
    selectionSort([...dataset]);

    const label = `Selection Sort ${name} (n=${dataset.length}, runs=${runs})`;
    console.time(label);
    let out: number[] = [];
    for (let i = 0; i < runs; i++) {
        out = selectionSort([...dataset]);
    }
    console.timeEnd(label);

    // quick correctness check
    const isSorted = out.every((val, index, array) => index === 0 || array[index - 1] <= val);
    console.log(`Dataset size: ${dataset.length}`);
    console.log(`Sorted correctly: ${isSorted}`);
    console.log("-");
}


// ----------------------------
// Running benchmarks
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

// Selection sort is O(n^2) and thus only feasible for small datasets in practice.
const RUNS = {
    small: 2000,
    medium: 200,
    large: 10,
    huge: 5,
};

console.log("\n========== Selection Sort Benchmarks (random datasets) ==========");
benchmarkSelectionSort("small", randomDatasets.small, RUNS.small);
benchmarkSelectionSort("medium", randomDatasets.medium, RUNS.medium);
benchmarkSelectionSort("large", randomDatasets.large, RUNS.large);
benchmarkSelectionSort("huge", randomDatasets.huge, RUNS.huge); // too large

console.log("\n========== Selection Sort Benchmarks (increasing datasets) ==========");
benchmarkSelectionSort("small", increasingDatasets.small, RUNS.small);
benchmarkSelectionSort("medium", increasingDatasets.medium, RUNS.medium);
benchmarkSelectionSort("large", increasingDatasets.large, RUNS.large);
benchmarkSelectionSort("huge", increasingDatasets.huge, RUNS.huge); // too large

console.log("\n========== Selection Sort Benchmarks (decreasing datasets) ==========");
benchmarkSelectionSort("small", decreasingDatasets.small, RUNS.small);
benchmarkSelectionSort("medium", decreasingDatasets.medium, RUNS.medium);
benchmarkSelectionSort("large", decreasingDatasets.large, RUNS.large);
benchmarkSelectionSort("huge", decreasingDatasets.huge, RUNS.huge); // too large

// Timings will vary based on machine performance.

// Example Output:
/*
========== Selection Sort Benchmarks (random datasets) ==========
Selection Sort small (n=20, runs=2000): 2.787ms
Dataset size: 20
Sorted correctly: true
-
Selection Sort medium (n=200, runs=200): 5.558ms
Dataset size: 200
Sorted correctly: true
-
Selection Sort large (n=2000, runs=10): 24.5ms
Dataset size: 2000
Sorted correctly: true
-
Selection Sort huge (n=20000, runs=5): 1.215s
Dataset size: 20000
Sorted correctly: true
-

========== Selection Sort Benchmarks (increasing datasets) ==========
Selection Sort small (n=20, runs=2000): 1.054ms
Dataset size: 20
Sorted correctly: true
-
Selection Sort medium (n=200, runs=200): 5.423ms
Dataset size: 200
Sorted correctly: true
-
Selection Sort large (n=2000, runs=10): 25.448ms
Dataset size: 2000
Sorted correctly: true
-
Selection Sort huge (n=20000, runs=5): 1.245s
Dataset size: 20000
Sorted correctly: true
-

========== Selection Sort Benchmarks (decreasing datasets) ==========
Selection Sort small (n=20, runs=2000): 0.804ms
Dataset size: 20
Sorted correctly: true
-
Selection Sort medium (n=200, runs=200): 5.513ms
Dataset size: 200
Sorted correctly: true
-
Selection Sort large (n=2000, runs=10): 24.641ms
Dataset size: 2000
Sorted correctly: true
-
Selection Sort huge (n=20000, runs=5): 1.199s
Dataset size: 20000
Sorted correctly: true
-*/