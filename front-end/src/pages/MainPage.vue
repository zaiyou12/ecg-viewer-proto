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
import { makeDummyPreprocessGroups, makeDummyTestGroups, makeDummySampleGroups } from '../utils/make-dummy'


const store = useDataLakeStore()
onMounted(() => {
  const numP = 2
  store.preprocessGroups = makeDummyPreprocessGroups(numP)
  store.numPreprocessGroups += 2
  const numT = 4
  store.testGroups = makeDummyTestGroups(numT)
  store.numTestGroups += numT
  const numS = 3
  store.sampleGroups = makeDummySampleGroups(numS)
  store.numSampleGroups += numS
})
</script>
