<template>
  <div class="w-screen h-screen overflow-hidden overscroll-none box-border flex">
    <SidebarMenu class="flex-none"/>
    <div class="flex-auto overflow-y-auto overscroll-none">
      <router-view/>
    </div>
  </div>
</template>

<script setup lang="ts">
import SidebarMenu from '@/components/SidebarMenu/index.vue'
</script>
