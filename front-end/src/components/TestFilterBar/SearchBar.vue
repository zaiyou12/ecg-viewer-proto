<template>
  <div class="flex items-center w-2/3">
    <SvgIcon name="Search" class="h-5 w-5" :strokeWidth="3"/>
    <input :placeholder="placeholder" class="test-search-bar"
      :value="query"
      @focus="clearSearchBar"
      @keyup.enter="pressedEnter"
    >
  </div>
</template>

<script setup lang="ts">
import { inject, ref } from 'vue'
// @ts-ignore
import { QueryKey, StringSetterFunc, UpdateQueryKey } from '@/symbols/symbols'


const query = inject(QueryKey, ref(''))
const updateQuery: StringSetterFunc = inject(UpdateQueryKey)
const placeholder = 'Search by test sequence'

function pressedEnter(e: Event) {
  const typed = (e.target as HTMLTextAreaElement).value
  updateQuery(typed)
}

function clearSearchBar(e: Event) {
  (e.target as HTMLTextAreaElement).value = ''
}
</script>

<style>
@layer components {
  .test-search-bar {
    @apply bg-blue-100 rounded-lg h-9 w-full
    px-3 pt-2 pb-1 ml-2 focus:outline-none
    /* focus:ring focus:ring-blue-300 */
    hover:bg-blue-50
    focus:bg-blue-100
  }
}
</style>
