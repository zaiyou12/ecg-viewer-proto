<template>
  <div class="flex h-28 items-center w-full">
    <div class="flex-none w-2/3">
      <div class="flex justify-center">
        <button
          class="bg-white ring ring-blue-200 px-3 py-1 mx-5 rounded-full text-sm"
          v-for="(label, index) in buttonLabels"
          :key="index"
        >
          {{ label }}
        </button>
      </div>
    </div>
    <div class="flex-none w-1/3">
      <div class="flex items-center justify-left w-full">
        <SvgIcon name="Search" class="h-5 w-5"/>
        <input
          type="search"
          :placeholder="placeholder"
          class="w-1/2 bg-blue-50 text-lg rounded-lg h-9 p-2 mx-2 focus:outline-none focus:ring focus:ring-blue-300"
        >
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import SvgIcon from '@/components/SvgIcon.vue'

const buttonLabels = ['Region', 'Duration', 'Normal', 'Sample Group']
const placeholder = 'aaa'
</script>
