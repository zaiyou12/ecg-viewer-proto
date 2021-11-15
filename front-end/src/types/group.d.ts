declare interface GroupBasic {
  id: number
  groupName: string
}

declare type GroupStatus = 'open' | 'closed'

declare interface GroupDetail extends GroupBasic {
  groupStatus?: GroupStatus
}

declare interface PreprocessGroup extends GroupBasic {}
declare interface PreprocessGroups {
  [id: number]: PreprocessGroup
}

declare interface TestGroup extends GroupDetail {
  /** Must be left as optional; will break deserializeToGroups and test-view */
  numTests?: number
  pid?: number
}
declare interface TestGroups {
  [id: number]: TestGroup
}

declare interface SampleGroup extends GroupDetail {
  /** Must be left as optional; will break deserializeToGroups and test-view */
  numSamples?: number
  pid?: number
}
declare interface SampleGroups {
  [id: number]: SampleGroup
}

// TODO: Remove or modify later
declare type AnomalyGroupId = number
declare interface AnomalyGroup {
  id: AnomalyGroupId
  anomalyName: string
  description: string
  numEcgTests: number
}
declare interface AnomalyGroups {
  [id: AnomalyGroupId]: AnomalyGroup
}
