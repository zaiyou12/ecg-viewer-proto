<template>
  <div class="flex h-28 items-center w-full">
    <div class="flex-none w-1/2 align-middle">
      <div class="flex justify-left ml-10">
        <button class="border-2 rounded-md border-gray-200 py-1 px-2 focus:border-blue-300">
          <div class="flex items-center font-bold">
            <SvgIcon name="Adjustments" class="h-5 w-5 mr-1"/>
            Filter
          </div>
        </button>
      </div>
    </div>
    <div class="flex-none w-1/2">
      <div class="flex items-center justify-center w-full">
        <SvgIcon name="Search" class="h-5 w-5"/>
        <input
          type="search"
          :placeholder="placeholder"
          :value="searchInput"
          @keyup.enter="emitSearchInput"
          class="w-1/2 bg-blue-50 rounded-lg h-9 px-3 pt-2 pb-1 mx-2 focus:outline-none focus:ring focus:ring-blue-300"
        >
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import SvgIcon from '@/components/SvgIcon.vue'


const props = defineProps<{
  searchInput: string
}>()

const emits = defineEmits<{
  (e: 'update:searchInput', searchInput: string): void
}>()

const placeholder = 'Search by test sequence'

function emitSearchInput(e: Event) {
  const newSearchInput = (e.target as HTMLTextAreaElement).value
  emits('update:searchInput', newSearchInput)
}
</script>
