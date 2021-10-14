declare type PreprocessGroupId = number
declare interface PreprocessGroup {
  [id: PreprocessGroupId]: {
    displayName: string
    description?: string
  }
}

declare type TestGroupId = number
declare interface TestGroup {
  [id: TestGroupId]: {
    displayName: string
    description?: string
    numEcgTests: number
    testSeqs: EcgTest.TestSeq[]
    preprocessId?: PreprocessGroupId
  }
}

declare type SampleGroupId = number
declare interface SampleGroup {
  [id: SampleGroupId]: {
    displayName: string
    description?: string
    numStrips: number
    strips: EcgStrip[]
    preprocessId?: PreprocessGroupId
  }
}

declare type AnomalyGroupId = number
declare interface AnomalyGroup {
  [id: AnomalyGroupId]: {
    anomalyName: string
    description: string
    numEcgTests: number
    testSeqs: EcgTest.TestSeq[]
  }
}
