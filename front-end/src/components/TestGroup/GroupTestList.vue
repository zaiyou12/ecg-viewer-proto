<template>
  <div class="border rounded-lg p-5">
    <table class="table-test-list">
      <thead class="cursor-default">
        <th
          v-for="(col, idx) in listHeaders"
          :key="idx"
          class="border-b-2 h-7 px-3 py-1"
          :class="col.id"
        >{{ col.label }}</th>
      </thead>
      <tbody>
        <template v-for="(test, idx) in tests" :key="idx">
          <TestListItem :ecgTest="test" class="border-b h-11" />
        </template>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts" setup>
import { computed } from 'vue'
import TestListItem from '@/components/TestList/TestListItem.vue'
import useGroupPageStore from '../../stores/group-page'

const store = useGroupPageStore()
const tests = computed(() => store.type === 't' ? store.tests : store.samples)

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
    @apply table-fixed;
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
