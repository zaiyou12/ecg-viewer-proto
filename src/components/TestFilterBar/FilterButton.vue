<template>
  <SvgIconButton class="test-filter-btn"
    icon="Adjustments" text="Filter"
  />
</template>

<script setup lang="ts">
import SvgIconButton from '@/components/SvgIconButton.vue'
</script>

<style>
@layer components {
  .test-filter-btn {
    @apply rounded-md bg-blue-100
    py-2 px-3 focus:ring focus:ring-blue-300
    focus:bg-blue-100 hover:bg-blue-50
  }
}
</style>
