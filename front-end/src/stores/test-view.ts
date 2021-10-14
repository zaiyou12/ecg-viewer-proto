import { defineStore } from 'pinia'


type TestViewState = {
  selectedTest: undefined | EcgTest.Meta
}

const useTestViewStore = defineStore('testView', {
  state: () => {
    return { selectedTest: undefined } as TestViewState
  }
})

export default useTestViewStore
