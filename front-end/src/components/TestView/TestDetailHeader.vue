<template>
<div class="relative">
  <div class="test-detail-header-container">
    <div class="h-full flex items-center">
      <div class="test-detail-header">
        <p>Test {{ testSeq }}</p>
      </div>
      <div class="w-2/3 flex items-center">
        <div class="w-1/3">
          <div class="mx-5 cursor-pointer hover:bg-blue-50">Preprocess Group</div>
        </div>
        <div class="w-1/3 border-l">
          <div class="mx-5 cursor-pointer hover:bg-blue-50">Test Group</div>
        </div>
        <div class="w-1/3 border-l">
          <div class="mx-5 cursor-pointer hover:bg-blue-50">Sample Group</div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script lang="ts" setup>
const props = defineProps<{
  testSeq: EcgTest.TestSeq
}>()
</script>

<style>
@layer components {
  .test-detail-header-container {
    z-index: 98;
    @apply fixed left-0 top-0 right-60 h-16
      transform translate-x-60
      mx-5 border-b-2 border-gray-100 bg-white
  }

  .test-detail-header {
    @apply w-1/3 h-1/2 flex-none border-r flex items-center pl-5
      font-bold text-2xl cursor-default
  }
}
</style>
