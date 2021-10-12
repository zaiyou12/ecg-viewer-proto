import { defineStore } from 'pinia'

export type EcgTestsState = {
  ecgTests: EcgTests
}

export const useEcgTestsStore = defineStore('ecgTests', {
  state: () => {
    return { ecgTests: [] } as EcgTestsState
  },
  getters: {
    // justPracticingGetters: (state) => state.ecgTests
    // justPracticingGetters(): EcgTests {
    //   return this.ecgTests
    // }
  }
})
