<template>
  <li
    class="text-white text-l font-bold py-2 my-2 hover:bg-gray-500 rounded-lg"
  >
    <AppLink :name="sidebarRouter">
      <div class="flex items-center">
        <SvgIcon name="ChartPie" class="h-6- w-6 mx-1" />
        <!-- <ChartPieIcon class="h-6 w-6 mx-1" /> -->
        <p>{{ sidebarLabel }}</p>
      </div>
    </AppLink>
  </li>
</template>

<script setup lang="ts">
// import { ChartPieIcon } from '@heroicons/vue/outline'
import SvgIcon from '@/components/SvgIcon.vue'

const props = defineProps<{
  sidebarLabel: string,
  sidebarRouter: string
}>();
</script>
