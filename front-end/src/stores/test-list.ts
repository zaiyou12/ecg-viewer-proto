import { defineStore } from 'pinia'
import EcgTestApi from '../utils/ecg-test-api'

type TestListState = {
  tests: EcgTests
  totalPages: number
  page: number
  duration?: EcgTest.Duration
  region?: EcgTest.Region
  testGroup?: TestGroupId
  condition?: EcgTest.ConditionType
  query?: EcgTest.TestId
  loading: boolean
}

const api = new EcgTestApi()

const useTestsStore = defineStore('ecgTests', {
  state: () => {
    return {
      tests: [],
      page: 1,
      totalPages: 1,
      loading: false
    } as TestListState
  },
  actions: {
    /**
     * Fetches the list of tests for specified page and filters
     */
    async fetchEcgTests(): Promise<void> {
      this.loading = true
      const params: Req.EcgTestQuery = {
        page: this.page,
        duration: this.duration,
        region: this.region,
        test_group: this.testGroup,
        condition: this.condition,
        query: this.query
      }
      const res = await api.getEcgTests(params)
      if (res === undefined) return
      ;({
        tests: this.tests,
        page: this.page,
        totalPages: this.totalPages
        // TODO: testGroup: ???
      } = res)
      this.loading = false
    }
  }
})

export default useTestsStore
