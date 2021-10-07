export function paramToInt(param: string | string[]): number {
  if (typeof param === 'string') {
    return +param
  } else {
    return +param[0]
  }
}

export function range(start = 0, end: number): ReadonlyArray<number> {
  const size = end - start
  return [...Array(size).keys()].map(i => i + start)
}
