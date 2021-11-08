<template>
  <div>
    <p class="text-sm font-bold flex mb-1">{{ heading }}</p>
    <RowButtons :labels="options" :type="type" />
  </div>
</template>

<script setup lang="ts">
import RowButtons from './RowButtons.vue'

const props = defineProps<{
  heading: string
  options: string[] | number[]
  type: 'duration' | 'region' | 'condition'
}>()
</script>
