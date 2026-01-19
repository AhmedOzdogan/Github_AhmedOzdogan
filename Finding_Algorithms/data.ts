// Datasets for practicing finding / searching algorithms.
//
// We provide 4 sizes:
//   - small
//   - medium
//   - large
//   - huge
//
// And 3 orderings:
//   - random (unsorted)
//   - increasing (sorted ascending)
//   - decreasing (sorted descending)
//
// NOTE: random datasets are generated deterministically using a seeded PRNG
// so results are reproducible across runs.

export type DatasetSize = "small" | "medium" | "large" | "huge";
export type DatasetOrder = "random" | "increasing" | "decreasing";

// Feel free to tweak these sizes
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

/**
 * Returns a deterministic shuffled permutation of [1..n].
 * This guarantees every number exists exactly once, which is ideal
 * for practicing finding/searching algorithms.
 */
function makeRandomDataset(n: number, seed: number): number[] {
    const rand = mulberry32(seed);

    // Start with [1..n]
    const arr: number[] = new Array(n);
    for (let i = 0; i < n; i++) arr[i] = i + 1;

    // Fisher–Yates shuffle using deterministic PRNG
    for (let i = n - 1; i > 0; i--) {
        const j = Math.floor(rand() * (i + 1));
        const tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    return arr;
}

/** Returns [1..n] */
function makeIncreasingDataset(n: number): number[] {
    const arr: number[] = new Array(n);
    for (let i = 0; i < n; i++) arr[i] = i + 1;
    return arr;
}

/** Returns [n..1] */
function makeDecreasingDataset(n: number): number[] {
    const arr: number[] = new Array(n);
    for (let i = 0; i < n; i++) arr[i] = n - i;
    return arr;
}

// ----------------------------
// Ready-to-use datasets
// ----------------------------

export const datasetsBySize = {
    small: {
        random: makeRandomDataset(DATASET_SIZES.small, 1),
        increasing: makeIncreasingDataset(DATASET_SIZES.small),
        decreasing: makeDecreasingDataset(DATASET_SIZES.small),
    },
    medium: {
        random: makeRandomDataset(DATASET_SIZES.medium, 2),
        increasing: makeIncreasingDataset(DATASET_SIZES.medium),
        decreasing: makeDecreasingDataset(DATASET_SIZES.medium),
    },
    large: {
        random: makeRandomDataset(DATASET_SIZES.large, 3),
        increasing: makeIncreasingDataset(DATASET_SIZES.large),
        decreasing: makeDecreasingDataset(DATASET_SIZES.large),
    },
    huge: {
        random: makeRandomDataset(DATASET_SIZES.huge, 4),
        increasing: makeIncreasingDataset(DATASET_SIZES.huge),
        decreasing: makeDecreasingDataset(DATASET_SIZES.huge),
    },
} satisfies Record<DatasetSize, Record<DatasetOrder, number[]>>;

// Backwards-compatible / convenience exports
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

// Original-style grouped export (now includes sizes)
export const datasets = datasetsBySize;