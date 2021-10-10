<template>
  <div>
    <p class="text-sm font-bold flex mb-1">{{ heading }}</p>
    <select v-model="selected" class="dropdown-filter-select" >
      <option value="">--Please choose an option--</option>
      <option v-for="(opt, idx) in options" :key="idx"
        :value="opt"
      >
        {{ opt }}
      </option>
    </select>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'


const props = defineProps<{
  heading: string
  options: string[]
}>()

const selected = ref('')
watch(selected, () => {
  console.log(selected.value)
})
</script>

<style>
@layer components {
  .dropdown-filter-select {
    @apply w-full h-8 border-2 border-blue-200 rounded-lg
      px-2 text-sm cursor-pointer
      focus:outline-none focus:bg-blue-100
  }
}
</style>
