export function deserializeGroup(
  type: Resp.GroupType,
  group: Resp.GroupBasic | Resp.GroupDetail
): TestGroup | SampleGroup | PreprocessGroup {
  if ('numTests' in group) {
    const { id, groupName, numTests } = group
    if (type === 't') return { ...group }
    else if (type === 's') return { numSamples: numTests, ...group }
    else return { id, groupName }
  } else {
    return group
  }
}

export function deserializeToGroups(
  type: Resp.GroupType,
  groups: Resp.GroupBasic[] | Resp.GroupDetail[]
): TestGroups | SampleGroups | PreprocessGroups {
  const gi: { [id: number]: TestGroup | SampleGroup | PreprocessGroup } = {}
  groups.forEach((g) => {
    const d = deserializeGroup(type, g)
    gi[d.id] = d
  })
  return gi
}

/**
 * @returns Order of the return affects TestListItem column order.
 * If modified, the table headers in TestList should also be modified.
 * @see /components/TestList/index.vue
 */
export function deserializeTest(test: Resp.Test): EcgTest.Meta {
  const { id, region, orgCode, siteName, seq, duration, condition } = test
  return {
    id,
    region,
    orgCode,
    siteName,
    seq,
    duration,
    condition: { final: condition }
  }
}

export function deserializeAllTest(tests: Resp.Test[]): EcgTests {
  return tests.map((r) => deserializeTest(r))
}

export function deserializeTestInGroup(
  type: Resp.GroupType,
  testInGroup: Resp.TestInGroup
): EcgTest.Meta | [EcgTest.Meta, number[]] {
  const { pages, ...test } = testInGroup
  if (type === 't') {
    return deserializeTest(test)
  }
  return [deserializeTest(test), pages]
}

export function deserializeAllTestsInGroup(
  type: Resp.GroupType,
  testsInGroup: Resp.TestInGroup[]
) {
  return testsInGroup.map((r) => deserializeTestInGroup(type, r))
}
