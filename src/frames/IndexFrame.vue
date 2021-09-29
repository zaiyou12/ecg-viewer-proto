<template>
  <div class="w-screen h-screen overflow-hidden flex box-border">
    <div class="flex-none w-60">
      <SidebarMenu />
    </div>
    <div class="flex-auto overflow-y-auto">
      <TestListPage />
    </div>
  </div>
</template>

<script setup lang="ts">
import SidebarMenu from '@/components/SidebarMenu/index.vue'
import TestListPage from '@/pages/TestListPage.vue'
import EmptyPage from '@/pages/EmptyPage.vue'
</script>
