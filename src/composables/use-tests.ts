import { ref } from 'vue'


const ecgTests = ref<EcgTest.Meta[]>([])

export default function useEcgTests() {
  async function fetchEcgTests(): Promise<void> {
    ecgTests.value = []
    let responsePromise: null | Promise<ServerResponse.EcgTests>
  }

  function makeEcgTests(tests?: EcgTest.Meta[]): void {
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

  function searchEcgTest(testSeq: string): EcgTest.Meta | undefined {
    const test = ecgTests.value.find((t) => t.testSeq === testSeq)
    return test
  }

  return {
    ecgTests,
    makeEcgTests,
    searchEcgTest
  }
}
