// Finding_Algorithms/ExponentialSearch.ts

// Exponential Search
//
// - Works only on SORTED arrays
// - Finds range where target may be present by repeated doubling
// - Then performs binary search within that range
//
// Time Complexity:
//   Best:    O(1)   (target is at first index)
//   Average: O(log n)
//   Worst:   O(log n)   (target is at one of the ends or not present)
//
// Space Complexity: O(1)
//
// NOTE:
// For SMALL or UNSORTED datasets, consider Linear Search (O(n)).

import {
    increasingDatasetSmall,
    increasingDatasetMedium,
    increasingDatasetLarge,
    increasingDatasetHuge,
} from "./data.ts";

/**
 * Performs binary search on a sorted array within given bounds.
 * @returns index of target if found, otherwise -1
 */
function binarySearchInRange(
    arr: number[],
    target: number,
    left: number,
    right: number
): number {
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] === target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

/**
 * Performs exponential search on a sorted array.
 * @returns index of target if found, otherwise -1
 */
function exponentialSearch(arr: number[], target: number): number {
    if (arr.length === 0) return -1;
    if (arr[0] === target) return 0;

    let bound = 1;
    while (bound < arr.length && arr[bound] < target) {
        bound *= 2;
    }

    return binarySearchInRange(
        arr,
        target,
        Math.floor(bound / 2),
        Math.min(bound, arr.length - 1)
    );
}

/**
 * Runs a more reliable benchmark by repeating the search multiple times.
 * This helps reduce noise from JIT warmup / OS scheduling / console overhead.
 */
function benchmarkExponentialSearch(
    name: string,
    dataset: number[],
    target: number,
    runs: number
): void {
    // Warm-up run (helps reduce JIT first-run effects)
    exponentialSearch(dataset, target);

    const label = `Exponential Search ${name} (target=${target}, runs=${runs})`;
    console.time(label);
    let index = -1;
    for (let i = 0; i < runs; i++) {
        index = exponentialSearch(dataset, target);
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
    small: increasingDatasetSmall,
    medium: increasingDatasetMedium,
    large: increasingDatasetLarge,
    huge: increasingDatasetHuge,
};

const runs = 100000;
const targetsLast = {
    small: datasets.small[datasets.small.length - 1],   // last element
    medium: datasets.medium[datasets.medium.length - 1], // last element
    large: datasets.large[datasets.large.length - 1],   // last element
    huge: datasets.huge[datasets.huge.length - 1],   // last element
};

console.log('*'.repeat(50));
console.log('Searching for last elements:');
for (const size of Object.keys(datasets) as (keyof typeof datasets)[]) {
    benchmarkExponentialSearch(
        size,
        datasets[size],
        targetsLast[size],
        runs
    );
}
console.log('*'.repeat(50));


const targetsFirst = {
    small: datasets.small[0],   // first element
    medium: datasets.medium[0], // first element
    large: datasets.large[0],   // first element
    huge: datasets.huge[0],     // first element
};

console.log('Searching for first elements:');
console.log('*'.repeat(50));
for (const size of Object.keys(datasets) as (keyof typeof datasets)[]) {
    benchmarkExponentialSearch(
        size,
        datasets[size],
        targetsFirst[size],
        runs
    );
}
console.log('*'.repeat(50));

const targetsMiddle = {
    small: datasets.small[Math.floor(datasets.small.length / 2)],   // middle element
    medium: datasets.medium[Math.floor(datasets.medium.length / 2)], // middle element
    large: datasets.large[Math.floor(datasets.large.length / 2)],   // middle element
    huge: datasets.huge[Math.floor(datasets.huge.length / 2)],       // middle element
};

console.log('Searching for middle elements:');
console.log('*'.repeat(50));
for (const size of Object.keys(datasets) as (keyof typeof datasets)[]) {
    benchmarkExponentialSearch(
        size,
        datasets[size],
        targetsMiddle[size],
        runs
    );
}
console.log('*'.repeat(50));

// Output timings will vary depending on your computer and runtime.
// The important takeaway is how time grows as dataset size increases (O(log n)).

// Results Example:
/*
**************************************************
Searching for last elements:
**************************************************
Interpolation Search small (target=20, runs=100000): 1.352ms
Dataset size: 20
Target found at index: 19
-
Interpolation Search medium (target=200, runs=100000): 0.786ms
Dataset size: 200
Target found at index: 199
-
Interpolation Search large (target=2000, runs=100000): 0.89ms
Dataset size: 2000
Target found at index: 1999
-
Interpolation Search huge (target=20000, runs=100000): 0.508ms
Dataset size: 20000
Target found at index: 19999
-
**************************************************
Searching for first elements:
**************************************************
Interpolation Search small (target=1, runs=100000): 0.519ms
Dataset size: 20
Target found at index: 0
-
Interpolation Search medium (target=1, runs=100000): 0.518ms
Dataset size: 200
Target found at index: 0
-
Interpolation Search large (target=1, runs=100000): 0.516ms
Dataset size: 2000
Target found at index: 0
-
Interpolation Search huge (target=1, runs=100000): 0.55ms
Dataset size: 20000
Target found at index: 0
-
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
-
ahmedozdogan@Ahmeds-MacBook-Pro finding_algorithms % node exponentialSearch.ts  
ahmedozdogan@Ahmeds-MacBook-Pro finding_algorithms % node exponentialSearch.ts
**************************************************
Searching for last elements:
Exponential Search small (target=20, runs=100000): 3.789ms
Dataset size: 20
Target found at index: 19
-
Exponential Search medium (target=200, runs=100000): 4.627ms
Dataset size: 200
Target found at index: 199
-
Exponential Search large (target=2000, runs=100000): 6.446ms
Dataset size: 2000
Target found at index: 1999
-
Exponential Search huge (target=20000, runs=100000): 8.398ms
Dataset size: 20000
Target found at index: 19999
-
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
-
**************************************************
Searching for middle elements:
**************************************************
Exponential Search small (target=11, runs=100000): 3.016ms
Dataset size: 20
Target found at index: 10
-
Exponential Search medium (target=101, runs=100000): 2.708ms
Dataset size: 200
Target found at index: 100
-
Exponential Search large (target=1001, runs=100000): 3.831ms
Dataset size: 2000
Target found at index: 1000
-
Exponential Search huge (target=10001, runs=100000): 9.115ms
Dataset size: 20000
Target found at index: 10000
-
**************************************************/