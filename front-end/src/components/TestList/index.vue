<template>
  <table class="table-test-list">
    <thead class="cursor-default">
      <th
        v-for="(col, idx) in testCols"
        :key="idx"
        class="border-b h-12"
        :class="col.class"
      >{{ col.label }}</th>
    </thead>
    <tbody>
      <template v-for="(test, idx) in store.tests" :key="idx">
        <TestListItem
          :ecgTest="test"
          :testCols="testCols"
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

const testCols: TestCol[] = [
  // { label: 'DB ID', class: 'db-id', prop: 'id'},
  { label: 'Region', class: 'reg', prop: 'region' },
  { label: 'Org', class: 'org-code', prop: 'orgCode' },
  { label: 'Site', class: 'site-name', prop: 'siteName' },
  { label: 'Test Seq', class: 'test-seq', prop: 'seq' },
  { label: 'Duration', class: 'dur', prop: 'duration' },
  { label: 'Status', class: 'stat', prop: 'condition' },
]

</script>

<style>
@layer components {
  .table-test-list {
    @apply table-fixed w-full;
  }
  .table-test-list .org-code {
    width: 15%;
  }
  .table-test-list .site-name {
    width: 25%;
  }
  /* .table-test-list th.test-seq,
  td.test-seq {
    width: 40%;
  } */
  .table-test-list .reg,
  .table-test-list .dur,
  .table-test-list .stat {
    width: 10%;
  }
}
</style>
