<template>
  <p>This is a sample group page.</p>
  <ul>
    <li v-for="(g, idx) in store.sampleGroups" :key="idx">
      {{ g }}
    </li>
  </ul>

  <div>
    <p>
      Sample Group Name:
    </p>
    <input type="text" class="border-2" v-model="newGroupName">
  </div>

  <div>
    <p>
      Sample Group Description:
    </p>
    <input type="text" class="border-2" v-model="newGroupDesc">
  </div>

  <button class="border-2 hover:bg-blue-50"
    @click="store.addSampleGroup(newGroupName, newGroupDesc)"
  >
    Add Sample Group
  </button>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import useDataLakeStore from '../stores/data-lake'

const store = useDataLakeStore()
const newGroupName = ref('')
const newGroupDesc = ref('')
</script>
