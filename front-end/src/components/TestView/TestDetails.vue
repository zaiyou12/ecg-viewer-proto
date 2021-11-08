<template>
  <div>
    <div class="flex items-baseline">
      <div class="mt-5 mb-1 text-left mx-14 font-bold">Details</div>
      <div
        class="text-sm mr-10"
      >Recording Start Time: {{ store.details!.startTime }}</div>
      <div
        class="text-sm mr-10"
      >Actual Duration: {{ store.details!.actualDuration }}</div>
      <!-- TODO: Add file path -->
      <div class="text-sm">File Path: {{ "N/A" }}</div>
    </div>
    <StripsPanel />
    <div class="flex items-center justify-center h-16">
      <StripsNavButton type="left" class="mx-2" />
      <StripsSearchInput />
      <StripsNavButton type="right" class="mx-2" />
    </div>
  </div>
</template>

<script setup lang="ts">
import StripsPanel from './StripsPanel.vue'
import StripsNavButton from './StripsNavButton.vue'
import StripsSearchInput from './StripsSearchInput.vue';
import useTestViewStore from '../../stores/test-view';

const store = useTestViewStore()
</script>
