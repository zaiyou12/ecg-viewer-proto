declare namespace Resp {
  /** */
  interface Test {
    id: EcgTest.Id
    region: EcgTest.Region
    orgCode: EcgTest.OrgCode
    siteName: EcgTest.SiteName
    seq: EcgTest.Seq
    duration: EcgTest.Duration
    condition: EcgTest.ConditionType
  }

  interface TestList {
    tests: Test[]
    page: number
    totalPage: number
    // TODO: Remove?
    testGroup?: string
  }
  /** */

  /** */
  type GroupBasic = {
    id: number
    groupName: string
  }

  interface TestView {
    details: {
      hr: number
      startTime: string
      actualDuration: string
    }
    testGroup: GroupBasic[]
    id: EcgTest.Id
    region: EcgTest.Region
    seq: EcgTest.Seq
    duration: EcgTest.Duration
    condition: EcgTest.ConditionType
    totalPage: number
  }
  /** */

  /** */
  type GroupType = 't' | 's' | 'p'

  type GroupDetail = {
    id: number
    groupName: string
    numTests: number
    groupStatus: GroupStatus
  }

  interface GroupList {
    totalNum: number
    type: GroupType
    groupList: GroupDetail[]
  }
  /** */

  /** */
  interface Strips {
    imagePath: string[]
    sampleGroup: GroupBasic[]
  }
  /** */

  /** */
  type GroupModifyMessage =
    | 'Added'
    | 'Already Added'
    | 'Deleted'
    | 'Already Deleted'

  type GroupChangeResult = {
    target: number | [number, number]
    message: GroupModifyMessage
  }

  type GroupChange = {
    id: number
    result: GroupChangeResult[]
  }
  /** */

  /** */
  interface TestInGroup extends Test {
    pages: number[]
  }

  type TestsInGroup = {
    type: GroupType
    tests: TestInGroup[]
  }
  /** */

  /** */
  type GroupAddDel = {
    message: GroupModifyMessage
    id: number
  }
  /** */
}
