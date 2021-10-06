<template>
  <div class="flex h-28 items-center w-full">
    <div class="flex-none w-1/2 align-middle">
      <div class="flex justify-left ml-10">
        <button class="border-2 rounded-md border-gray-200 py-1 px-2">
          <div class="flex items-center">
            <SvgIcon name="Adjustments" class="h-5 w-5 mr-1"/>
            Filter
          </div>
        </button>
      </div>
      <!-- <div class="flex justify-center">
        <button
          class="bg-white ring ring-blue-200 px-3 py-1 mx-5 rounded-full text-sm"
          v-for="(label, index) in buttonLabels"
          :key="index"
        >
          {{ label }}
        </button> -->
      <!-- </div> -->
    </div>
    <div class="flex-none w-1/2">
      <div class="flex items-center justify-center w-full">
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
