import { ref, computed } from 'vue'


const ecgTests = ref<EcgTest.Meta[]>([])

export default function useEcgTests() {
  async function fetchEcgTests(): Promise<void> {
    ecgTests.value = []
    let responsePromise: null | Promise<ServerResponse.EcgTests>
  }

  function makeEcgTests(tests?: EcgTest.Meta[]): void {
    // To manually add tests during testing etc.
    if (tests != null) {
      ecgTests.value = tests
      return
    }
    // fetchEcgTests()
  }

  return {
    ecgTests,
    makeEcgTests
  }
}
