<template>
  <table class="table-fixed w-full">
    <thead class="cursor-default">
      <th
        v-for="(label, index) in listHeaders"
        :key="index"
        class="border-b h-12"
      >
        {{ label }}
      </th>
    </thead>
    <tbody>
      <template
        v-for="index in totalDisplayRows"
        :key="index"
      >
        <TestListItem
          v-if="index-1 >= startIndex && index-1 < endIndex"
          :ecgTest="currentTests[index-1]" class="border-b h-10"
        />
      </template>
    </tbody>
  </table>
</template>

<script lang="ts" setup>
import { ref, watch, computed } from 'vue'
import { useRoute } from 'vue-router'
import TestListItem from './TestListItem.vue'
import { paramToInt } from '../../utils/helper'


const props = defineProps<{
  currentTests: EcgTest.Meta[]
  maxTestsPerPage: number
}>()

const route = useRoute()

const listHeaders = ['Test Seq', 'Duration', 'Region', 'Sampled', 'Normal']

const startIndex = ref(0)
const endIndex = computed(() => startIndex.value + props.maxTestsPerPage)
const totalDisplayRows = computed(() => {
  const neededPages = Math.ceil(props.currentTests.length / props.maxTestsPerPage)
  return neededPages * props.maxTestsPerPage
})

watch(() => route.params.page, () => {
  if (route.name === 'testPagination') {
    const idx = paramToInt(route.params.page)
    const perPage = props.maxTestsPerPage
    startIndex.value = (idx-1) * perPage
  }
})
</script>
