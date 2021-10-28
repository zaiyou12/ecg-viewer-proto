<template>
  <div class="flex">
    <div class="w-1/2 mt-5 mb-1 text-left ml-14 mr-5 font-bold">60s Strips</div>
    <div
      v-if="split"
      class="w-1/2 mt-5 mb-1 text-left ml-5 mr-14 font-bold"
    >Preprocessed</div>
  </div>
  <div v-if="!store.loading" class="strips-panel-container">
    <div class="h-full flex justify-center">
      <template v-if="split">
        <div class="flex h-full">
          <div class="w-1/2 flex flex-col justify-evenly border-r">
            <img :src="getStripUrl(0)" class="h-full ml-14 mr-5" />
          </div>
          <div class="w-1/2 flex flex-col justify-evenly border-l">
            <img :src="getStripUrl(1)" class="h-full ml-5 mr-14" />
          </div>
        </div>
      </template>
      <template v-else>
        <img :src="getStripUrl(0)" class="w-full h-full mx-14" />
      </template>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import Strip from '@/components/Strip60s.vue'
import useTestViewStore from '../../stores/test-view'


const store = useTestViewStore()
const split = computed(() => {
  return store.pid !== undefined
})
// const numStrips = 6

function getStripUrl(idx = 0): string {
  const strips = store.stripUrl!
  const baseUrl = import.meta.env.VITE_API_BASE_URL
  console.log(baseUrl + strips[idx])
  return baseUrl + strips[idx]
}
</script>

<style>
@layer components {
  .strips-panel-container {
    height: 735px;
  }
}
</style>
