import { defineStore } from 'pinia'
import DataLakeApi from '../utils/data-lake-api'

const api = new DataLakeApi()

type DataLakeState = {
  durations: EcgTest.Duration[]
  regions: EcgTest.Region[]
  conditions: EcgTest.ConditionType[]
  preprocessGroups: PreprocessGroups
  testGroups: TestGroups
  sampleGroups: SampleGroups
  anomalyGroups: AnomalyGroups
  numPreprocessGroups: number
  numTestGroups: number
  numSampleGroups: number
  numAnomalyGroups: number
  loading: boolean
}

const useDataLakeStore = defineStore('dataLake', {
  state: () => {
    return {
      durations: [24, 48, 72],
      regions: ['KR', 'AU', 'UK', 'SG'],
      conditions: ['normal', 'abnormal', 'unknown'],
      preprocessGroups: {},
      testGroups: {},
      sampleGroups: {},
      anomalyGroups: {},
      numPreprocessGroups: 0,
      numTestGroups: 0,
      numSampleGroups: 0,
      numAnomalyGroups: 0,
      loading: false
    } as DataLakeState
  },
  actions: {
    async fetchGroupList(type: 't' | 's' | 'p'): Promise<void> {
      this.loading = true
      const res = await api.getGroupList(type)
      if (res === undefined) return
      switch (type) {
        case 't':
          this.numTestGroups = res.numGroups
          this.testGroups = res.groups as TestGroups
          break
        case 's':
          this.numSampleGroups = res.numGroups
          this.sampleGroups = res.groups as SampleGroups
          break
        case 'p':
          this.numPreprocessGroups = res.numGroups
          this.preprocessGroups = res.groups as PreprocessGroups
          break
      }
      this.loading = false
    }
  }
})

export default useDataLakeStore
