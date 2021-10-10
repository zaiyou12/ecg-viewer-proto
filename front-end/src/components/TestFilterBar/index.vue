<template>
  <div class="flex h-28 items-center">
    <div class="flex-none w-1/2 flex justify-start">
      <FilterButton class="ml-10" />
    </div>
    <div class="flex-none w-1/2 flex justify-end" @click="disablePanel">
      <SearchBar class="mr-10" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { inject } from 'vue'
import FilterButton from './FilterButton.vue'
import SearchBar from './SearchBar.vue'
import { DisablePanelKey } from '../../symbols/symbols';


const disablePanel = inject(DisablePanelKey)
</script>
