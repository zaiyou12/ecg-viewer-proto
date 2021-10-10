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

export function makeDummySampleGroups(n: number): EcgTest.SampleGroup[] {
  let groups: EcgTest.SampleGroup[] = []
  for (let i = 0; i < n; i++) {
    const g: EcgTest.SampleGroup = {
      id: i,
      displayName: `Group${i}`,
      description: `This is dummy sample group #${i}.`,
      numEcgTests: 0,
      testSeqs: []
    }
    groups.push(g)
  }
  return groups
}

export function makeDummyAnomalyGroups(n: number): EcgTest.AnomalyGroup[] {
  let groups: EcgTest.AnomalyGroup[] = []
  for (let i = 0; i < n; i++) {
    const g: EcgTest.AnomalyGroup = {
      id: i,
      anomalyName: `Anomaly${i}`,
      description: `This is dummy anomaly group #${i}.`,
      numEcgTests: 0,
      testSeqs: []
    }
    groups.push(g)
  }
  return groups
}

function getRandomGroupIds(n: number): number[] {
  const howMany = getRandomInt(0, n + 1)
  return range(0, howMany)
}

export function makeDummyEcgTests(n: number): EcgTest.Meta[] {
  console.log('Making dummy EcgTests...')
  let tests: EcgTest.Meta[] = []
  for (let i = 1; i < n + 1; i++) {
    const t: EcgTest.Meta = {
      testSeq: `000${i}`,
      duration: getRandomDuration(),
      region: getRandomRegion(),
      sampled: getRandomGroupIds(3),
      anomaly: getRandomGroupIds(2),
      path: './'
    }
    tests.push(t)
  }
  return tests
}
