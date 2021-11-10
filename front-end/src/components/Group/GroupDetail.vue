<template>
  <div class="flex flex-col select-none">
    <div class="text-left text-sm flex mb-2 px-5 font-bold">
      <p class="mr-5">Group ID #{{ groupStore.selectedGroupId }}</p>
      <p>{{ groupStore.selectedGroupName }}</p>
    </div>
    <div class="group-modify-bar">
      <div>
        <label class="mr-2 font-bold">Test Seq:</label>
        <input type="text" placeholder="ex) 0001" />
        <button
          class="cursor-not-allowed"
          :class="{ 'disabled': !isGroupOpen }"
        >Add</button>
      </div>
      <button
        @mouseup="deleteCheckedFromGroup"
        :class="{ 'disabled': !isGroupOpen || !groupStore.isSomethingChecked }"
      >Delete</button>
    </div>
    <GroupTestList />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import GroupTestList from '@/components/Group/GroupTestList.vue'
import useGroupPageStore from '../../stores/group-page'
import useDataLakeStore from '../../stores/data-lake'

const groupStore = useGroupPageStore()
const lakeStore = useDataLakeStore()

const isGroupOpen = computed(() => {
  const group = lakeStore.getGroup(groupStore.type!) as TestGroups | SampleGroups
  return group[groupStore.selectedGroupId!].groupStatus === 'open'
})

async function deleteCheckedFromGroup() {
  await groupStore.toggleGroupChange()
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
  .group-modify-bar button.disabled {
    pointer-events: none;
    @apply bg-gray-400;
  }
}
</style>
