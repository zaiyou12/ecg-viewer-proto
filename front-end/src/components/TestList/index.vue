<template>
  <table class="table-test-list">
    <thead class="cursor-default">
      <th
        v-for="(col, idx) in listHeaders"
        :key="idx"
        class="border-b h-12"
        :class="col.class"
      >{{ col.label }}</th>
    </thead>
    <tbody>
      <template v-for="(test, idx) in store.tests" :key="idx">
        <TestListItem
          :ecgTest="test"
          :testCols="listHeaders"
          class="border-b h-11"
        />
      </template>
    </tbody>
  </table>
</template>

<script lang="ts" setup>
import TestListItem from './TestListItem.vue'
import useTestsStore from '../../stores/test-list'

const store = useTestsStore()

/**
 * Must be in order with the deserialized EcgTest.Meta object
 * @see deserializer.deserializeTest
 */
const listHeaders: TestCol[] = [
  { label: 'DB ID', class: 'db-id' },
  { label: 'Test Seq', class: 'test-seq' },
  { label: 'Region', class: 'reg' },
  { label: 'Duration', class: 'dur' },
  { label: 'Status', class: 'stat' },
]
</script>

<style>
@layer components {
  .table-test-list {
    @apply table-fixed w-full;
  }
  .table-test-list th.db-id,
  td.db-id {
    width: 15%;
  }
  .table-test-list th.reg,
  th.dur,
  th.stat,
  td.reg,
  td.dur,
  td.stat {
    width: 15%;
  }
}
</style>
