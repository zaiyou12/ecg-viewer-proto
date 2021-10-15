<template>
  <button class="flex items-center p-1 rounded-lg bg-blue-100 hover:bg-blue-50"
    @click="type === 'left' ? viewStore.getPrevStrips() : viewStore.getNextStrip()"
  >
    <p v-if="type === 'right'" class="pl-1">Next Strips</p>
    <SvgIcon :name="buttonTypeMap[type]" class="w-5 h-5" :strokeWidth="3" />
    <p v-if="type === 'left'" class="pr-1">Prev Strips</p>
  </button>
</template>

<script setup lang="ts">
import useTestViewStore from '../../stores/test-view'


const props = defineProps<{
  type: 'left' | 'right'
}>()

const viewStore = useTestViewStore()

const buttonTypeMap = {
  'left': 'ChevronLeft',
  'right': 'ChevronRight'
}
</script>
