<template>
  <div class="px-10">
    <table class="table-group-list">
      <thead class="cursor-default">
        <th
          v-for="(col, idx) in testGroupHeader"
          :key="idx"
          class="border-b-2 h-7 px-3 py-1"
          :class="col.class"
        >{{ col.label }}</th>
      </thead>
      <tbody>
        <TestGroupListItem
          v-for="(g, idx) in store.testGroups"
          :key="idx"
          :group="g"
        />
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
// @ts-ignore
import useDataLakeStore from '@/stores/data-lake'
import TestGroupListItem from './TestGroupListItem.vue';


const store = useDataLakeStore()

const testGroupHeader = [
  { label: 'ID', class: 'id' },
  { label: 'Group Name', class: 'group-name' },
  { label: 'Description', class: 'description' },
  { label: '# Tests', class: 'num-tests' },
  { label: 'PID', class: 'pid' },
]
</script>

<style>
@layer components {
  .table-group-list {
    @apply table-auto w-1/2;
  }
  .table-group-list th.id,
  th.pid {
    width: 5%;
  }
  .table-group-list th.group-name {
    width: 25%;
  }
  .table-group-list th.num-tests {
    width: 15%;
  }
}
</style>
