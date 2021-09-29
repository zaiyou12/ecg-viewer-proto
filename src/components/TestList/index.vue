<template>
  <div v-if="loading">Loading...</div>
  <div v-else-if="tests.length === 0">No tests here</div>
  <div v-else class="flex flex-col shadow text-left text-base text-gray-600">
    <div class="flex-auto">
      <TestItem
        v-for="(test, index) in tests"
        :key="index"
        :test="test"
        :index="index"
      />
    </div>
  </div>
</template>

<script lang="ts" setup>
import TestItem from "./TestItem.vue";
const loading = false
const tests = ['0000', '0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009']
</script>
