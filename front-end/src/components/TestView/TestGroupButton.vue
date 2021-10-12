<template>
  <div class="test-group-btn" @click="$emit('update:showDrop', !showDrop)">
    <div>
      {{ type }}
    </div>
    <SvgIcon name="ChevronDown" class="w-5 h-5 ml-2" />
  </div>
</template>

<script lang="ts" setup>
import TestGroupDropdown from './TestGroupDropdown.vue'

const props = defineProps<{
  type: 'Preprocess' | 'Test' | 'Sample'
  showDrop: boolean
}>()

// const emits = defineEmits<{
//   (e: 'update:showDrop', val: boolean): void
// }>()
</script>

<style>
@layer components {
  .test-group-btn {
    @apply flex items-center
    mx-2 p-2 justify-between cursor-pointer
    bg-gray-50 rounded-lg
    select-none
  }
}
</style>
