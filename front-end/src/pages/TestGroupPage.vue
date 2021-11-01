<template>
  <PageHeader>
    <div class="text-2xl font-bold pl-5">Test Groups</div>
    <div class="text-sm ml-5">Add or remove test groups</div>
    <div>
      <button class="mx-5 group-modify-btn">
        <SvgIcon class="h-5 w-5" name="PlusSm" />
      </button>
      <button class="group-modify-btn">
        <SvgIcon class="h-5 w-5" name="MinusSm" />
      </button>
    </div>
  </PageHeader>
  <TestGroupList class="mb-5 pt-16" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
import TestGroupList from '@/components/TestGroup/TestGroupList.vue'
import PageHeader from '@/components/PageHeader.vue'
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
