import { ref } from 'vue'


const dataLake = ref<DataLake.Meta>()

export default function useDataLake() {
  function initDataLake(fsRootPath: string, numEcgTests: number) {
    dataLake.value = {
      fsRootPath,
      numEcgTests
    }
  }

  function incNumEcgTests(increase = 1) {
    if (dataLake.value != null) {
      dataLake.value.numEcgTests += increase
    }
  }

  return {
    dataLake,
    initDataLake
  }
}
