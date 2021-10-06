<template>
  <div class="flex justify-center">
    <a href="/auth/tests" class="mr-5">&lt;</a>
    <a
      class="mx-2"
      href="/auth/tests"
      v-for="label in numPageDisplay"
      :key="label"
    >
      {{ label }}
    </a>
    <a href="/auth/tests" class="ml-5">&gt;</a>
  </div>
</template>

<script setup lang="ts">
import PageButton from './PageButton.vue'
const numPageDisplay = 10
// const range = (n: number) => [...Array(n).keys()]
// const pageLabels = range(numPageDisplay).map(n => `${n+1}`)
</script>
