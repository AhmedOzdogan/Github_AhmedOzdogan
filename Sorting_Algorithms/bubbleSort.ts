// Sorting_Algorithms/bubbleSort.ts
//
// Bubble Sort
//
// Idea:
// Repeatedly steps through the array, compares adjacent elements and swaps them
// if they are in the wrong order. The pass through the list is repeated until
// the array is sorted.
//
// Time Complexity:
//   Best:    O(n)     (already sorted + early-exit optimization)
//   Average: O(n^2)
//   Worst:   O(n^2)
// Space Complexity: O(1) (in-place)
//
// NOTE:
// Bubble sort is mainly for learning. It becomes extremely slow on large datasets.

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
 * Sorts an array of numbers in ascending order using Bubble Sort.
 * Mutates the input array (in-place).
 */
export function bubbleSort(arr: number[]): number[] {
    const n = arr.length;
    for (let i = 0; i < n - 1; i++) {
        let swapped = false;
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
                swapped = true;
            }
        }
        // Early exit: if no swaps were made, the array is already sorted.
        if (!swapped) break;
    }
    return arr;
}

/**
 * Benchmarks Bubble Sort by sorting a fresh copy of the dataset multiple times.
 * We must copy because bubbleSort mutates arrays.
 */
function benchmarkBubbleSort(name: string, dataset: number[], runs: number): void {
    // warm-up
    bubbleSort([...dataset]);

    const label = `Bubble Sort ${name} (n=${dataset.length}, runs=${runs})`;
    console.time(label);
    let out: number[] = [];
    for (let i = 0; i < runs; i++) {
        out = bubbleSort([...dataset]);
    }
    console.timeEnd(label);

    // quick correctness check (not a full proof)
    const isSorted = out.every((v, idx) => idx === 0 || out[idx - 1] <= v);
    console.log(`Dataset size: ${dataset.length}`);
    console.log(`Sorted correctly: ${isSorted}`);
    console.log("-");
}

// ----------------------------
// Example usage / Benchmarks
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

// Bubble sort is O(n^2), so we use fewer runs as size increases.
const RUNS = {
    small: 2000,
    medium: 200,
    large: 10,
    huge: 5,
};

console.log("\n========== Bubble Sort Benchmarks (random datasets) ==========");
benchmarkBubbleSort("small", randomDatasets.small, RUNS.small);
benchmarkBubbleSort("medium", randomDatasets.medium, RUNS.medium);
benchmarkBubbleSort("large", randomDatasets.large, RUNS.large);
benchmarkBubbleSort("huge", randomDatasets.huge, RUNS.huge);

console.log("\n========== Bubble Sort Benchmarks (increasing datasets) ==========");
benchmarkBubbleSort("small", increasingDatasets.small, RUNS.small);
benchmarkBubbleSort("medium", increasingDatasets.medium, RUNS.medium);
benchmarkBubbleSort("large", increasingDatasets.large, RUNS.large);
benchmarkBubbleSort("huge", increasingDatasets.huge, RUNS.huge);

console.log("\n========== Bubble Sort Benchmarks (decreasing datasets) ==========");
benchmarkBubbleSort("small", decreasingDatasets.small, RUNS.small);
benchmarkBubbleSort("medium", decreasingDatasets.medium, RUNS.medium);
benchmarkBubbleSort("large", decreasingDatasets.large, RUNS.large);
benchmarkBubbleSort("huge", decreasingDatasets.huge, RUNS.huge);

// Timings will vary by machine/runtime.

//Example Output:
/*
========== Bubble Sort Benchmarks (random datasets) ==========
Bubble Sort small (n=20, runs=2000): 4.547ms
Dataset size: 20
Sorted correctly: true
-
Bubble Sort medium (n=200, runs=200): 9.917ms
Dataset size: 200
Sorted correctly: true
-
Bubble Sort large (n=2000, runs=10): 49.404ms
Dataset size: 2000
Sorted correctly: true
-
Bubble Sort huge (n=20000, runs=5): 2.351s
Dataset size: 20000
Sorted correctly: true
-

========== Bubble Sort Benchmarks (increasing datasets) ==========
Bubble Sort small (n=20, runs=2000): 0.166ms
Dataset size: 20
Sorted correctly: true
-
Bubble Sort medium (n=200, runs=200): 0.138ms
Dataset size: 200
Sorted correctly: true
-
Bubble Sort large (n=2000, runs=10): 0.079ms
Dataset size: 2000
Sorted correctly: true
-
Bubble Sort huge (n=20000, runs=5): 0.443ms
Dataset size: 20000
Sorted correctly: true
-

========== Bubble Sort Benchmarks (decreasing datasets) ==========
Bubble Sort small (n=20, runs=2000): 1.07ms
Dataset size: 20
Sorted correctly: true
-
Bubble Sort medium (n=200, runs=200): 9.963ms
Dataset size: 200
Sorted correctly: true
-
Bubble Sort large (n=2000, runs=10): 47.545ms
Dataset size: 2000
Sorted correctly: true
-
Bubble Sort huge (n=20000, runs=5): 2.348s
Dataset size: 20000
Sorted correctly: true
-
=====================================================*/