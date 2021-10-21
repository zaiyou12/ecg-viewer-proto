import { defineStore } from 'pinia'
import GroupApi from '../utils/group-api'

const api = new GroupApi()

type DataLakeState = {
  preprocessGroups: PreprocessGroups
  testGroups: TestGroups
  sampleGroups: SampleGroups
  anomalyGroups: AnomalyGroups
  numPreprocessGroups: number
  nextPreprocessGroupId: number
  numTestGroups: number
  nextTestGroupId: number
  numSampleGroups: number
  nextSampleGroupId: number
  numAnomalyGroups: number
  nextAnomalyGroupId: number
  loading: boolean
}

const useDataLakeStore = defineStore('dataLake', {
  state: () => {
    return {
      preprocessGroups: {},
      testGroups: {},
      sampleGroups: {},
      anomalyGroups: {},
      numPreprocessGroups: 0,
      nextPreprocessGroupId: 0,
      numTestGroups: 0,
      nextTestGroupId: 0,
      numSampleGroups: 0,
      nextSampleGroupId: 0,
      numAnomalyGroups: 0,
      nextAnomalyGroupId: 0,
      loading: false
    } as DataLakeState
  },
  getters: {},
  actions: {
    async fetchGroupList(type: 't' | 's' | 'p'): Promise<void> {
      this.loading = true
      const res = await api.getGroupList(type)
      if (res === undefined) return
      switch (type) {
        case 't':
          this.numTestGroups = res.numGroups
          this.testGroups = res.groups
          break
        case 's':
          this.numSampleGroups = res.numGroups
          this.sampleGroups = res.groups
          break
        case 'p':
          this.numPreprocessGroups = res.numGroups
          this.preprocessGroups = res.groups
          break
      }
      this.loading = false
    }
  }
})

export default useDataLakeStore
