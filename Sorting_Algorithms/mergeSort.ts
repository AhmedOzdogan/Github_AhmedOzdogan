// Sorting_Algorithms/mergeSort.ts
//
// Merge Sort
//
// Idea:
// Divides the array into halves, recursively sorts each half, and then merges
// the sorted halves back together.
//
// Time Complexity:
//   Best:    O(n log n)
//   Average: O(n log n)
//   Worst:   O(n log n)
// Space Complexity: O(n) (not in-place)
//
// NOTE:
// Merge sort is stable and works well for large datasets. However, it requires
// additional space proportional to the size of the input array.

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

/** Merges two sorted arrays into one sorted array. */
function merge(left: number[], right: number[]): number[] {
    const result: number[] = [];
    let i = 0;
    let j = 0;

    while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) {
            result.push(left[i]);
            i++;
        } else {
            result.push(right[j]);
            j++;
        }
    }

    // Append remaining elements
    return result.concat(left.slice(i)).concat(right.slice(j));
}

/** Sorts an array of numbers in ascending order using Merge Sort. */
export function mergeSort(arr: number[]): number[] {
    if (arr.length <= 1) {
        return arr;
    }

    const mid = Math.floor(arr.length / 2);
    const left = mergeSort(arr.slice(0, mid));
    const right = mergeSort(arr.slice(mid));

    return merge(left, right);
}


/**
 * Benchmarks Merge Sort by sorting a fresh copy of the dataset multiple times.
 * We must copy because mergeSort does not mutate arrays, but we want to ensure
 * consistent input for each run.
 */
function benchmarkMergeSort(name: string, dataset: number[], runs: number): void {
    // warm-up
    mergeSort([...dataset]);

    const label = `Merge Sort ${name} (n=${dataset.length}, runs=${runs})`;
    console.time(label);
    let out: number[] = [];
    for (let i = 0; i < runs; i++) {
        out = mergeSort([...dataset]);
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
console.log("\n================= Merge Sort Benchmarks (Random Datasets) =================");
benchmarkMergeSort("Random Small", randomDatasetSmall, 1000);
benchmarkMergeSort("Random Medium", randomDatasetMedium, 100);
benchmarkMergeSort("Random Large", randomDatasetLarge, 10);
benchmarkMergeSort("Random Huge", randomDatasetHuge, 1);


console.log("\n================= Merge Sort Benchmarks (Increasing Datasets) =================");
benchmarkMergeSort("Increasing Small", increasingDatasetSmall, 1000);
benchmarkMergeSort("Increasing Medium", increasingDatasetMedium, 100);
benchmarkMergeSort("Increasing Large", increasingDatasetLarge, 10);
benchmarkMergeSort("Increasing Huge", increasingDatasetHuge, 1);


console.log("\n================= Merge Sort Benchmarks (Decreasing Datasets) =================");
benchmarkMergeSort("Decreasing Small", decreasingDatasetSmall, 1000);
benchmarkMergeSort("Decreasing Medium", decreasingDatasetMedium, 100);
benchmarkMergeSort("Decreasing Large", decreasingDatasetLarge, 10);
benchmarkMergeSort("Decreasing Huge", decreasingDatasetHuge, 1);

// Timings will vary based on machine performance.

/*
\n================= Merge Sort Benchmarks (Random Datasets) =================
Merge Sort Random Small (n=20, runs=1000): 6.864ms
Dataset size: 20
Sorted correctly: true
-
Merge Sort Random Medium (n=200, runs=100): 6.659ms
Dataset size: 200
Sorted correctly: true
-
Merge Sort Random Large (n=2000, runs=10): 8.049ms
Dataset size: 2000
Sorted correctly: true
-
Merge Sort Random Huge (n=20000, runs=1): 9.326ms
Dataset size: 20000
Sorted correctly: true
-

================= Merge Sort Benchmarks (Increasing Datasets) =================
Merge Sort Increasing Small (n=20, runs=1000): 5.28ms
Dataset size: 20
Sorted correctly: true
-
Merge Sort Increasing Medium (n=200, runs=100): 5.857ms
Dataset size: 200
Sorted correctly: true
-
Merge Sort Increasing Large (n=2000, runs=10): 6.247ms
Dataset size: 2000
Sorted correctly: true
-
Merge Sort Increasing Huge (n=20000, runs=1): 8.704ms
Dataset size: 20000
Sorted correctly: true
-

================= Merge Sort Benchmarks (Decreasing Datasets) =================
Merge Sort Decreasing Small (n=20, runs=1000): 6.95ms
Dataset size: 20
Sorted correctly: true
-
Merge Sort Decreasing Medium (n=200, runs=100): 5.919ms
Dataset size: 200
Sorted correctly: true
-
Merge Sort Decreasing Large (n=2000, runs=10): 6.253ms
Dataset size: 2000
Sorted correctly: true
-
Merge Sort Decreasing Huge (n=20000, runs=1): 6.643ms
Dataset size: 20000
Sorted correctly: true
=============================================================*/