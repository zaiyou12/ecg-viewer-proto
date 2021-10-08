/**
 * Converts vue-router route param to a number
 *
 * @param param Should be a string rep of a number
 * @returns A param value as number
 */
export function paramToInt(param: string | string[]): number {
  if (typeof param === 'string') {
    return +param
  } else {
    return +param[0]
  }
}

/**
 * Attempt to mimic Python's range function
 *
 * @param start Inclusive start number
 * @param end Exclusive end number
 * @returns Number array of [start ... end)
 */
export function range(start = 0, end: number): Array<number> {
  const size = end - start
  return [...Array(size).keys()].map(i => i + start)
}

/**
 * Random integer selector
 *
 * @param min Inclusive minimum
 * @param max Exclusive minimum
 * @returns Random int between [min, max)
 */
export function getRandomInt(min: number, max: number): number {
  return Math.floor(Math.random() * (max - min) + min)
}

/**
 * Random item selector
 *
 * @param arr Array<T> to select from
 * @returns An item of type T
 */
export function getRandomItem<T>(arr: Array<T>): T {
  const randIdx = Math.floor(Math.random() * arr.length)
  return arr[randIdx]
}
