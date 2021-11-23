<template>
  <input
    type="text"
    class="test-detail-strip-search"
    title="Enter page number or HH:MM:SS syntax"
    :placeholder="'Max page: ' + store.totalPage.toString()"
    v-model="stripSearchInput"
    @keyup.enter="pressedEnter"
  />
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import useTestViewStore from '../../stores/test-view';

const store = useTestViewStore()

const stripSearchInput = ref('')
const isInputPage = () => {
  const re = new RegExp(/^(?:[1-9]|[1-9]\d+)$/)
  return re.test(stripSearchInput.value)
}
const isInputTime = () => {
  const re = new RegExp(/^(?:[0-6]\d|7[0-2]):(?:[0-5]\d):(?:[0-5]\d)$/)
  return re.test(stripSearchInput.value)
}

function timeToPage(timeString: string) {
  const timeArr = timeString.split(':')
  const page = parseInt(timeArr[0]) * 60 + parseInt(timeArr[1])
  const lastMin = parseInt(timeArr[2]) > 0 ? 1 : 0
  return page + lastMin
}

async function pressedEnter() {
  let page = 0
  if (isInputPage()) {
    page = parseInt(stripSearchInput.value)
  } else if (isInputTime()) {
    page = timeToPage(stripSearchInput.value)
  } else return

  if (page > 0 && page < store.totalPage) await store.getStrips(page)
}
</script>

<style>
@layer components {
  .test-detail-strip-search {
    @apply border w-36 py-1 rounded-lg text-center
    focus:outline-none focus:bg-blue-100;
  }
}
</style>
