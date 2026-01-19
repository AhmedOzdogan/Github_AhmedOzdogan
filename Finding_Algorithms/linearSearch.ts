// Finding_Algorithms/linearSearch.ts
//
// Linear Search (Sequential Search)
//
// - Works on any array (sorted or unsorted)
// - Checks elements one-by-one until target is found
//
// Time Complexity:
//   Best:    O(1)   (target is at index 0)
//   Average: O(n)
//   Worst:   O(n)   (target is at the end or not present)
// Space Complexity: O(1)
//
// NOTE:
// For LARGE + SORTED datasets, consider Binary Search (O(log n)).

import {
    randomDatasetSmall,
    randomDatasetMedium,
    randomDatasetLarge,
    randomDatasetHuge,
} from "./data.ts";

/**
 * Performs linear search on an array.
 * @returns index of target if found, otherwise -1
 */
function linearSearch(arr: number[], target: number): number {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) return i;
    }
    return -1;
}

/**
 * Runs a more reliable benchmark by repeating the search multiple times.
 * This helps reduce noise from JIT warmup / OS scheduling / console overhead.
 */
function benchmarkLinearSearch(
    name: string,
    dataset: number[],
    target: number,
    runs: number
): void {
    // Warm-up run (helps reduce JIT first-run effects)
    linearSearch(dataset, target);

    const label = `Linear Search ${name} (target=${target}, runs=${runs})`;
    console.time(label);
    let index = -1;
    for (let i = 0; i < runs; i++) {
        index = linearSearch(dataset, target);
    }
    console.timeEnd(label);

    console.log(`Dataset size: ${dataset.length}`);
    console.log(`Target found at index: ${index}`);
    console.log("-");
}

// ----------------------------
// Example usage
// ----------------------------

const datasets = {
    small: randomDatasetSmall,
    medium: randomDatasetMedium,
    large: randomDatasetLarge,
    huge: randomDatasetHuge,
};

// Choose targets that definitely exist (our datasets contain 1..n)
const targets = [1, 10];

// Benchmark runs: fewer runs for huge to keep runtime reasonable
const RUNS = {
    small: 50_000,
    medium: 20_000,
    large: 5_000,
    huge: 500,
};

for (const target of targets) {
    console.log(`\n========== Linear Search Benchmarks (target=${target}) ==========`);

    benchmarkLinearSearch("small", datasets.small, target, RUNS.small);
    benchmarkLinearSearch("medium", datasets.medium, target, RUNS.medium);
    benchmarkLinearSearch("large", datasets.large, target, RUNS.large);
    benchmarkLinearSearch("huge", datasets.huge, target, RUNS.huge);
}

// Output timings will vary depending on your computer and runtime.
// The important takeaway is how time grows as dataset size increases (O(n)).


//Results Example:
/*========== Linear Search Benchmarks (target=1) ==========
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
Target found at index: 15118*/

