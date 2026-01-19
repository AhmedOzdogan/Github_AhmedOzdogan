// Finding_Algorithms/interpolationSearch.ts

// Interpolation Search
//
// - Works only on SORTED and UNIFORMLY DISTRIBUTED arrays
// - Estimates the position of the target based on its value relative to the bounds
//
// Time Complexity:
//   Best:    O(1)   (target is at estimated position)
//   Average: O(log log n)   (for uniformly distributed data)
//   Worst:   O(n)   (for non-uniformly distributed data)
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
 * Performs interpolation search on a sorted array.
 * @returns index of target if found, otherwise -1
 */
function interpolationSearch(arr: number[], target: number): number {
    let low = 0;
    let high = arr.length - 1;

    while (low <= high && target >= arr[low] && target <= arr[high]) {
        if (low === high) {
            if (arr[low] === target) return low;
            return -1;
        }

        // Estimate the position using the interpolation formula
        const pos =
            low +
            Math.floor(
                ((target - arr[low]) * (high - low)) / (arr[high] - arr[low])
            );

        if (arr[pos] === target) {
            return pos;
        } else if (arr[pos] < target) {
            low = pos + 1;
        } else {
            high = pos - 1;
        }
    }

    return -1;
}

/**
 * Runs a more reliable benchmark by repeating the search multiple times.
 * This helps reduce noise from JIT warmup / OS scheduling / console overhead.
 */
function benchmarkInterpolationSearch(
    name: string,
    dataset: number[],
    target: number,
    runs: number
): void {
    // Warm-up run (helps reduce JIT first-run effects)
    interpolationSearch(dataset, target);

    const label = `Interpolation Search ${name} (target=${target}, runs=${runs})`;
    console.time(label);
    let index = -1;
    for (let i = 0; i < runs; i++) {
        index = interpolationSearch(dataset, target);
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
console.log('*'.repeat(50));

for (const size of ["small", "medium", "large", "huge"] as const) {
    benchmarkInterpolationSearch(
        size,
        datasets[size],
        targetsLast[size],
        runs
    );
}

const targetsFirst = {
    small: datasets.small[0],   // first element
    medium: datasets.medium[0], // first element
    large: datasets.large[0],   // first element
    huge: datasets.huge[0],     // first element
};

console.log('*'.repeat(50));
console.log('Searching for first elements:');
console.log('*'.repeat(50));

for (const size of ["small", "medium", "large", "huge"] as const) {
    benchmarkInterpolationSearch(
        size,
        datasets[size],
        targetsFirst[size],
        runs
    );
}

const targetsMiddle = {
    small: datasets.small[Math.floor(datasets.small.length / 2)],   // middle element
    medium: datasets.medium[Math.floor(datasets.medium.length / 2)], // middle element
    large: datasets.large[Math.floor(datasets.large.length / 2)],   // middle element
    huge: datasets.huge[Math.floor(datasets.huge.length / 2)],       // middle element
};

console.log('*'.repeat(50));
console.log('Searching for middle elements:');
console.log('*'.repeat(50));

for (const size of ["small", "medium", "large", "huge"] as const) {
    benchmarkInterpolationSearch(
        size,
        datasets[size],
        targetsMiddle[size],
        runs
    );
}

// Output timings will vary depending on your computer and runtime.
// The important takeaway is how time grows as dataset size increases (O(log log n) on average).


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
Target found at index: 10000 */