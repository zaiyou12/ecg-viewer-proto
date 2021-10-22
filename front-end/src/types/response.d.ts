declare namespace Resp {
  interface EcgTest {
    region: EcgTest.Region
    testId: EcgTest.TestId
    duration: EcgTest.Duration
    condition: EcgTest.ConditionType
  }

  interface EcgTestResp {
    tests: EcgTest[]
    page: number
    totalPage: number
    testGroup?: string
  }

  interface Group {
    id: number
    groupName: string
  }

  interface GroupListResp {
    status: number
    totalNum: number
    groupList: Group[]
    type: 't' | 's' | 'p'
  }

  interface TestViewResp {
    details: {
      hr: number
      startTime: string
      actualDuration: string
    }
    testGroup: Group[]
    region: EcgTest.Region
    testId: EcgTest.TestId
    duration: EcgTest.Duration
    condition: EcgTest.ConditionType
    totalPage: number
  }

  interface StripsResp {
    imagePath: string[]
    sampleGroup: Group[]
  }
}
