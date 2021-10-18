<template>
  <div class="flex h-16 items-center border-b-2 mx-5 border-gray-100 cursor-default">
    <div class="text-2xl font-bold pl-5">
      Test Groups
    </div>
    <div class="text-sm ml-5">
      Add or remove test groups
    </div>
  </div>
  <div class="px-10 my-5 cursor-default">
    <div class="text-left font-bold">
      List of Test Groups
    </div>
  </div>
  <TestGroupList />
  <!-- <ul>
    <li v-for="(g, idx) in store.testGroups" :key="idx">
      {{ g }}
    </li>
  </ul>

  <div>
    <p>
      New Test Group Name:
    </p>
    <input type="text" class="border-2" v-model="newGroupName">
  </div>

  <div>
    <p>
      New Test Group Description:
    </p>
    <input type="text" class="border-2" v-model="newGroupDesc">
  </div>
  <button class="border-2 hover:bg-blue-50"
    @click="store.addTestGroup(newGroupName, newGroupDesc)"
  >
    Add Test Group
  </button>

  <div>
    <p>
      Delete Test Group ID:
    </p>
    <input type="text" class="border-2" v-model="delTestGroupId">
  </div>
  <button class="border-2 hover:bg-blue-50"
    @click="store.delTestGroup(delTestGroupId)"
  >
    Delete Test Group
  </button> -->
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
