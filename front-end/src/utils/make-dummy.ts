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

export function makeDummySampleGroup(n: number): SampleGroup {
  let groups: SampleGroup = {}
  for (let i = 0; i < n; i++) {
    const g = {
      displayName: `SampleGroup${i}`,
      description: `This is dummy sample group #${i}.`,
      numStrips: 0,
      strips: []
    }
    groups[i] = g
  }
  return groups
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
      tGroup: getRandomGroupIds(3),
      sGroup: getRandomGroupIds(4),
      status: { final: getRandomStatus() },
      path: './'
    }
    tests.push(t)
  }
  return tests
}
