<template>
  <div class="flex">
    <div class="w-1/2 mt-5 mb-1 text-left mx-14 font-bold">60s Strips</div>
    <div
      v-if="split"
      class="w-1/2 mt-5 mb-1 text-left mx-14 font-bold"
    >Preprocessed</div>
  </div>
  <div class="strips-panel-container">
    <div v-if="!split" class="h-full flex flex-col justify-evenly">
      <Strip v-for="index in numStrips" :key="index" :type="`g${index}`" />
    </div>
    <div v-else class="flex h-full">
      <div class="w-1/2 flex flex-col justify-evenly border-r">
        <Strip v-for="index in numStrips" :key="index" :type="`g${index}`" />
      </div>
      <div class="w-1/2 flex flex-col justify-evenly border-l">
        <Strip v-for="index in numStrips" :key="index" :type="`g${index}`" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import Strip from '@/components/Strip60s.vue'
import useTestViewStore from '../../stores/test-view'


const store = useTestViewStore()
const split = computed(() => {
  return store.pid != undefined
})
const numStrips = 6
console.log(store.stripUrl)
</script>

<style>
@layer components {
  .strips-panel-container {
    height: 735px;
  }
}
</style>
