<template>
  <div class="w-screen h-screen overflow-hidden flex box-border">
    <div class="flex-none w-60">
      <SidebarMenu />
    </div>
    <div class="flex-auto overflow-y-auto">
      <router-view name="dashboard"/>
      <router-view name="tests"/>
    </div>
  </div>
</template>

<script setup lang="ts">
import SidebarMenu from '@/components/SidebarMenu/index.vue'


</script>
