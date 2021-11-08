declare namespace EcgTest {
  type Duration = 24 | 48 | 72
  type Region = 'AU' | 'UK' | 'KR' | 'SG'
  type Id = number
  type Seq = string
  type ConditionType = 'normal' | 'abnormal' | 'unknown'
  interface Condition {
    final: ConditionType
    perModel?: AiModelCondition[]
  }

  interface Meta {
    id: Id
    seq: Seq
    region: Region
    duration: Duration
    condition: Condition
  }
}

declare type EcgTests = EcgTest.Meta[]
