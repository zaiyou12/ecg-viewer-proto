<template>
  <SvgIconButton class="test-filter-btn"
    icon="Adjustments" text="Filter"
    @click="togglePanel"
  />
</template>

<script setup lang="ts">
import { inject } from 'vue'
import SvgIconButton from '@/components/SvgIconButton.vue'
// @ts-ignore
import { TogglePanelKey, VoidFunc } from '@/symbols/symbols'


const togglePanel: VoidFunc = inject(TogglePanelKey)
</script>

<style>
@layer components {
  .test-filter-btn {
    @apply rounded-md bg-blue-100
    py-2 px-3 /* focus:ring focus:ring-blue-300 */
    hover:bg-blue-50
  }
}
</style>
