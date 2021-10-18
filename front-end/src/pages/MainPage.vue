<template>
  <div class="w-screen h-screen box-border flex">
    <SidebarMenu class="flex-none"/>
    <div class="flex-auto overflow-y-auto overscroll-none">
      <router-view/>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import SidebarMenu from '@/components/SidebarMenu/index.vue'
import useDataLakeStore from '../stores/data-lake'
import useTestsStore from '../stores/ecg-tests'
import { makeDummyEcgTests, makeDummyPreprocessGroups, makeDummyTestGroups, makeDummySampleGroups } from '../utils/make-dummy'


const lakeStore = useDataLakeStore()
const testStore = useTestsStore()

onMounted(() => {
  const numP = 2
  lakeStore.preprocessGroups = makeDummyPreprocessGroups(numP)
  lakeStore.numPreprocessGroups += 2
  const numT = 4
  lakeStore.testGroups = makeDummyTestGroups(numT)
  lakeStore.numTestGroups += numT
  const numS = 3
  lakeStore.sampleGroups = makeDummySampleGroups(numS)
  lakeStore.numSampleGroups += numS

  const numTestSeqs = 500
  testStore.makeEcgTests(makeDummyEcgTests(numTestSeqs))
})
</script>
