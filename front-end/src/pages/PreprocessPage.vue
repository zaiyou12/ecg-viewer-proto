<template>
  <p>This is a preprocess page.</p>
  <ul>
    <li v-for="(g, idx) in store.preprocessGroups" :key="idx">
      {{ g }}
    </li>
  </ul>
</template>

<script setup lang="ts">
import useDataLakeStore from '../stores/data-lake'

const store = useDataLakeStore()
</script>
