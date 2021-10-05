<template>
  <table class="table-fixed w-full">
    <thead>
      <th
        v-for="(label, index) in testHeaders"
        :key="index"
        class="w-1/3 border-b h-12"
      >
        {{ label }}
      </th>
    </thead>
    <tbody>
      <TestListItem
        v-for="(testSeq, index) in testSeqs"
        :key="index"
        :testSeq="testSeq"
        :index="index"
        class="h-10 border-b"
      />
    </tbody>
  </table>
  <!-- <div v-if="loading">Loading...</div>
  <div v-else-if="tests.length === 0">No tests here</div>
  <div v-else class="flex flex-col shadow text-left text-base text-gray-600">
    <ul class="flex-auto">
      <TestListItem
        v-for="(test, index) in testSeqs"
        :key="index"
        :testSeq="test"
        :index="index"
      />
    </ul>
  </div> -->
</template>

<script lang="ts" setup>
import TestListItem from "./TestListItem.vue";
const loading = false
const testSeqs = ['0000', '0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009']
const testHeaders = ['Test Seq', 'Sampled', 'Normal']
const colSizes = ['w-4/6', 'w-1/6', 'w-1/6']
</script>
