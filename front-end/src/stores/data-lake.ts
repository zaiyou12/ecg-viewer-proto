import { defineStore } from 'pinia'


type DataLakeState = {
  preprocessGroups: PreprocessGroups
  testGroups: TestGroups
  sampleGroups: SampleGroups
  anomalyGroups: AnomalyGroups
  numPreprocessGroups: number
  numTestGroups: number
  numSampleGroups: number
  numAnomalyGroups: number
}

const useDataLakeStore = defineStore('dataLake', {
  state: () => {
    return {
      preprocessGroups: {},
      testGroups: {},
      sampleGroups: {},
      anomalyGroups: {},
      numPreprocessGroups: 0,
      numTestGroups: 0,
      numSampleGroups: 0,
      numAnomalyGroups: 0
    } as DataLakeState
  },
  actions: {
    addPreprocessGroup(group: PreprocessGroup): void {
      this.preprocessGroups[this.numPreprocessGroups] = group
      this.numPreprocessGroups++
    },

    addTestGroup(group: TestGroup): void {
      this.testGroups[this.numTestGroups] = group
      this.numTestGroups++
    },

    addSampleGroup(group: SampleGroup): void {
      this.sampleGroups[this.numSampleGroups] = group
      this.numSampleGroups++
    },

    addAnomalyGroup(group: AnomalyGroup): void {
      this.anomalyGroups[this.numAnomalyGroups] = group
      this.numAnomalyGroups++
    }
  }
})

export default useDataLakeStore
