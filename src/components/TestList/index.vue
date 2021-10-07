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
      <TestListItem
        v-for="(test, index) in currentTests"
        :key="index"
        :ecgTest="test"
        class="h-10 border-b"
      />
    </tbody>
  </table>
</template>

<script lang="ts" setup>
import TestListItem from './TestListItem.vue'


const props = defineProps<{
  currentTests: EcgTest.Meta[]
  maxTestsPerPage: number
}>()

const listHeaders = ['Test Seq', 'Duration', 'Region', 'Sampled', 'Normal']

// const range = (n: number) => [...Array(n).keys()]
</script>
