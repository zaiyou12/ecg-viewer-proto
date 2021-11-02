<template>
  <div class="group-list-container">
    <table class="table-group-list">
      <thead class="cursor-default">
        <th
          v-for="(col, idx) in groupHeader"
          :key="idx"
          class="border-b-2 h-7 px-3 py-1"
          :class="col.class"
        >{{ col.label }}</th>
      </thead>
      <tbody>
        <GroupListItem v-for="(g, idx) in groups" :key="idx" :group="g" />
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { toRef } from 'vue'
// @ts-ignore
import useDataLakeStore from '@/stores/data-lake'
import GroupListItem from './GroupListItem.vue';


const store = useDataLakeStore()
const groups = toRef(store, 'testGroups')
const groupHeader = [
  { label: 'ID', class: 'id' },
  { label: 'Group Name', class: 'group-name' },
  { label: 'Description', class: 'description' },
  { label: '# Tests', class: 'num-tests' },
  { label: 'PID', class: 'pid' },
]
</script>

<style>
@layer components {
  .group-list-container {
    @apply overflow-x-hidden overflow-y-auto overscroll-contain;
  }
  .group-list-container::-webkit-scrollbar {
    @apply opacity-0;
  }

  .table-group-list {
    @apply table-auto;
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
