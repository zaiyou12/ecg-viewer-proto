import { defineStore } from 'pinia'
import TestViewApi from '../utils/test-view-api'

const api = new TestViewApi()

type EcgTestDetails = {
  hr: number
  startTime: string
  actualDuration: string
}

type TestViewState = {
  selectedTest?: EcgTest.Meta
  details?: EcgTestDetails
  testGroup?: TestGroups
  totalPage: number
  page: number
  stripUrl?: string[]
  sampleGroup?: SampleGroups
  pid?: PreprocessGroupId
  loading: boolean
}

const useTestViewStore = defineStore('testView', {
  state: () => {
    return {
      selectedTest: undefined,
      details: undefined,
      testGroup: undefined,
      totalPage: 1,
      page: 1,
      stripUrl: undefined,
      sampleGroup: undefined,
      pid: undefined,
      loading: false
    } as TestViewState
  },
  actions: {
    resetState(): void {
      this.selectedTest = undefined
      this.details = undefined
      this.testGroup = undefined
      this.totalPage = 1
      this.page = 1
      this.stripUrl = undefined
      this.sampleGroup = undefined
      this.pid = undefined
      this.loading = false
    },

    async viewNewTest(region: EcgTest.Region, testId: EcgTest.TestId) {
      this.resetState()
      this.loading = true
      const res = await api.fetchTestView(region, testId)
      if (res === undefined) {
        this.loading = false
        return
      }
      ;({
        selectedTest: this.selectedTest,
        details: this.details,
        testGroup: this.testGroup,
        totalPage: this.totalPage
      } = res)
      await this.getStrips()
      this.loading = false
    },

    async addToTestGroup(id: TestGroupId, displayName: string) {
      this.loading = true
      const res = await api.postTestGroupToggle(
        this.selectedTest!.region,
        this.selectedTest!.testId,
        id,
        true
      )
      // TODO: Think more about this later
      // If res is true, then it means it was successfully registered to server
      if (res) this.testGroup![id] = { id, displayName }
      this.loading = false
    },

    async delFromTestGroup(id: TestGroupId) {
      this.loading = true
      const res = await api.postTestGroupToggle(
        this.selectedTest!.region,
        this.selectedTest!.testId,
        id,
        false
      )
      // TODO: Think more about this later
      // If res is true, then it means it was successfully registered to server
      if (res) delete this.testGroup![id]
      this.loading = false
    },

    async getStrips() {
      this.loading = true
      const res = await api.fetchStrips(
        this.selectedTest!.region,
        this.selectedTest!.testId,
        this.page,
        this.pid
      )
      if (res === undefined) {
        this.loading = false
        return
      }
      ;({ stripUrl: this.stripUrl, sampleGroup: this.sampleGroup } = res)
      this.loading = false
    },

    async getPrevStrips() {
      if (this.page <= 1) return
      this.loading = true
      this.page--
      await this.getStrips()
      this.loading = false
    },

    async getNextStrip() {
      if (this.page >= this.totalPage) return
      this.loading = true
      this.page++
      await this.getStrips()
      this.loading = false
    },

    async addToSampleGroup(id: SampleGroupId, displayName: string) {
      this.loading = true
      const res = await api.postSampleGroupToggle(
        this.selectedTest!.region,
        this.selectedTest!.testId,
        this.page,
        id,
        true
      )
      // TODO: Think more about this later
      // If res is true, then it means it was successfully registered to server
      if (res) this.sampleGroup![id] = { id, displayName }
      this.loading = false
    },

    async delFromSampleGroup(id: SampleGroupId) {
      this.loading = true
      const res = await api.postSampleGroupToggle(
        this.selectedTest!.region,
        this.selectedTest!.testId,
        this.page,
        id,
        false
      )
      // TODO: Think more about this later
      // If res is true, then it means it was successfully registered to server
      if (res) delete this.testGroup![id]
      this.loading = false
    }
  }
})

export default useTestViewStore
