/**
 * Converts vue-router route param to a number
 *
 * @param param Should be a string rep of a number
 * @returns A param value as number
 */
export function paramToInt(param: string | string[]): number {
  if (typeof param === 'string') {
    return Math.abs(+param)
  } else {
    return Math.abs(+param[0])
  }
}

/**
 * Converts vue-router route param to a string
 *
 * @param param Should be a string
 * @returns A param value as string
 */
export function paramToString(param: string | string[]): string {
  if (typeof param === 'string') {
    return param
  } else {
    return param[0]
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
  return [...Array(size).keys()].map((i) => i + start)
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

/**
 * Returns new array after removing given item
 * @param arr Array of string or number
 * @param item Item to remove
 */
export function removeFromArray<T extends string | number>(
  arr: Array<T>,
  item: T
) {
  const idx = arr.indexOf(item)
  if (idx > -1) {
    arr.splice(idx, 1)
  }
}

export function hasTypedProperty<X extends {}, Y extends PropertyKey>(
  obj: X,
  prop: Y
): obj is X & Record<Y, unknown> {
  return obj.hasOwnProperty(prop)
}
