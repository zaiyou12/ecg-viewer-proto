import { ref } from 'vue'
import EcgTestApi from '../utils/ecg-test-api'

const ecgTests = ref<EcgTests>([])
const api = new EcgTestApi()

export default function useEcgTests() {
  async function fetchEcgTests(): Promise<void> {
    ecgTests.value = await api.getEcgTests()
  }

  function makeEcgTests(tests?: EcgTests): void {
    console.log('makeEcgTests called.')
    // To manually add tests during testing etc.
    if (tests != null) {
      tests.sort((x, y) => {
        if (x.testSeq < y.testSeq) return -1;
        if (x.testSeq > y.testSeq) return 1;
        return 0;
      })
      ecgTests.value = tests
      return
    }
    // fetchEcgTests()
  }

  function searchEcgTest(testSeq: string): EcgTests {
    const test = ecgTests.value.find((t) => t.testSeq === testSeq)
    return test ? [test] : []
  }

  return {
    ecgTests,
    makeEcgTests,
    searchEcgTest
  }
}
