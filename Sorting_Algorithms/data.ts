

// Sorting_Algorithms/data.ts
//
// Datasets for practicing sorting algorithms.
//
// We provide 4 sizes:
//   - small
//   - medium
//   - large
//   - huge
//
// And 3 patterns:
//   - random: shuffled permutation of 1..n (every value exists exactly once)
//   - increasing: already sorted ascending 1..n
//   - decreasing: sorted descending n..1
//
// NOTE: Random datasets are deterministic (seeded), so your benchmarks
// are reproducible across runs.

export type DatasetSize = "small" | "medium" | "large" | "huge";
export type DatasetPattern = "random" | "increasing" | "decreasing";

// Feel free to tweak these sizes depending on how fast your computer is.
// huge can be expensive for O(n^2) sorts (Bubble/Selection/Insertion).
export const DATASET_SIZES: Record<DatasetSize, number> = {
    small: 20,
    medium: 200,
    large: 2000,
    huge: 20000,
};

/** Simple deterministic PRNG (Mulberry32) */
function mulberry32(seed: number) {
    let t = seed >>> 0;
    return function next() {
        t += 0x6d2b79f5;
        let r = Math.imul(t ^ (t >>> 15), 1 | t);
        r ^= r + Math.imul(r ^ (r >>> 7), 61 | r);
        return ((r ^ (r >>> 14)) >>> 0) / 4294967296;
    };
}

/** Returns a deterministic shuffled permutation of [1..n]. */
function makeRandomPermutation(n: number, seed: number): number[] {
    const rand = mulberry32(seed);

    // Start with [1..n]
    const arr: number[] = new Array(n);
    for (let i = 0; i < n; i++) arr[i] = i + 1;

    // Fisher–Yates shuffle
    for (let i = n - 1; i > 0; i--) {
        const j = Math.floor(rand() * (i + 1));
        const tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    return arr;
}

/** Returns [1..n] */
function makeIncreasing(n: number): number[] {
    const arr: number[] = new Array(n);
    for (let i = 0; i < n; i++) arr[i] = i + 1;
    return arr;
}

/** Returns [n..1] */
function makeDecreasing(n: number): number[] {
    const arr: number[] = new Array(n);
    for (let i = 0; i < n; i++) arr[i] = n - i;
    return arr;
}

// ----------------------------
// Ready-to-use datasets
// ----------------------------

export const datasetsBySize = {
    small: {
        random: makeRandomPermutation(DATASET_SIZES.small, 1),
        increasing: makeIncreasing(DATASET_SIZES.small),
        decreasing: makeDecreasing(DATASET_SIZES.small),
    },
    medium: {
        random: makeRandomPermutation(DATASET_SIZES.medium, 2),
        increasing: makeIncreasing(DATASET_SIZES.medium),
        decreasing: makeDecreasing(DATASET_SIZES.medium),
    },
    large: {
        random: makeRandomPermutation(DATASET_SIZES.large, 3),
        increasing: makeIncreasing(DATASET_SIZES.large),
        decreasing: makeDecreasing(DATASET_SIZES.large),
    },
    huge: {
        random: makeRandomPermutation(DATASET_SIZES.huge, 4),
        increasing: makeIncreasing(DATASET_SIZES.huge),
        decreasing: makeDecreasing(DATASET_SIZES.huge),
    },
} satisfies Record<DatasetSize, Record<DatasetPattern, number[]>>;

// Convenience exports (similar style to Finding_Algorithms)
export const randomDatasetSmall = datasetsBySize.small.random;
export const increasingDatasetSmall = datasetsBySize.small.increasing;
export const decreasingDatasetSmall = datasetsBySize.small.decreasing;

export const randomDatasetMedium = datasetsBySize.medium.random;
export const increasingDatasetMedium = datasetsBySize.medium.increasing;
export const decreasingDatasetMedium = datasetsBySize.medium.decreasing;

export const randomDatasetLarge = datasetsBySize.large.random;
export const increasingDatasetLarge = datasetsBySize.large.increasing;
export const decreasingDatasetLarge = datasetsBySize.large.decreasing;

export const randomDatasetHuge = datasetsBySize.huge.random;
export const increasingDatasetHuge = datasetsBySize.huge.increasing;
export const decreasingDatasetHuge = datasetsBySize.huge.decreasing;

// Grouped export
export const datasets = datasetsBySize;

/**
 * IMPORTANT for sorting:
 * Sorting algorithms usually mutate arrays.
 * If you want to compare algorithms fairly, always sort a COPY:
 *
 *   const arr = [...randomDatasetMedium];
 *   mySort(arr);
 */