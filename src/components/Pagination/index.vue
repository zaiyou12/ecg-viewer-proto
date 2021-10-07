<template>
  <div class="flex justify-center">
    <AppLink
      name="testPagination" :params="{ page: 1 }"
      class="mr-5"
    >
      <!-- <SvgIcon name="ChevronDoubleLeft" /> -->
      &lt;&lt;
    </AppLink>
    <AppLink
      name="testPagination" :params="{ page: goDownPage() }"
      class="mr-5"
    >
      &lt;
    </AppLink>
    <AppLink
      v-for="index in totalPages"
      :key="index"
      :class="{'px-2 rounded-lg': true, 'bg-blue-100': isCurrentPage(index)}"
      name="testPagination" :params="{ page: index }"
    >
      {{ index }}
    </AppLink>
    <AppLink
      name="testPagination" :params="{ page: goUpPage() }"
      class="ml-5"
    >
      &gt;
    </AppLink>
    <AppLink
      name="testPagination" :params="{ page: totalPages }"
      class="ml-5"
    >
      &gt;&gt;
    </AppLink>
    <!-- <a href="/main/tests" class="ml-5">&gt;&gt;</a> -->
  </div>
</template>

<script setup lang="ts">
import { computed, watch, ref } from 'vue'
import { useRoute } from 'vue-router'


const props = defineProps<{
  numEcgTests: number
  maxTestsPerPage: number
  maxPageDisplay: number
}>()

const route = useRoute()

const currentPage = ref(1)
const totalPages = computed(() => Math.ceil(props.numEcgTests / props.maxTestsPerPage))

function paramToInt(param: string | string[]): number {
  if (typeof param === 'string') {
    return +param
  } else {
    return +param[0]
  }
}

watch(() => route.params.page, () => {
  currentPage.value = paramToInt(route.params.page)
})

function goDownPage(): number {
  return currentPage.value <= 1 ? 1 : currentPage.value-1
}

function goUpPage(): number {
  return currentPage.value >= totalPages.value ? totalPages.value : currentPage.value+1
}

function isCurrentPage(page: number): boolean {
  return page === paramToInt(route.params.page)
}
</script>
