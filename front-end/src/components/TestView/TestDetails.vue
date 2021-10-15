<template>
  <div>
    <div class="flex items-baseline">
      <div class="mt-5 mb-1 text-left mx-14 font-bold">Details</div>
      <div class="text-sm mr-10">Recording Start Time: {{ store.selectedTest!.startTime }}</div>
      <div class="text-sm mr-10">Actual Duration: 12:29:32</div>
      <div class="text-sm">File Path: {{ store.selectedTest!.path }}</div>
    </div>
    <div class="mt-5 mb-1 text-left mx-14 font-bold">60s Strips</div>
    <div>
      <Strip
        v-for="index in numStrips"
        :key="index"
        :type="`g${index}`"
      />
    </div>
    <div class="flex flex-col justify-center">
      <div class="flex items-center justify-center h-16">
        <TestNavButton type="left" class="mx-2"/>
        <TestNavButton type="right" class="mx-2"/>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Strip from '@/components/Strip60s.vue'
import TestNavButton from './TestNavButton.vue'
import useTestViewStore from '../../stores/test-view';


const store = useTestViewStore()
const numStrips = 6
</script>
