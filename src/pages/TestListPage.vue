<template>
  <div class="flex flex-col">
    <div class="flex-none">
      <TestFilterBar v-model:searchInput="query" />
    </div>
    <div class="flex-grow mx-5">
      <router-view name="testList" v-bind="{ currentTests, maxTestsPerPage }" />
    </div>
    <div class="flex-none my-10">
      <router-view name="pagination" v-bind="{ numEcgTests, maxTestsPerPage, maxPageDisplay}" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch, watchEffect } from 'vue'
import { useRouter } from 'vue-router'
import TestFilterBar from '@/components/TestFilterBar.vue'
// @ts-ignore
import useTests from '@/composables/use-tests'


const router = useRouter()
const { ecgTests, makeEcgTests, makeDummyEcgTests, searchEcgTest } = useTests()

const numTestSeqs = ref(35)
watchEffect(() => {
  makeEcgTests(makeDummyEcgTests(numTestSeqs.value))
})

const currentTests = ref(ecgTests.value)
const numEcgTests = computed(()=> currentTests.value.length)
const maxTestsPerPage = 15
const maxPageDisplay = 10

const query = ref('')
watch(query, () => {
  if (query.value) {
    const test: EcgTest.Meta = searchEcgTest(query.value)
    if (test) {
      console.log(`Search output was ${test.testSeq}`)
      currentTests.value = [test]
    } else {
      console.log('No matching search')
      currentTests.value = []
    }
    router.push( { name: 'testPagination', params: { page: 1 } } )
  } else {
    currentTests.value = ecgTests.value
  }
})

</script>
