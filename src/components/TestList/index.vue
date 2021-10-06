<template>
  <table class="table-fixed w-full">
    <thead class="cursor-default">
      <th
        v-for="(label, index) in testHeaders"
        :key="index"
        class="border-b h-12"
      >
        {{ label }}
      </th>
    </thead>
    <tbody>
      <TestListItem
        v-for="(testSeq, index) in testSeqs"
        :key="index"
        :testSeq="testSeq"
        :duration="duration"
        :region="region"
        :index="index"
        class="h-10 border-b"
      />
    </tbody>
  </table>
</template>

<script lang="ts" setup>
import TestListItem from './TestListItem.vue'
import useTests from '@/composables/use-tests'

const { ecgTests, makeEcgTests } = useTests()

const duration = 24
const region = 'AU'
const numTestSeqs = 15
const testHeaders = ['Test Seq', 'Duration', 'Region', 'Sampled', 'Normal']

const range = (n: number) => [...Array(n).keys()]
const testSeqs = range(numTestSeqs).map((n: number) => `000${n}`)
</script>
