declare namespace Req {
  interface EcgTestQuery {
    page?: number
    duration?: EcgTest.Duration | EcgTest.Duration[]
    region?: EcgTest.Region | EcgTest.Region[]
    test_group?: TestGroupId | TestGroupId[]
    condition?: EcgTest.ConditionType | EcgTest.ConditionType[]
    query?: EcgTest.TestId
  }
}
