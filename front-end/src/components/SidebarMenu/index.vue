<template>
  <div class="sidebar-menu">
    <MainLink class="transform mb-10" />
    <GoBack class="mb-5" />
    <ul class="px-5">
      <SidebarItem
        v-for="(opt, index) in sidebarOptions"
        :key="index"
        :label="opt.label"
        :routerName="opt.router"
        :icon="opt.icon"
      />
    </ul>
  </div>
</template>

<script setup lang="ts">
import SidebarItem from './SidebarItem.vue'
import MainLink from './MainLink.vue'
import GoBack from './GoBack.vue'

const sidebarOptions = [
  {
    label: 'Dashboard',
    router: 'dashboard',
    icon: 'ChartPie'
  },
  {
    label: 'Tests',
    router: 'tests',
    icon: 'Collection'
  },
  {
    label: 'Preprocess',
    router: 'preprocess',
    icon: 'ChevronRight'
  },
  {
    label: 'Test Group',
    router: 'testGroup',
    icon: 'ChevronRight'
  },
  {
    label: 'Sample Group',
    router: 'sampleGroup',
    icon: 'ChevronRight'
  }
]
</script>

<style>
@layer components {
  .sidebar-menu {
    @apply w-52 h-full overflow-x-hidden overflow-y-auto overscroll-none py-5
      bg-gradient-to-br from-blue-500 to-blue-300
      rounded-tr-3xl;
  }
}
</style>
