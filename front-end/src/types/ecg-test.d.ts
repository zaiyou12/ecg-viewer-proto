declare namespace EcgTest {
  type Duration = 24 | 48 | 72
  type Region = 'AU' | 'UK' | 'KR' | 'SG'
  type TestId = string
  type ConditionType = 'normal' | 'abnormal' | 'unknown'
  interface Condition {
    final: ConditionType
    perModel?: AiModelCondition[]
  }

  interface Meta {
    testId: TestId
    duration: Duration
    region: Region
    tGroup: TestGroupId[]
    condition: Condition
  }
}

declare type EcgTests = EcgTest.Meta[]

declare interface EcgStrip {
  len: 60 | 10 // seconds
  testSeq: EcgTest.TestId
  start: number // seconds
  data?: string
}
