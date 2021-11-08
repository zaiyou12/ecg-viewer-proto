<template>
  <!-- TODO: Remove this navigation guard later -->
  <li v-if="routerName === 'preprocess'" class="sidebar-item-disabled">
    <div class="flex items-center text-white">
      <SvgIcon :name="icon" class="h-6 w-6 mx-2" />
      <p class="text-l font-bold">{{ label }}</p>
    </div>
  </li>
  <li v-else @click="routeTo" class="sidebar-item">
    <div class="flex items-center text-white">
      <SvgIcon :name="icon" class="h-6 w-6 mx-2" />
      <p class="text-l font-bold">{{ label }}</p>
    </div>
  </li>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import useTestsStore from '../../stores/test-list'
import useGroupPageStore from '../../stores/group-page'

const props = defineProps<{
  label: string
  routerName: string
  icon: string
}>()

const router = useRouter()
const testStore = useTestsStore()
const groupStore = useGroupPageStore()

async function routeTo() {
  // TODO: Remove after api for preprocess has been fixed
  if (props.routerName === 'preprocess') {
    return
  }
  router.push({ name: props.routerName })
  if (props.routerName === 'tests') {
    testStore.resetAllParams()
    await testStore.getTestList()
  } else if (props.routerName === 'testGroup') {
    await groupStore.updateGroupInfo('t')
  } else if (props.routerName === 'sampleGroup') {
    await groupStore.updateGroupInfo('s')
  }
}
</script>

<style>
@layer components {
  .sidebar-item {
    @apply h-10 cursor-pointer py-2 my-2
      hover:bg-blue-600 rounded-lg;
  }
  .sidebar-item-disabled {
    @apply h-10 cursor-not-allowed py-2 my-2
      rounded-lg;
  }
}
</style>
