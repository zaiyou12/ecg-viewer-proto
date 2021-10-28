<template>
  <div
    class="flex h-16 items-center border-b-2 mx-5 border-gray-100 cursor-default"
  >
    <div class="text-2xl font-bold pl-5">Test Groups</div>
    <div class="text-sm ml-5">Add or remove test groups</div>
  </div>
  <div class="px-10 my-5 cursor-default">
    <div class="flex items-center">
      <div class="text-left font-bold">List of Test Groups</div>
      <div>
        <button class="mx-5 group-modify-btn">
          <SvgIcon class="h-5 w-5" name="PlusSm" />
        </button>
        <button class="group-modify-btn">
          <SvgIcon class="h-5 w-5" name="MinusSm" />
        </button>
      </div>
    </div>
  </div>
  <TestGroupList class="mb-5" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
import TestGroupList from '@/components/TestGroup/TestGroupList.vue'
import useDataLakeStore from '../stores/data-lake'

const store = useDataLakeStore()
const newGroupName = ref('')
const newGroupDesc = ref('')
const delTestGroupId = ref(0)
</script>

<style>
@layer components {
  .group-modify-btn {
    @apply px-1 py-1 rounded-lg
    bg-blue-400 text-white font-bold
    hover:bg-blue-300;
  }
}
</style>
