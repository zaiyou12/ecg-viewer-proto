declare type PreprocessGroupId = number
declare interface PreprocessGroup {
  id: PreprocessGroupId
  displayName: string
  description?: string
}
declare interface PreprocessGroups {
  [id: PreprocessGroupId]: PreprocessGroup
}

declare type TestGroupId = number
declare interface TestGroup {
  id: TestGroupId
  displayName: string
  description?: string
  numEcgTests: number
  testSeqs: EcgTest.TestSeq[]
  preprocessId?: PreprocessGroupId
}
declare interface TestGroups {
  [id: TestGroupId]: TestGroup
}

declare type SampleGroupId = number
declare interface SampleGroup {
  id: SampleGroupId
  displayName: string
  description?: string
  numStrips: number
  strips: EcgStrip[]
  preprocessId?: PreprocessGroupId
}
declare interface SampleGroups {
  [id: SampleGroupId]: SampleGroup
}

declare type AnomalyGroupId = number
declare interface AnomalyGroup {
  id: AnomalyGroupId
  anomalyName: string
  description: string
  numEcgTests: number
  testSeqs: EcgTest.TestSeq[]
}
declare interface AnomalyGroups {
  [id: AnomalyGroupId]: AnomalyGroup
}
