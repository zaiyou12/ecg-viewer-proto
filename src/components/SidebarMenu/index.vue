<template>
  <div ref="listRef" class="sidebar-menu">
    <div>
      <div class="cursor-default">
        A sidebar header
      </div>
      <ul>
        <SidebarItem
          v-for="(option, index) in sidebar_options"
          :key="index"
          :sidebar_option="option"
        />
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import SidebarItem from './SidebarItem.vue'

const sidebar_options = ['A', 'B', 'C', 'D']
</script>

<style>
@layer components {
  .sidebar-menu {
    @apply bg-gray-400 w-full h-full overflow-x-hidden z-0 pt-3
  }
}
</style>
