// TODO: Fix after api is modified
export function deserializeGroup(group: Resp.Group) {
  return {
    id: group.id,
    displayName: group.groupName,
    description: undefined,
    numEcgTests: undefined,
    preprocessId: undefined
  }
}

export function deserializeToGroups(groups: Resp.Group[]) {
  const gi: { [id: number]: TestGroup | SampleGroup | PreprocessGroup } = {}
  groups.forEach((g) => {
    const d = deserializeGroup(g)
    gi[d.id] = d
  })
  return gi
}

export function deserializeTest(test: Resp.EcgTest): EcgTest.Meta {
  const { testId, duration, region, condition } = test
  return {
    testId,
    duration,
    region,
    tGroup: [],
    condition: { final: condition }
  }
}

export function deserializeAllTest(tests: Resp.EcgTest[]): EcgTests {
  return tests.map((r) => deserializeTest(r))
}
