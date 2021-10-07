<template>
  <div class="flex items-center justify-center">
    <div
      v-if="currentStartPage === 1"
      class="mr-5"
    >
      <SvgIcon name="ChevronDoubleLeft" stroke="#C0C0C0" :strokeWidth="strokeWidth" class="h-5 w-5"/>
    </div>
    <AppLink
      v-else
      name="testPagination" :params="{ page: 1 }"
      class="mr-5"
    >
      <SvgIcon name="ChevronDoubleLeft" :strokeWidth="strokeWidth" class="h-5 w-5"/>
    </AppLink>
    <div
      v-if="currentStartPage === 1"
      class="mr-5"
    >
      <SvgIcon name="ChevronLeft" stroke="#C0C0C0" :strokeWidth="strokeWidth" class="h-5 w-5"/>
    </div>
    <AppLink
      v-else
      name="testPagination" :params="{ page: goDownPage(maxPageDisplay) }"
      class="mr-5"
    >
      <SvgIcon name="ChevronLeft" :strokeWidth="strokeWidth" class="h-5 w-5"/>
    </AppLink>
    <AppLink
      v-for="index in currentDisplayPages"
      :key="index"
      :class="{
        'px-2 mx-1 rounded-lg font-bold': true,
        'bg-blue-100': isCurrentPage(index)
      }"
      name="testPagination" :params="{ page: index }"
    >
      {{ index }}
    </AppLink>
    <div
      v-if="currentStartPage === lastStartPage"
      class="ml-5"
    >
      <SvgIcon name="ChevronRight" stroke="#C0C0C0" :strokeWidth="strokeWidth" class="h-5 w-5"/>
    </div>
    <AppLink
      v-else
      name="testPagination" :params="{ page: goUpPage(maxPageDisplay) }"
      class="ml-5"
    >
      <SvgIcon name="ChevronRight" :strokeWidth="strokeWidth" class="h-5 w-5"/>
    </AppLink>
    <div
      v-if="currentStartPage === lastStartPage"
      class="ml-5"
    >
      <SvgIcon name="ChevronDoubleRight" stroke="#C0C0C0" :strokeWidth="strokeWidth" class="h-5 w-5"/>
    </div>
    <AppLink
      v-else
      name="testPagination" :params="{ page: totalPages }"
      class="ml-5"
    >
      <SvgIcon name="ChevronDoubleRight" :strokeWidth="strokeWidth" class="h-5 w-5"/>
    </AppLink>
  </div>
</template>

<script setup lang="ts">
import { computed, watch, ref } from 'vue'
import { useRoute } from 'vue-router'
import { paramToInt, range } from '../../utils/helper'
import SvgIcon from '@/components/SvgIcon.vue'


const props = defineProps<{
  numEcgTests: number
  maxTestsPerPage: number
  maxPageDisplay: number
}>()

const route = useRoute()

const currentPage = ref(1)

function calcStartPage(page: number): number {
  let div = Math.floor(page / props.maxPageDisplay)
  const mod = page % props.maxPageDisplay
  if (mod === 0) div -= 1
  return div * props.maxPageDisplay + 1
}

const currentStartPage = computed(() => calcStartPage(currentPage.value))
const currentDisplayPages = computed(() => {
  let endPage = currentStartPage.value + props.maxPageDisplay - 1
  return range(currentStartPage.value, Math.min(totalPages.value, endPage)+1)
})
const totalPages = computed(() => Math.ceil(props.numEcgTests / props.maxTestsPerPage))
const lastStartPage = computed(() => calcStartPage(totalPages.value))

const strokeWidth = 3

watch(() => route.params.page, () => {
  if (route.name === 'testPagination') {
    currentPage.value = paramToInt(route.params.page)
  }
})

function goDownPage(n: number): number {
  return currentStartPage.value <= n ? 1 : currentStartPage.value - n
}

function goUpPage(n: number): number {
  if (currentStartPage.value + n <= totalPages.value) {
    return currentStartPage.value + n
  } else {
    return totalPages.value
  }
}

function isCurrentPage(page: number): boolean {
  return page === paramToInt(route.params.page)
}
</script>
