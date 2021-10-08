<template>
  <li @click="routeTo" class="sidebar-item">
    <div class="flex items-center text-white">
      <SvgIcon :name="sidebarIcon" class="h-6 w-6 mx-2" />
      <p class="text-l font-bold">{{ sidebarLabel }}</p>
    </div>
  </li>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'


const props = defineProps<{
  sidebarLabel: string
  sidebarRouter: string
  sidebarIcon: string
}>()

const router = useRouter()

function routeTo(e: Event) {
  router.push({ name: props.sidebarRouter })
}
</script>

<style>
@layer components {
  .sidebar-item {
    @apply h-10 cursor-pointer py-2 my-2
      hover:bg-blue-600 rounded-lg
  }
}
</style>
