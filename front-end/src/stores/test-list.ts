import { defineStore } from 'pinia'
import EcgTestApi from '../utils/test-list-api'
import { removeFromArray } from '../utils/helper'

type TestListState = {
  tests: EcgTests
  totalPage: number
  page: number
  duration: EcgTest.Duration[]
  region: EcgTest.Region[]
  testGroup?: number // Test Group ID
  condition: EcgTest.ConditionType[]
  query: EcgTest.Seq
  loading: boolean
}

const api = new EcgTestApi()

const useTestsStore = defineStore('ecgTests', {
  state: () => {
    return {
      tests: [],
      page: 1,
      totalPage: 1,
      duration: [],
      region: [],
      testGroup: undefined,
      condition: [],
      query: '',
      loading: false
    } as TestListState
  },
  actions: {
    /**
     * Fetches the list of tests for specified page and filters
     */
    async getTestList(): Promise<void> {
      this.loading = true
      const params: Req.EcgTestQuery = {
        page: this.page,
        duration: this.duration.length > 0 ? this.duration : undefined,
        region: this.region.length > 0 ? this.region : undefined,
        test_group: this.testGroup,
        condition: this.condition.length > 0 ? this.condition : undefined,
        query: this.query.length > 0 ? this.query : undefined
      }
      const res = await api.fetchTestList(params)
      if (res === undefined) return
      ;({
        tests: this.tests,
        page: this.page,
        totalPage: this.totalPage
        // TODO: testGroup: ???
      } = res)
      this.loading = false
    },

    resetFilters() {
      this.duration = []
      this.region = []
      this.testGroup = undefined
      this.condition = []
    },

    resetAllParams() {
      this.page = 1
      this.resetFilters()
      this.query = ''
    },

    toggleDuration(dur: EcgTest.Duration) {
      if (this.duration.includes(dur)) {
        removeFromArray(this.duration, dur)
      } else {
        this.duration.push(dur)
      }
    },

    toggleRegion(reg: EcgTest.Region) {
      if (this.region.includes(reg)) {
        removeFromArray(this.region, reg)
      } else {
        this.region.push(reg)
      }
    },

    toggleCondition(cond: EcgTest.ConditionType) {
      if (this.condition.includes(cond)) {
        removeFromArray(this.condition, cond)
      } else {
        this.condition.push(cond)
      }
    }
  }
})

export default useTestsStore
