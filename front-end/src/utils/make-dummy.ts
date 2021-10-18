/* Testing purpose */
import { range, getRandomInt, getRandomItem } from './helper'

function getRandomDuration(): EcgTest.Duration {
  const durs = [24, 48, 72]
  return getRandomItem<EcgTest.Duration>(durs as EcgTest.Duration[])
}

function getRandomRegion(): EcgTest.Region {
  const regions = ['AU', 'UK', 'KR', 'N/A']
  return getRandomItem<EcgTest.Region>(regions as EcgTest.Region[])
}

function getRandomGroupIds(n: number): number[] {
  const howMany = getRandomInt(0, n + 1)
  return range(0, howMany)
}

function getRandomStatus() {
  const status = ['normal', 'abnormal', 'unknown']
  return getRandomItem<EcgTest.StatusType>(status as EcgTest.StatusType[])
}

export function makeDummyEcgTests(n: number): EcgTests {
  console.log('Making dummy EcgTests...')
  let tests: EcgTests = []
  for (let i = 1; i < n + 1; i++) {
    const t: EcgTest.Meta = {
      testSeq: `000${i}`,
      startTime: '2021-10-31T00:00:00',
      duration: getRandomDuration(),
      region: getRandomRegion(),
      tGroup: [],  // getRandomGroupIds(4),
      sGroup: [],  // getRandomGroupIds(3),
      status: { final: getRandomStatus() },
      path: '/some/file/path'
    }
    tests.push(t)
  }
  return tests
}

export function makeDummyPreprocessGroups(n: number): PreprocessGroups {
  let groups: PreprocessGroups = {}
  for (let i = 0; i < n; i++) {
    const g = {
      id: i,
      displayName: `PreprocessGroup${i}`,
      description: `This is dummy preprocess group #${i}.`
    }
    groups[i] = g
  }
  return groups
}

export function makeDummyTestGroups(n: number): TestGroups {
  let groups: TestGroups = {}
  for (let i = 0; i < n; i++) {
    const g = {
      id: i,
      displayName: `TestGroup${i}`,
      description: `This is dummy test group #${i}.`,
      numEcgTests: 0,
      testSeqs: []
    }
    groups[i] = g
  }
  return groups
}

export function makeDummySampleGroups(n: number): SampleGroups {
  let groups: SampleGroups = {}
  for (let i = 0; i < n; i++) {
    const g = {
      id: i,
      displayName: `SampleGroup${i}`,
      description: `This is dummy sample group #${i}.`,
      numStrips: 0,
      strips: []
    }
    groups[i] = g
  }
  return groups
}

