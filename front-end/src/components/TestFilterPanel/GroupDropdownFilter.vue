<template>
  <div>
    <p class="text-sm font-bold flex mb-1">{{ heading }}</p>
    <select v-model="selected" class="dropdown-filter-select">
      <option selected value="-1">--Please choose an option--</option>
      <option
        v-for="(opt, idx) in options"
        :key="idx"
        :value="opt.id"
      >{{ opt.displayName }}</option>
    </select>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import useTestsStore from '../../stores/test-list'

const props = defineProps<{
  heading: string
  options: TestGroups | SampleGroups | PreprocessGroups
}>()

const store = useTestsStore()

const selected = ref(-1)
watch(selected, () => {
  if (selected.value < 0) {
    store.testGroup = undefined
  } else {
    store.testGroup = selected.value
  }
})
</script>

<style>
@layer components {
  .dropdown-filter-select {
    @apply w-full h-8 border-2 border-blue-300 rounded-lg
      px-2 text-sm cursor-default
      hover:bg-blue-300
      focus:outline-none;
  }
}
</style>
