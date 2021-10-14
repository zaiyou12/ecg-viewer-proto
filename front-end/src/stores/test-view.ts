import { defineStore } from 'pinia'


type TestViewState = {
  selectedTest: undefined | EcgTest.Meta
}

const useTestViewStore = defineStore('testView', {
  state: () => {
    return { selectedTest: undefined } as TestViewState
  },
  actions: {
    addTestGroupToTest(gid: TestGroupId): void {
      this.selectedTest!.tGroup.push(gid)
    },

    delTestGroupFromTest(gid: TestGroupId): void {
      const index = this.selectedTest!.tGroup.indexOf(gid)
      this.selectedTest!.tGroup.splice(index, 1)
    },

    addSampleGroupToTest(gid: SampleGroupId): void {
      this.selectedTest!.sGroup.push(gid)
    },

    delSampleGroupFromTest(gid: SampleGroupId): void {
      const index = this.selectedTest!.sGroup.indexOf(gid)
      this.selectedTest!.sGroup.splice(index, 1)
    }
  }
})

export default useTestViewStore
