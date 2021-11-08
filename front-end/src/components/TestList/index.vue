<template>
  <table class="table-test-list">
    <thead class="cursor-default">
      <th
        v-for="(col, idx) in listHeaders"
        :key="idx"
        class="border-b h-12"
        :class="col.id"
      >{{ col.label }}</th>
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

/**
 * Must be in order with the deserialized EcgTest.Meta object
 * @see deserializer.deserializeTest
 */
const listHeaders = [
  { label: 'DB ID', id: 'db-id' },
  { label: 'Test Seq', id: 'test-seq' },
  { label: 'Region', id: 'reg' },
  { label: 'Duration', id: 'dur' },
  { label: 'Status', id: 'stat' },
]
</script>

<style>
@layer components {
  .table-test-list {
    @apply table-fixed w-full;
  }
  .table-test-list th.db-id {
    width: 15%;
  }
  .table-test-list th.reg,
  th.dur,
  th.stat {
    width: 15%;
  }
}
</style>
