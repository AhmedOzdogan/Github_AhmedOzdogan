// Finding_Algorithms/jumpSeach.ts

// Jump Search
//
// - Works only on SORTED arrays
// - Divides the array into blocks of fixed size and performs linear search within the block
//
// Time Complexity:
//   Best:    O(√n)   (target is at the beginning of a block)
//   Average: O(√n)
//   Worst:   O(√n)   (target is at the end or not present)
//
// Space Complexity: O(1)
//
// NOTE:
// For SMALL or UNSORTED datasets, consider Linear Search (O(n)).
// For LARGE + SORTED datasets, consider Binary Search (O(log n)).

import {
    increasingDatasetSmall,
    increasingDatasetMedium,
    increasingDatasetLarge,
    increasingDatasetHuge,
} from "./data.ts";

/**
 * Performs jump search on a sorted array.
 * @returns index of target if found, otherwise -1
 */
function jumpSearch(arr: number[], target: number): number {
    const n = arr.length;
    const step = Math.floor(Math.sqrt(n));
    let prev = 0;
    let curr = step;

    // Finding the block where the target may be present
    while (arr[Math.min(curr, n) - 1] < target) {
        prev = curr;
        curr += step;
        if (prev >= n) return -1;
    }

    // Linear search within the identified block [prev, curr)
    for (let i = prev; i < Math.min(curr, n); i++) {
        if (arr[i] === target) return i;
    }

    return -1;
}

/**
 * Runs a more reliable benchmark by repeating the search multiple times.
 * This helps reduce noise from JIT warmup / OS scheduling / console overhead.
 */
function benchmarkJumpSearch(
    name: string,
    dataset: number[],
    target: number,
    runs: number
): void {
    // Warm-up run (helps reduce JIT first-run effects)
    jumpSearch(dataset, target);

    const label = `Jump Search ${name} (target=${target}, runs=${runs})`;
    console.time(label);
    let index = -1;
    for (let i = 0; i < runs; i++) {
        index = jumpSearch(dataset, target);
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



const runs = 100;

console.log('*'.repeat(50));
console.log('Searching for last elements:');
console.log('*'.repeat(50));

//find last element in each dataset
const targetsLast = {
    small: datasets.small[datasets.small.length - 1],   // last element
    medium: datasets.medium[datasets.medium.length - 1], // last element
    large: datasets.large[datasets.large.length - 1],   // last element
    huge: datasets.huge[datasets.huge.length - 1],       // last element
};

for (const size of ["small", "medium", "large", "huge"] as const) {
    benchmarkJumpSearch(
        size,
        datasets[size],
        targetsLast[size],
        runs
    );
}

console.log('*'.repeat(50));
console.log('Searching for middle elements:');
console.log('*'.repeat(50));

//find middle element in each dataset
const targetsMiddle = {
    small: datasets.small[Math.floor(datasets.small.length / 2)],   // middle element
    medium: datasets.medium[Math.floor(datasets.medium.length / 2)], // middle element
    large: datasets.large[Math.floor(datasets.large.length / 2)],   // middle element
    huge: datasets.huge[Math.floor(datasets.huge.length / 2)],       // middle element
};

for (const size of ["small", "medium", "large", "huge"] as const) {
    benchmarkJumpSearch(
        size,
        datasets[size],
        targetsMiddle[size],
        runs
    );
}

console.log('*'.repeat(50));
console.log('Searching for first elements:');
console.log('*'.repeat(50));

//finding the first element in each dataset
const targetsFirst = {
    small: datasets.small[0],   // first element
    medium: datasets.medium[0], // first element
    large: datasets.large[0],   // first element
    huge: datasets.huge[0],     // first element
};

// Benchmarking jump search for first elements
for (const size of ["small", "medium", "large", "huge"] as const) {
    benchmarkJumpSearch(
        size,
        datasets[size],
        targetsFirst[size],
        runs
    );
}

//Output timings will vary depending on your computer and runtime.
// The important takeaway is how time grows as dataset size increases (O(√n)).

// Results Example:
/*
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
-
**************************************************
Searching for middle elements:
**************************************************
Jump Search small (target=11, runs=100): 0.007ms
Dataset size: 20
Target found at index: 10
-
Jump Search medium (target=101, runs=100): 0.012ms
Dataset size: 200
Target found at index: 100
-
Jump Search large (target=1001, runs=100): 0.04ms
Dataset size: 2000
Target found at index: 1000
-
Jump Search huge (target=10001, runs=100): 0.129ms
Dataset size: 20000
Target found at index: 10000
-
**************************************************
Searching for first elements:
**************************************************
Jump Search small (target=1, runs=100): 0.004ms
Dataset size: 20
Target found at index: 0
-
Jump Search medium (target=1, runs=100): 0.004ms
Dataset size: 200
Target found at index: 0
-
Jump Search large (target=1, runs=100): 0.003ms
Dataset size: 2000
Target found at index: 0
-
Jump Search huge (target=1, runs=100): 0.003ms
Dataset size: 20000
Target found at index: 0

-*/