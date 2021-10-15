import { defineStore } from 'pinia'
import EcgTestApi from '../utils/ecg-test-api'


type EcgTestsState = {
  ecgTests: EcgTests
}

const api = new EcgTestApi()

const useTestsStore = defineStore('ecgTests', {
  state: () => {
    return { ecgTests: [] } as EcgTestsState
  },
  actions: {
    /**
     * Fetches the entire list of files and their metadata
     */
    async fetchEcgTests(): Promise<void> {
      this.ecgTests = await api.getEcgTests()
    },

    /**
     * Needs to be fixed so that it gets searches from back
     * @returns A single test meta wrapped in an array
     */
    searchEcgTest(testSeq: EcgTest.TestSeq): EcgTests {
      const test = this.ecgTests.find((t) => t.testSeq === testSeq)
      return test ? [test] : []
    },

    /**
     * Used to place dummy ECG tests for testing.
     * First sorts the given @param tests by its test sequence.
     * @param {EcgTests} tests Tests list that you want to manually set
     */
    makeEcgTests(tests?: EcgTests): void {
      console.log('makeEcgTests called.')
      if (tests != null) {
        tests.sort((x, y) => {
          if (x.testSeq < y.testSeq) return -1;
          if (x.testSeq > y.testSeq) return 1;
          return 0;
        })
        this.ecgTests = tests
      }
    }
  }
})

export default useTestsStore
