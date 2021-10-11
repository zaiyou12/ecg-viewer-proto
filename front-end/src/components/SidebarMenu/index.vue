<template>
  <div class="sidebar-menu">
    <MainLink class="transform mb-10"/>
    <GoBack class="mb-5"/>
    <ul class="px-5">
      <SidebarItem
        v-for="(label, index) in sidebarLabels"
        :key="index"
        :sidebarLabel="label"
        :sidebarRouter="sidebarRouters[index]"
        :sidebarIcon="sidebarIcons[index]"
      />
    </ul>
  </div>
</template>

<script setup lang="ts">
import SidebarItem from './SidebarItem.vue'
import MainLink from './MainLink.vue'
import GoBack from './GoBack.vue'


const sidebarLabels = ['Dashboard', 'Tests', 'Cats', 'Sandbox']
const sidebarRouters = ['dashboard', 'tests', 'tests', 'sandbox']
const sidebarIcons = ['ChartPie', 'Collection', 'ChevronRight', 'ChevronRight']
</script>

<style>
@layer components {
  .sidebar-menu {
    @apply w-52 h-full overflow-x-hidden overflow-y-auto overscroll-none py-5
      bg-gradient-to-br from-blue-500 to-blue-300
      rounded-tr-3xl
  }
}
</style>
