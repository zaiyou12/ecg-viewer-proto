<template>
  <li @click="routeTo" class="sidebar-item">
    <div class="flex items-center text-white">
      <SvgIcon :name="icon" class="h-6 w-6 mx-2" />
      <p class="text-l font-bold">{{ label }}</p>
    </div>
  </li>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import useTestsStore from '../../stores/test-list'

const props = defineProps<{
  label: string
  router: string
  icon: string
}>()

const router = useRouter()
const store = useTestsStore()

async function routeTo() {
  router.push({ name: props.router })
  if (props.label === 'Tests') {
    store.resetAllParams()
    await store.fetchEcgTests()
  }
}
</script>

<style>
@layer components {
  .sidebar-item {
    @apply h-10 cursor-pointer py-2 my-2
      hover:bg-blue-600 rounded-lg;
  }
}
</style>
