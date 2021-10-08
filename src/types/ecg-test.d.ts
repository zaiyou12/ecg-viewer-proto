declare namespace EcgTest {
  type Duration = 24 | 48 | 72
  type Region = 'AU' | 'UK' | 'KR' | 'N/A'
  type TestSeq = string

  type SampleGroupId = number
  interface SampleGroup {
    readonly id: SampleGroupId
    displayName: string
    description: string
    numEcgTests: number
    testSeqs: TestSeq[]
  }

  type AnomalyGroupId = number
  interface AnomalyGroup {
    readonly id: AnomalyGroupId
    anomalyName: string
    description: string
    numEcgTests: number
    testSeqs: TestSeq[]
  }

  interface Meta {
    testSeq: TestSeq
    duration: Duration
    region: Region
    sampled: SampleGroupId[]
    anomaly: AnomalyGroupId[]
    readonly path?: string
  }
}
