export function deserializeGroup(
  type: Resp.GroupType,
  group: Resp.GroupBasic | Resp.GroupDetail
): TestGroup | SampleGroup | PreprocessGroup {
  if ('numTests' in group) {
    const { id, groupName, numTests, groupStatus } = group
    switch (type) {
      case 't':
        return { ...group }
      case 's':
        return { numSamples: numTests, ...group }
      case 'p':
        return { id, groupName }
    }
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
  const { id, seq, region, duration, condition } = test
  return {
    id,
    seq,
    region,
    duration,
    condition: { final: condition }
  }
}

export function deserializeAllTest(tests: Resp.Test[]): EcgTests {
  return tests.map((r) => deserializeTest(r))
}
