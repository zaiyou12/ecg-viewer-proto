declare namespace Resp {
  interface EcgTest {
    region: EcgTest.Region
    test_id: EcgTest.TestId
    duration: EcgTest.Duration
    condition: EcgTest.ConditionType
  }

  interface EcgTestResp {
    tests: EcgTest[]
    page: number
    total_page: number
    test_group?: string
  }

  interface GroupList {
    id: number
    group_name: string
  }

  interface GroupListResp {
    status: number
    total_num: number
    group_list: GroupList[]
    type: 't' | 's' | 'p'
  }
}
