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
        class="cursor-pointer bg-blue-300 py-3 mb-5 text-white font-bold hover:bg-blue-200"
        @click="goBack()"
      >
        &lt; Go Back
      </div>
      <ul class="px-5">
        <SidebarItem
          v-for="(label, index) in sidebarLabels"
          :key="index"
          :sidebarLabel="label"
          :sidebarRouter="sidebarRouters[index]"
        />
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import { getCurrentInstance } from 'vue'
import SidebarItem from './SidebarItem.vue'
import logo from '@/assets/logo.png'

const sidebarLabels = ['Dashboard', 'Tests', 'Cats', 'Dogs']
const sidebarRouters = ['dashboard', 'tests', 'tests', 'tests']

const instance = getCurrentInstance()

function goBack() {
  instance!.appContext.config.globalProperties.$router.back()
}
</script>

<style>
@layer components {
  .sidebar-menu {
    @apply bg-blue-400 w-full h-full overflow-x-hidden pt-3 rounded-tr-lg
  }
}
</style>
