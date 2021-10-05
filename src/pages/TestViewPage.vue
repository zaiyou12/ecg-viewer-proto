<template>
  <div class="my-8">Test Viewer - {{ index }}</div>
  <TestDetails />
  <div class="my-4">
    <AppLink name="tests"> > GO BACK TO TestList </AppLink>
  </div>
</template>

<script lang="ts" setup>
import { useRoute } from 'vue-router'
import TestDetails from '@/components/TestDetails.vue'

const route = useRoute()
const index = route.params.index
</script>
