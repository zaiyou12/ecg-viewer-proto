<template>
  <div class="flex flex-col">
    <div class="text-left text-sm flex mb-2">
      <p class="mr-5">Group ID #{{ store.selectedGroupId }}</p>
      <p>{{ store.selectedGroupName }}</p>
    </div>
    <div class="h-16 border mb-2 flex items-center">
      <label>Test</label>
      <input type="text" class="border h-8" />
      <button class="border">Add</button>
      <button class="border">Delete</button>
      <div>
        <button class="border">Confirm</button>
        <button class="border">Cancel</button>
      </div>
    </div>
    <GroupTestList />
  </div>
</template>

<script setup lang="ts">
import GroupTestList from '@/components/Group/GroupTestList.vue'
//@ts-ignore
import useGroupPageStore from '@/stores/group-page'

const store = useGroupPageStore()
</script>
