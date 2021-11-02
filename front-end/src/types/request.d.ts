declare namespace Req {
  interface EcgTestQuery {
    page?: number
    duration?: EcgTest.Duration | EcgTest.Duration[]
    region?: EcgTest.Region | EcgTest.Region[]
    test_group?: number | number[] // Test Group ID
    condition?: EcgTest.ConditionType | EcgTest.ConditionType[]
    query?: EcgTest.Seq
  }
}
