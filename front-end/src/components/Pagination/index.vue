<template>
  <div class="flex items-center justify-center">
    <PageNaveButton
      type="ffwLeft"
      :page="1"
      :disabled="currentStartPage === 1"
    />
    <PageNaveButton
      type="left"
      :page="goDownPage(maxPageDisplay)"
      :disabled="currentStartPage === 1"
    />
    <button
      v-for="index in currentDisplayPages"
      :key="index"
      :class="{
        'px-2 mx-1 rounded-lg font-bold hover:bg-blue-50': true,
        'bg-blue-100': isCurrentPage(index)
      }"
      @click="pageClick(index)"
    >{{ index }}</button>
    <PageNaveButton
      type="right"
      :page="goUpPage(maxPageDisplay)"
      :disabled="currentStartPage === lastStartPage"
    />
    <PageNaveButton
      type="ffwRight"
      :page="store.totalPages"
      :disabled="currentStartPage === lastStartPage"
    />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import PageNaveButton from './PageNavButton.vue'
import { range } from '../../utils/helper'
import useTestsStore from '../../stores/test-list'

const props = defineProps<{
  maxPageDisplay: number
}>()

const store = useTestsStore()

/**
 * Depends on the maxPageDisplay (default 10)
 * @returns Starting index page given the current page
 */
function calcStartPage(page: number): number {
  let div = Math.floor(page / props.maxPageDisplay)
  const mod = page % props.maxPageDisplay
  if (mod === 0) div -= 1
  return div * props.maxPageDisplay + 1
}

const currentStartPage = computed(() => calcStartPage(store.page))
const currentDisplayPages = computed(() => {
  let endPage = currentStartPage.value + props.maxPageDisplay - 1
  return range(currentStartPage.value, Math.min(store.totalPages, endPage) + 1)
})
const lastStartPage = computed(() => calcStartPage(store.totalPages))

function goDownPage(n: number): number {
  return currentStartPage.value <= n ? 1 : currentStartPage.value - n
}

function goUpPage(n: number): number {
  if (currentStartPage.value + n <= store.totalPages) {
    return currentStartPage.value + n
  } else {
    return store.totalPages
  }
}

function isCurrentPage(page: number): boolean {
  return page === store.page
}

async function pageClick(page: number) {
  if (isCurrentPage(page)) return
  store.page = page
  await store.fetchEcgTests()
}
</script>
