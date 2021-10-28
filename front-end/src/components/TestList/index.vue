<template>
  <table class="table-fixed w-full">
    <thead class="cursor-default">
      <th
        v-for="(label, index) in listHeaders"
        :key="index"
        class="border-b h-12"
      >{{ label }}</th>
    </thead>
    <tbody>
      <template v-for="(test, idx) in store.tests" :key="idx">
        <TestListItem :ecgTest="test" class="border-b h-11" />
      </template>
    </tbody>
  </table>
</template>

<script lang="ts" setup>
import TestListItem from './TestListItem.vue'
import useTestsStore from '../../stores/test-list'

const store = useTestsStore()

const listHeaders = ['Test ID', 'Duration', 'Region', 'Group', 'Status']
</script>
