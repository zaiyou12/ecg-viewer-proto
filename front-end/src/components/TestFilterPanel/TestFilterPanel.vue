<template>
  <transition name="fade" appear>
    <div v-if="showPanel" class="panel-overlay">
      <div class="w-full h-5/6 px-5 pt-2 pb-3 flex flex-col justify-evenly">
        <ButtonFilter
          heading="Duration"
          :options="lakeStore.durations"
          type="duration"
        />
        <ButtonFilter
          heading="Region"
          :options="lakeStore.regions"
          type="region"
        />
        <DropdownFilter heading="Test Group" :options="lakeStore.testGroups" />
        <ButtonFilter
          heading="Condition"
          :options="lakeStore.conditions"
          type="condition"
        />
      </div>
      <div class="flex justify-around reset-confirm-btn">
        <button @click="listStore.resetFilters()">Reset</button>
        <button @click="confirm">Confirm</button>
      </div>
    </div>
  </transition>
</template>

<script setup lang="ts">
import useTestsStore from '../../stores/test-list'
import useDataLakeStore from '../../stores/data-lake'
import ButtonFilter from './ButtonFilter.vue'
import DropdownFilter from './GroupDropdownFilter.vue'

const props = defineProps<{
  showPanel: boolean
}>()

const emits = defineEmits<{
  (e: 'update:showPanel', value: boolean): void
}>()

const listStore = useTestsStore()
const lakeStore = useDataLakeStore()

async function confirm() {
  listStore.page = 1
  await listStore.fetchEcgTests()
  emits('update:showPanel', false)
}
</script>

<style>
@layer components {
  .panel-overlay {
    z-index: 98;
    height: 21rem;
    @apply absolute w-80 rounded-3xl
    transform translate-x-10 translate-y-20
    bg-white shadow-2xl
    border-2 border-blue-50
    overflow-x-hidden overflow-y-auto overscroll-none;
  }

  .fade-enter-active {
    @apply transition-opacity duration-300 ease-out;
  }

  .fade-leave-active {
    @apply transition-opacity duration-300;
  }

  .fade-enter-from,
  .fade-leave-to {
    @apply opacity-0;
  }

  .reset-confirm-btn button {
    @apply bg-blue-400 rounded-lg py-1 w-20
    font-bold text-white
    hover:bg-blue-300;
  }
}
</style>
