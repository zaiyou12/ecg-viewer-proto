import { defineStore } from 'pinia'


type TestViewState = {
  selectedTest: undefined | EcgTest.Meta
  start: number
}

const useTestViewStore = defineStore('testView', {
  state: () => {
    return {
      selectedTest: undefined,
      start: 0
    } as TestViewState
  },
  actions: {
    addToTestGroup(gid: TestGroupId): void {
      this.selectedTest!.tGroup.push(gid)
    },

    delFromTestGroup(gid: TestGroupId): void {
      const index = this.selectedTest!.tGroup.indexOf(gid)
      this.selectedTest!.tGroup.splice(index, 1)
    },

    addSampleTo(gid: SampleGroupId, strip: EcgStrip): void {
      // this.selectedTest!.sGroup[gid] = strip
    },

    delSampleFrom(gid: SampleGroupId, strip: EcgStrip): void {
      // const index = this.selectedTest!.sGroup[gid].indexOf(gid)
      // this.selectedTest!.sGroup.splice(index, 1)
    },

    // TODO: Need to connect to back later
    getPrevStrips(): void {
      const window = 60 * 6
      if (this.start >= window) this.start -= window
    },

    // TODO: If promise from back resolves, then increment and display
    getNextStrip(): void {
      const window = 60 * 6
      this.start += window
    }
  }
})

export default useTestViewStore
