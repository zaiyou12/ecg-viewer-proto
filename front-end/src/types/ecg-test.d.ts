declare namespace EcgTest {
  type Duration = 24 | 48 | 72
  type Region = 'AU' | 'UK' | 'KR' | 'N/A'
  type TestSeq = string
  type StatusType = 'normal' | 'abnormal' | 'unknown'
  interface Status {
    final: StatusType
    statPerModel?: AiModelStatus[]
  }

  interface Meta {
    testSeq: TestSeq
    startTime: string
    duration: Duration
    region: Region
    tGroup: TestGroupId[]
    sGroup: SampleGroupId[]
    status: Status
    readonly path?: string
  }
}

declare type EcgTests = EcgTest.Meta[]

declare interface EcgStrip {
  len: 60 | 10  // seconds
  testSeq: EcgTest.TestSeq
  start: number  // seconds
  data?: string
}
