<template>
  <div class="flex h-28 items-center w-full">
    <div class="flex-none w-1/2 align-middle">
      <FilterButton />
    </div>
    <div class="flex-none w-1/2">
      <div class="flex items-center justify-center w-full">
        <SvgIcon name="Search" class="h-5 w-5"/>
        <input
          type="search"
          :placeholder="placeholder"
          :value="searchInput"
          @keyup.enter="emitSearchInput"
          class="test-search-bar"
        >
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import FilterButton from './FilterButton.vue'


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

<style>
@layer components {
  .test-search-bar {
    @apply w-1/2 bg-blue-100 rounded-lg h-9
    px-3 pt-2 pb-1 mx-2 focus:outline-none
    focus:ring focus:ring-blue-300
    hover:bg-blue-50
    focus:bg-blue-100
  }
}
</style>
