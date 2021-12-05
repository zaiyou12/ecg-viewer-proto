declare namespace EcgTest {
  type Duration = 2 | 24 | 48 | 72
  type Region = 'AU' | 'UK' | 'KR' | 'SG'
  type Id = number
  type OrgCode = string
  type SiteName = string
  type Seq = string
  type ConditionType = 'normal' | 'abnormal' | 'unknown'
  interface Condition {
    final: ConditionType
    perModel?: AiModelCondition[]
  }

  interface Meta {
    id: Id
    region: Region
    orgCode: OrgCode
    siteName: SiteName
    seq: Seq
    duration: Duration
    condition: Condition
  }
}

declare type EcgTests = EcgTest.Meta[]
