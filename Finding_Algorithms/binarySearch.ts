// Finding_Algorithms/linearSearch.ts

// binary Search (Divide and Conquer)
//
// - Works only on SORTED arrays
// - Repeatedly divides search interval in half
//
// Time Complexity:
//   Best:    O(1)   (target is at middle index)
//   Average: O(log n)
//   Worst:   O(log n)   (target is at one of the ends or not present)

// Space Complexity: O(1) for iterative, O(log n) for recursive implementation
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
 * Performs binary search on a sorted array.
 * @returns index of target if found, otherwise -1
 */
function binarySearch(arr: number[], target: number): number {
    let left = 0;
    let right = arr.length - 1;

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
 * Runs a more reliable benchmark by repeating the search multiple times.
 * This helps reduce noise from JIT warmup / OS scheduling / console overhead.
 */
function benchmarkBinarySearch(
    name: string,
    dataset: number[],
    target: number,
    runs: number
): void {
    // Warm-up run (helps reduce JIT first-run effects)
    binarySearch(dataset, target);

    const label = `Binary Search ${name} (target=${target}, runs=${runs})`;
    console.time(label);
    let index = -1;
    for (let i = 0; i < runs; i++) {
        index = binarySearch(dataset, target);
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

//find last element in each dataset

const runs = 100000;
const targetsLast = {
    small: datasets.small[datasets.small.length - 1],   // last element
    medium: datasets.medium[Math.floor(datasets.medium.length - 1)], // last element
    large: datasets.large[datasets.large.length - 1],   // last element
    huge: datasets.huge[datasets.huge.length - 1],   // last element
};
console.log('*'.repeat(50));
console.log('Searching for last elements:');
console.log('*'.repeat(50));

for (const size of Object.keys(datasets) as Array<keyof typeof datasets>) {
    benchmarkBinarySearch(
        size,
        datasets[size],
        targetsLast[size],
        runs
    );
}

//find first element in each dataset
console.log('*'.repeat(50));
console.log('Searching for first elements:');
console.log('*'.repeat(50));

const targetsFirst = {
    small: datasets.small[0],   // first element
    medium: datasets.medium[0], // first element
    large: datasets.large[0],   // first element
    huge: datasets.huge[0],     // first element
};

for (const size of Object.keys(datasets) as Array<keyof typeof datasets>) {
    benchmarkBinarySearch(
        size,
        datasets[size],
        targetsFirst[size],
        runs
    );
}

//find middle element in each dataset
console.log('*'.repeat(50));
console.log('Searching for middle elements:');
console.log('*'.repeat(50));

const targetsMiddle = {
    small: datasets.small[Math.floor(datasets.small.length / 2)],   // middle element
    medium: datasets.medium[Math.floor(datasets.medium.length / 2)], // middle element
    large: datasets.large[Math.floor(datasets.large.length / 2)],   // middle element
    huge: datasets.huge[Math.floor(datasets.huge.length / 2)],       // middle element
};

for (const size of Object.keys(datasets) as Array<keyof typeof datasets>) {
    benchmarkBinarySearch(
        size,
        datasets[size],
        targetsMiddle[size],
        runs
    );
}

// Output timings will vary depending on your computer and runtime.
// The important takeaway is how time grows as dataset size increases (O(log n)).


//Results Example:
/*==================================================
**************************************************
Searching for first elements:
**************************************************
Binary Search small (target=1, runs=100000): 0.952ms
Dataset size: 20
Target found at index: 0
-
Binary Search medium (target=1, runs=100000): 2.001ms
Dataset size: 200
Target found at index: 0
-
Binary Search large (target=1, runs=100000): 3.497ms
Dataset size: 2000
Target found at index: 0
-
Binary Search huge (target=1, runs=100000): 5.263ms
Dataset size: 20000
Target found at index: 0
-
**************************************************
Searching for middle elements:
**************************************************
Binary Search small (target=11, runs=100000): 1.458ms
Dataset size: 20
Target found at index: 10
-
Binary Search medium (target=101, runs=100000): 2.126ms
Dataset size: 200
Target found at index: 100
-
Binary Search large (target=1001, runs=100000): 3.563ms
Dataset size: 2000
Target found at index: 1000
-
Binary Search huge (target=10001, runs=100000): 5.667ms
Dataset size: 20000
Target found at index: 10000*/