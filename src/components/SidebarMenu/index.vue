<template>
  <div ref="listRef" class="sidebar-menu">
    <div>
      <div class="flex items-center ml-8 mb-10">
        <AppLink name="main" class="flex-none">
          <img :src="logo" class="w-12 h-12"/>
        </AppLink>
        <AppLink name="main" class="text-white text-xl font-bold">
          ECG-Proto
        </AppLink>
      </div>
      <div
        class="flex items-center cursor-pointer
              bg-blue-300 h-14 py-3 mb-5 text-white font-bold hover:bg-blue-200"
        @click="goBack()"
      >
        <SvgIcon name="ArrowCircleLeft" class="h-6 w-6 ml-20 mr-2" />
        <p>Back</p>
      </div>
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
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import SidebarItem from './SidebarItem.vue'
import logo from '@/assets/logo.png'
import SvgIcon from '@/components/SvgIcon.vue'

const sidebarLabels = ['Dashboard', 'Tests', 'Cats', 'Sandbox']
const sidebarRouters = ['dashboard', 'tests', 'tests', 'sandbox']
const sidebarIcons = ['ChartPie', 'Collection', 'ChevronRight', 'ChevronRight']

const router = useRouter()

function goBack() {
  router.back()
}
</script>

<style>
@layer components {
  .sidebar-menu {
    @apply bg-blue-400 w-full h-full overflow-x-hidden pt-3 rounded-tr-3xl
  }
}
</style>
