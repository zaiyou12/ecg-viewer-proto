<template>
<transition name="fade" appear>
  <div v-if="showPanel" class="panel-overlay">
    <div class="w-full h-full px-5 pt-2 pb-3 flex flex-col justify-evenly">
      <ButtonFilter heading="Duration" :options="durations" />
      <ButtonFilter heading="Region" :options="regions" />
      <DropdownFilter heading="Test Group" :options="sampleGroups" />
      <ButtonFilter heading="Final Status" :options="normals" />
    </div>
  </div>
</transition>
</template>

<script setup lang="ts">
import ButtonFilter from './ButtonFilter.vue'
import DropdownFilter from './DropdownFilter.vue'


const props = defineProps<{
  showPanel: boolean
}>()

const emits = defineEmits<{
  (e: 'update:showPanel', value: boolean): void
}>()

const durations = [24, 48, 72]
const regions = ['KR', 'AU', 'UK', 'N/A']
const sampleGroups = ['Group 1', 'Group 2', 'Group 3']
const normals = ['Normal', 'Abnormal', 'Unknown']
</script>

<style>
@layer components {
  .panel-overlay {
    z-index: 98;
    @apply absolute w-80 h-72 rounded-3xl
    transform translate-x-10 translate-y-20
    bg-white shadow-2xl
    border-2 border-blue-50
    overflow-x-hidden overflow-y-auto overscroll-none
  }

  .fade-enter-active {
    @apply transition-opacity duration-300 ease-out
  }

  .fade-leave-active {
    @apply transition-opacity duration-300
  }

  .fade-enter-from, .fade-leave-to {
    @apply opacity-0
  }
}
</style>
