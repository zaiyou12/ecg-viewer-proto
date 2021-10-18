<template>
  <div class="test-detail-header-container">
    <div class="h-full flex items-center justify-between mx-5 border-b-2 border-gray-100">
      <div class="w-1/2 flex items-center cursor-default justify-between">
        <p class="ml-5 mr-5 font-bold text-2xl text-left">Test {{ store.selectedTest!.testSeq }}</p>
        <div class="flex flex-wrap text-sm">
          <p class="w-1/2 text-left"><b>HR</b> 100</p>
          <p class="w-1/2 text-left"><b>DUR</b> {{ store.selectedTest!.duration }}H</p>
          <p class="w-full text-left"><b>STAT</b> {{ store.selectedTest!.status.final.toUpperCase() }}</p>
        </div>
      </div>
      <div class="w-1/2 border-l">
        <GroupSelectorBar />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import GroupSelectorBar from './GroupSelectorBar.vue'
import useTestViewStore from '../../stores/test-view'


const store = useTestViewStore()
</script>

<style>
@layer components {
  .test-detail-header-container {
    z-index: 98;
    min-width: 1024px;
    @apply fixed left-0 top-0 right-52 h-16
      transform translate-x-52
      bg-white
  }
}
</style>
