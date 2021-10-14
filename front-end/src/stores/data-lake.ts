import { defineStore } from 'pinia'


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
      nextAnomalyGroupId: 0
    } as DataLakeState
  },
  getters: {
  },
  actions: {
    // Preprocess Group
    addPreprocessGroup(displayName: string, description?: string): void {
      this.preprocessGroups[this.nextPreprocessGroupId] = {
        id: this.numPreprocessGroups,
        displayName,
        description
      }
      this.numPreprocessGroups++
      this.nextPreprocessGroupId++
    },

    // Test Group
    addTestGroup(displayName: string, description?: string): void {
      this.testGroups[this.nextTestGroupId] = {
        id: this.numTestGroups,
        displayName,
        description,
        numEcgTests: 0,
        testSeqs: []
      }
      this.numTestGroups++
      this.nextTestGroupId++
    },

    delTestGroup(gid: TestGroupId): void {
      delete this.testGroups[gid]
      this.numTestGroups--
    },

    addTestSeqToTestGroup(gid: TestGroupId, testSeq: EcgTest.TestSeq): void {
      this.testGroups[gid].numEcgTests++
      this.testGroups[gid].testSeqs.push(testSeq)
    },

    delTestSeqFromTestGroup(gid: TestGroupId, testSeq:EcgTest.TestSeq): void {
      const index = this.testGroups[gid].testSeqs.indexOf(testSeq)
      this.testGroups[gid].testSeqs.splice(index, 1)
      this.testGroups[gid].numEcgTests--
    },

    addPreprocessToTestGroup(gid: TestGroupId, pid: PreprocessGroupId): void {
      this.testGroups[gid].preprocessId = pid
    },

    // Sample Group
    addSampleGroup(displayName: string, description?: string): void {
      this.sampleGroups[this.nextSampleGroupId] = {
        id: this.numSampleGroups,
        displayName,
        description,
        numStrips: 0,
        strips: []
      }
      this.numSampleGroups++
      this.nextSampleGroupId++
    },

    delSampleGroup(sid: SampleGroupId, strip: EcgStrip): void {
      delete this.sampleGroups[sid]
      this.numSampleGroups--
    },

    addStripToSampleGroup(sid: SampleGroupId, strip: EcgStrip): void {
      this.sampleGroups[sid].numStrips++
      this.sampleGroups[sid].strips.push(strip)
    },

    delStripFromSampleGroup(sid: SampleGroupId, strip: EcgStrip): void {
      const index = this.sampleGroups[sid].strips.findIndex(s => {
        return s.testSeq === strip.testSeq && s.start === strip.start
      })
      this.sampleGroups[sid].strips.splice(index, 1)
      this.sampleGroups[sid].numStrips--
    },

    addPreprocessToSampleGroup(sid: SampleGroupId, pid: PreprocessGroupId): void {
      this.sampleGroups[sid].preprocessId = pid
    },

    // Anomaly Group
    addAnomalyGroup(anomalyName: string, description: string): void {
      this.anomalyGroups[this.nextAnomalyGroupId] = {
        id: this.numAnomalyGroups,
        anomalyName,
        description,
        numEcgTests: 0,
        testSeqs: []
      }
      this.numAnomalyGroups++
      this.nextAnomalyGroupId++
    }
  }
})

export default useDataLakeStore
