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
  testGroups?: TestGroups
  totalPage: number
  page: number
  stripUrl?: string[]
  sampleGroups?: SampleGroups
  pid?: number
  loading: boolean
}

const useTestViewStore = defineStore('testView', {
  state: () => {
    return {
      selectedTest: undefined,
      details: undefined,
      testGroups: undefined,
      totalPage: 1,
      page: 1,
      stripUrl: undefined,
      sampleGroups: undefined,
      pid: undefined,
      loading: false
    } as TestViewState
  },
  actions: {
    resetState(): void {
      this.selectedTest = undefined
      this.details = undefined
      this.testGroups = undefined
      this.totalPage = 1
      this.page = 1
      this.stripUrl = undefined
      this.sampleGroups = undefined
      this.pid = undefined
      this.loading = false
    },

    async viewNewTest(id: EcgTest.Id, page?: number) {
      this.resetState()
      this.loading = true
      const res = await api.fetchTestView(id)
      if (res === undefined) {
        this.loading = false
        return
      }
      ;({
        selectedTest: this.selectedTest,
        details: this.details,
        testGroup: this.testGroups,
        totalPage: this.totalPage
      } = res)
      await this.getStrips(page)
      this.loading = false
    },

    isValidPage(page: number) {
      return 1 <= page && page <= this.totalPage
    },

    async getStrips(page?: number) {
      this.loading = true
      if (page != undefined) {
        if (this.isValidPage(page)) {
          this.page = page
        } else {
          this.loading = false
          return
        }
      }
      const res = await api.fetchStrips(
        this.selectedTest!.id,
        this.page,
        this.pid
      )
      if (res === undefined) {
        this.loading = false
        return
      }
      ;({ stripUrl: this.stripUrl, sampleGroup: this.sampleGroups } = res)
      this.loading = false
    },

    async getPrevStrips() {
      await this.getStrips(this.page - 1)
    },

    async getNextStrip() {
      await this.getStrips(this.page + 1)
    },

    async toggleSingleGroup(
      type: Resp.GroupType,
      id: number,
      groupName: string,
      toggle: boolean
    ) {
      this.loading = true
      const res = await api.postSingleGroupToggle(
        type,
        id,
        toggle,
        this.selectedTest!.id,
        type === 't' ? undefined : this.page
      )
      if (res) {
        const group = type === 't' ? this.testGroups! : this.sampleGroups!
        if (toggle) group[id] = { id, groupName }
        else delete group[id]
      }
      this.loading = false
    }
  }
})

export default useTestViewStore
