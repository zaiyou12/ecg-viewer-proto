function isTestGroupWork(
  work: EcgTest.Id | [EcgTest.Id, number]
): work is EcgTest.Id {
  return typeof work === 'number'
}

function isSampleGroupWork(
  work: EcgTest.Id | [EcgTest.Id, number]
): work is [EcgTest.Id, number] {
  return typeof work !== 'number'
}

export function resultTransacted(
  result: Resp.GroupChangeResult,
  type: Resp.GroupType,
  toggle: boolean,
  work: EcgTest.Id | [EcgTest.Id, number],
  page?: number
) {
  if (
    (toggle && result.message === 'Added') ||
    (!toggle && result.message === 'Deleted')
  ) {
    if (
      (type === 't' &&
        isTestGroupWork(result.target) &&
        result.target === work) ||
      (type === 's' &&
        isSampleGroupWork(result.target) &&
        isSampleGroupWork(work) &&
        result.target[0] === work[0] &&
        result.target[1] === work[1])
    ) {
      return true
    }
  }
  return false
}
