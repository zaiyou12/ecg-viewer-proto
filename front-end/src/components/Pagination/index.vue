<template>
  <div class="flex items-center justify-center">
    <PageNaveButton type="ffwLeft" :page="1"
      :disabled="currentStartPage === 1"
    />
    <PageNaveButton type="left" :page="goDownPage(maxPageDisplay)"
      :disabled="currentStartPage === 1"
    />
    <AppLink
      v-for="index in currentDisplayPages"
      :key="index"
      :class="{
        'px-2 mx-1 rounded-lg font-bold hover:bg-blue-50': true,
        'bg-blue-100': isCurrentPage(index)
      }"
      name="testPagination" :params="{ page: index }"
    >
      {{ index }}
    </AppLink>
    <PageNaveButton type="right" :page="goUpPage(maxPageDisplay)"
      :disabled="currentStartPage === lastStartPage || numEcgTests === 0"
    />
    <PageNaveButton type="ffwRight" :page="totalPages"
      :disabled="currentStartPage === lastStartPage || numEcgTests === 0"
    />
  </div>
</template>

<script setup lang="ts">
import { computed, watch, ref } from 'vue'
import { useRoute } from 'vue-router'
import PageNaveButton from './PageNavButton.vue'
import { paramToInt, range } from '../../utils/helper'


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
