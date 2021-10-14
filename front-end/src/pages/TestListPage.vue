<template>
  <div class="flex flex-col">
    <TestFilterPanel v-model:showPanel="showPanel" />
    <TestFilterBar class="flex-none" />
    <div class="flex-grow mx-5">
      <router-view name="testList" v-bind="{ currentTests, maxTestsPerPage }" />
    </div>
    <div class="flex-none my-10">
      <router-view name="pagination" v-bind="{ numEcgTests, maxTestsPerPage, maxPageDisplay}" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch, toRef, provide } from 'vue'
import { useRouter } from 'vue-router'
import TestFilterBar from '@/components/TestFilterBar/index.vue'
import TestFilterPanel from '@/components/TestFilterPanel/TestFilterPanel.vue'
import useTestsStore from '../stores/ecg-tests'
import { makeDummyEcgTests } from '../utils/make-dummy'
import { QueryKey, UpdateQueryKey,
          TogglePanelKey, DisablePanelKey } from '../symbols/symbols'


const router = useRouter()
const store = useTestsStore()

const numTestSeqs = 500
store.makeEcgTests(makeDummyEcgTests(numTestSeqs))
const ecgTests = toRef(store, 'ecgTests')

const currentTests = ref(ecgTests.value)
const numEcgTests = computed(()=> currentTests.value.length)
const maxTestsPerPage = 15
const maxPageDisplay = 10

const showPanel = ref(false)
const togglePanel = () => showPanel.value = !showPanel.value
const disablePanel = () => showPanel.value = false
provide(TogglePanelKey, togglePanel)
provide(DisablePanelKey, disablePanel)

const query = ref('')
const updateQuery = (q: string) => {
  query.value = q
}
provide(QueryKey, query)
provide(UpdateQueryKey, updateQuery)

watch(query, () => {
  if (query.value) {
    const test: EcgTest.Meta[] = store.searchEcgTest(query.value)
    currentTests.value = test
  } else {
    currentTests.value = ecgTests.value
  }
  router.push( { name: 'testPagination', params: { page: 1 } } )
})
</script>
