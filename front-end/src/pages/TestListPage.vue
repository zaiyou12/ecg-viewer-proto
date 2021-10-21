<template>
  <template v-if="store.loading">
    <div class="loading-screen-overlay"></div>
    <div class="loading-screen">Loading...</div>
  </template>
  <template v-else>
    <div class="flex flex-col">
      <TestFilterPanel v-model:showPanel="showPanel" />
      <TestFilterBar class="flex-none" />
      <div class="flex-grow mx-5">
        <TestList :maxPageDisplay="maxPageDisplay" />
        <!-- <router-view name="testList" :maxPageDisplay="maxPageDisplay" /> -->
      </div>
      <div class="flex-none my-10">
        <Pagination :maxPageDisplay="maxPageDisplay" />
        <!-- <router-view name="pagination" :maxPageDisplay="maxPageDisplay" /> -->
      </div>
    </div>
  </template>
</template>

<script setup lang="ts">
import { ref, onMounted, provide } from 'vue'
import TestFilterBar from '@/components/TestFilterBar/index.vue'
import TestFilterPanel from '@/components/TestFilterPanel/TestFilterPanel.vue'
import TestList from '@/components/TestList/index.vue'
import Pagination from '@/components/Pagination/index.vue'
import useTestsStore from '../stores/test-list'
import {
  QueryKey, UpdateQueryKey,
  TogglePanelKey, DisablePanelKey
} from '../symbols/symbols'

const store = useTestsStore()
// const maxTestsPerPage = 15
const maxPageDisplay = 10

const showPanel = ref(false)
const togglePanel = () => showPanel.value = !showPanel.value
const disablePanel = () => showPanel.value = false
provide(TogglePanelKey, togglePanel)
provide(DisablePanelKey, disablePanel)

// const query = ref('')
// const updateQuery = (q: string) => {
//   query.value = q
// }
// provide(QueryKey, query)
// provide(UpdateQueryKey, updateQuery)

// watch(query, () => {
//   if (query.value) {
//     const test: EcgTest.Meta[] = store.searchEcgTest(query.value)
//     currentTests.value = test
//   } else {
//     currentTests.value = ecgTests.value
//   }
//   router.push({ name: 'testPagination', params: { page: 1 } })
// })
</script>

<style>
@layer components {
  .loading-screen {
    z-index: 99;
    transform: translateX(50vw) translateX(-13rem) translateY(30vh);
    @apply absolute w-32 h-16 bg-gray-50 shadow rounded-2xl
    flex items-center justify-center;
  }
  .loading-screen-overlay {
    z-index: 98;
    @apply absolute opacity-0 w-screen h-screen;
  }
}
</style>
