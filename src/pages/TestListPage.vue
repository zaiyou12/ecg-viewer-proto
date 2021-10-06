<template>
  <div class="flex flex-col">
    <div class="flex-none">
      <TestFilterBar />
    </div>
    <div class="flex-grow mx-5">
      <TestList />
    </div>
    <div class="flex-none my-10">
      <Pagination />
    </div>
  </div>
</template>

<script setup lang="ts">
import TestList from '@/components/TestList/index.vue'
import TestFilterBar from '@/components/TestFilterBar.vue'
import Pagination from '@/components/Pagination.vue'
</script>
