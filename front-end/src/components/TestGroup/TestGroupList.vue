<template>
<div class="mx-5">
  <table class="table-auto w-full">
    <thead class="cursor-default">
      <th v-for="(prop, idx) in testGroupProps" :key="idx"
        class="border h-7 px-3"
      >
        {{ prop }}
      </th>
    </thead>
  </table>
  <tbody>
    <TestGroupListItem v-for="(g, idx) in store.testGroupProps"
      :key="idx" :group="g"
    />
  </tbody>
</div>
</template>

<script setup lang="ts">
// @ts-ignore
import useDataLakeStore from '@/stores/data-lake'
import TestGroupListItem from './TestGroupListItem.vue';


const store = useDataLakeStore()

const testGroupProps = ["Group ID", "Display Name", "Description", "Number of Tests", "Preprocess ID"]
</script>
