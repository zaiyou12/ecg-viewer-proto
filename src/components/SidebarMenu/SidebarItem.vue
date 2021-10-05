<template>
  <li
    class="text-white text-l font-bold py-2 my-2 hover:bg-gray-500 rounded-lg"
  >
    <AppLink :name="sidebarRouter">
      <div class="flex items-center">
        <ChartPieIcon class="h-6 w-6 mx-1" />
        <!-- <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z" />
        </svg> -->
        <p>{{ sidebarLabel }}</p>
      </div>
    </AppLink>
  </li>
</template>

<script setup lang="ts">
import { ChartPieIcon } from '@heroicons/vue/outline'

const props = defineProps<{
  sidebarLabel: string,
  sidebarRouter: string
}>();
</script>
