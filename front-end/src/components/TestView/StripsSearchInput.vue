<template>
  <input
    type="number"
    class="test-detail-strip-search"
    :placeholder="store.totalPage.toString()"
    min="1"
    :max="store.totalPage.toString()"
    :value="store.page"
    @keyup.enter="pressedEnter"
  />
</template>

<script setup lang="ts">
import useTestViewStore from '../../stores/test-view';

const store = useTestViewStore()

async function pressedEnter() {
  const pageQuery = (
    document.querySelector('.test-detail-strip-search') as HTMLInputElement
  ).valueAsNumber
  await store.getStrips(pageQuery)
}
</script>

<style>
@layer components {
  .test-detail-strip-search {
    @apply border w-14 py-1 rounded-lg text-center
    focus:outline-none focus:bg-blue-100;
  }
  .test-detail-strip-search::-webkit-inner-spin-button,
  .test-detail-strip-search::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }
}
</style>
