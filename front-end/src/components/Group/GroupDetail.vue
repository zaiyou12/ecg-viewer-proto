<template>
  <div class="flex flex-col select-none">
    <div class="text-left text-sm flex mb-2 px-5 font-bold">
      <p class="mr-5">Group ID #{{ store.selectedGroupId }}</p>
      <p>{{ store.selectedGroupName }}</p>
    </div>
    <div class="group-modify-bar">
      <div>
        <label class="mr-2 font-bold">Test Seq:</label>
        <input type="text" placeholder="ex) 0001" />
        <button class="cursor-not-allowed">Add</button>
      </div>
      <button @mouseup="deleteCheckedFromGroup">Delete</button>
    </div>
    <GroupTestList />
  </div>
</template>

<script setup lang="ts">
import GroupTestList from '@/components/Group/GroupTestList.vue'
//@ts-ignore
import useGroupPageStore from '@/stores/group-page'

const store = useGroupPageStore()

async function deleteCheckedFromGroup() {
  await store.toggleGroupChange()
}
</script>

<style>
@layer components {
  .group-modify-bar {
    @apply h-16 mb-2 px-5 border
    flex items-center justify-around;
  }
  .group-modify-bar input {
    @apply h-8 mr-2 px-2 py-1 text-sm
    outline-none bg-blue-100 rounded-lg
    focus:bg-blue-100 hover:bg-blue-50;
  }
  .group-modify-bar button {
    @apply border-0 h-8 w-16 px-2 rounded-lg
    bg-blue-400 hover:bg-blue-300
    text-white font-bold;
  }
}
</style>
