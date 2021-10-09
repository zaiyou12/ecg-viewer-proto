<template>
  <TestFilterModal />
  <div class="flex flex-col">
    <TestFilterBar v-model:searchInput="query" class="flex-none" />
    <div class="flex-grow mx-5">
      <router-view name="testList" v-bind="{ currentTests, maxTestsPerPage }" />
    </div>
    <div class="flex-none my-10">
      <router-view name="pagination" v-bind="{ numEcgTests, maxTestsPerPage, maxPageDisplay}" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch, watchEffect, provide } from 'vue'
import { useRouter } from 'vue-router'
import TestFilterBar from '@/components/TestFilterBar/index.vue'
import TestFilterModal from '@/components/TestFilterModal/index.vue'
import useTests from '../composables/use-tests'
import { makeDummyEcgTests } from '../utils/make-dummy'
import { QueryKey, UpdateQueryKey } from '../symbols/symbols'


const router = useRouter()
const { ecgTests, makeEcgTests, searchEcgTest } = useTests()

const numTestSeqs = 500
watchEffect(() => {
  makeEcgTests(makeDummyEcgTests(numTestSeqs))
})

const currentTests = ref(ecgTests.value)
const numEcgTests = computed(()=> currentTests.value.length)
const maxTestsPerPage = 15
const maxPageDisplay = 10

const query = ref('')
const updateQuery = (q: string) => {
  query.value = q
}

provide(QueryKey, query)
provide(UpdateQueryKey, updateQuery)

watch(query, () => {
  if (query.value) {
    const test: EcgTest.Meta[] = searchEcgTest(query.value)
    currentTests.value = test
  } else {
    currentTests.value = ecgTests.value
  }
  router.push( { name: 'testPagination', params: { page: 1 } } )
})
</script>
