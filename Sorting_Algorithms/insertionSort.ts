// Sorting_Algorithms/InsertionSort.ts
//
// Insertion Sort
//
// Idea:
// Builds the final sorted array one item at a time by repeatedly taking
// the next element from the input and inserting it into the correct position
//
// Time Complexity:
//   Best:    O(n)      (already sorted)
//   Average: O(n^2)
//   Worst:   O(n^2)    (reverse sorted)
// Space Complexity: O(1) (in-place)
//
// NOTE:
// Insertion sort is efficient for small datasets and mostly sorted data.
// It is stable and in-place, making it useful for certain applications.

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


/** * Sorts an array of numbers in ascending order using Insertion Sort.
 * Mutates the input array (in-place).
 */
export function insertionSort(arr: number[]): number[] {
  const n = arr.length;
  for (let i = 1; i < n; i++) {
    const key = arr[i];
    let j = i - 1;

    // Move elements of arr[0..i-1], that are greater than key,
    // to one position ahead of their current position
    while (j >= 0 && arr[j] > key) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = key;
  }
  return arr;
}


/**
 * Benchmarks Insertion Sort by sorting a fresh copy of the dataset multiple times.
 * We must copy because insertionSort mutates arrays.
 */
function benchmarkInsertionSort(name: string, dataset: number[], runs: number): void {
  // warm-up
  insertionSort([...dataset]);

  const label = `Insertion Sort ${name} (n=${dataset.length}, runs=${runs})`;
  console.time(label);
  let out: number[] = [];
  for (let i = 0; i < runs; i++) {
    out = insertionSort([...dataset]);
  }
  console.timeEnd(label);

  // quick correctness check
  const isSorted = out.every((val, idx, array) => idx === 0 || array[idx - 1] <= val);
  console.log(`Dataset size: ${dataset.length}`);
  console.log(`  Sorted correctly: ${isSorted}`);
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
}

const increasingDatasets = {
  small: increasingDatasetSmall,
  medium: increasingDatasetMedium,
  large: increasingDatasetLarge,
  huge: increasingDatasetHuge,
}

const decreasingDatasets = {
  small: decreasingDatasetSmall,
  medium: decreasingDatasetMedium,
  large: decreasingDatasetLarge,
  huge: decreasingDatasetHuge,
}

// Insertion Sort is 0(n^2) in average and worst cases, so we limit the runs for large and huge datasets
const runsConfig = {
  small: 1000,
  medium: 500,
  large: 10,
  huge: 5,
};

console.log("============= Insertion Sort Benchmarks ===========");
benchmarkInsertionSort("Random Small", randomDatasets.small, runsConfig.small);
benchmarkInsertionSort("Random Medium", randomDatasets.medium, runsConfig.medium);
benchmarkInsertionSort("Random Large", randomDatasets.large, runsConfig.large);
benchmarkInsertionSort("Random Huge", randomDatasets.huge, runsConfig.huge);

console.log("============= Insertion Sort Benchmarks (Increasing Datasets) ===========");
benchmarkInsertionSort("Increasing Small", increasingDatasets.small, runsConfig.small);
benchmarkInsertionSort("Increasing Medium", increasingDatasets.medium, runsConfig.medium);
benchmarkInsertionSort("Increasing Large", increasingDatasets.large, runsConfig.large);
benchmarkInsertionSort("Increasing Huge", increasingDatasets.huge, runsConfig.huge);

console.log("============= Insertion Sort Benchmarks (Decreasing Datasets) ===========");
benchmarkInsertionSort("Decreasing Small", decreasingDatasets.small, runsConfig.small);
benchmarkInsertionSort("Decreasing Medium", decreasingDatasets.medium, runsConfig.medium);
benchmarkInsertionSort("Decreasing Large", decreasingDatasets.large, runsConfig.large);
benchmarkInsertionSort("Decreasing Huge", decreasingDatasets.huge, runsConfig.huge);

// Timings will vary based on machine performance.

/*============= Insertion Sort Benchmarks ===========
Insertion Sort Random Small (n=20, runs=1000): 0.589ms
Dataset size: 20
  Sorted correctly: true
-
Insertion Sort Random Medium (n=200, runs=500): 7.165ms
Dataset size: 200
  Sorted correctly: true
-
Insertion Sort Random Large (n=2000, runs=10): 12.822ms
Dataset size: 2000
  Sorted correctly: true
-
Insertion Sort Random Huge (n=20000, runs=5): 622.292ms
Dataset size: 20000
  Sorted correctly: true
-
============= Insertion Sort Benchmarks (Increasing Datasets) ===========
Insertion Sort Increasing Small (n=20, runs=1000): 0.555ms
Dataset size: 20
  Sorted correctly: true
-
Insertion Sort Increasing Medium (n=200, runs=500): 0.318ms
Dataset size: 200
  Sorted correctly: true
-
Insertion Sort Increasing Large (n=2000, runs=10): 0.067ms
Dataset size: 2000
  Sorted correctly: true
-
Insertion Sort Increasing Huge (n=20000, runs=5): 0.442ms
Dataset size: 20000
  Sorted correctly: true
-
============= Insertion Sort Benchmarks (Decreasing Datasets) ===========
Insertion Sort Decreasing Small (n=20, runs=1000): 0.292ms
Dataset size: 20
  Sorted correctly: true
-
Insertion Sort Decreasing Medium (n=200, runs=500): 13.248ms
Dataset size: 200
  Sorted correctly: true
-
Insertion Sort Decreasing Large (n=2000, runs=10): 25.152ms
Dataset size: 2000
  Sorted correctly: true
-
Insertion Sort Decreasing Huge (n=20000, runs=5): 1.372s
Dataset size: 20000
  Sorted correctly: true
-*/