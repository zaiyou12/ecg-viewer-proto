<template>
  <transition name="drop" appear>
    <div v-if="showDrop" class="drop-overlay">
      <ul class="select-none">
        <li v-for="(g, idx) in whichGroup(type)" :key="idx"
          class="flex items-center h-8 hover:bg-blue-50"
        >
          <input type="checkbox" :id="`group${type+g.id}`"
            class="mx-2 h-full hover:bg-blue-50"
            :checked="testBelongsInGroup(type, g.id)"
          >
          <div class="h-full w-full flex items-center hover:bg-blue-50" >
            <label :for="`group${type+g.id}`" class="text-left w-full whitespace-nowrap">
              {{ g.displayName }}
            </label>
          </div>
        </li>
      </ul>
    </div>
  </transition>
</template>

<script lang="ts" setup>
import useDataLakeStore from '../../stores/data-lake'
import useTestViewStore from '../../stores/test-view'


const props = defineProps<{
  type: 'Preprocess' | 'Test' | 'Sample'
  showDrop: boolean
}>()

const lakeStore = useDataLakeStore()
const viewStore = useTestViewStore()

function whichGroup(groupType: 'Preprocess' | 'Test' | 'Sample') {
  if (groupType === 'Preprocess') return lakeStore.preprocessGroups
  if (groupType === 'Test') return lakeStore.testGroups
  else return lakeStore.sampleGroups
}

function testBelongsInGroup(groupType: 'Preprocess' | 'Test' | 'Sample', id: number): boolean {
  if (groupType === 'Preprocess') return false
  if (groupType === 'Test') return id in viewStore.selectedTest!.tGroup
  else return id in viewStore.selectedTest!.sGroup
}

// function groupChecked(idx: number) {
//   (document.getElementById(`group${idx}`) as HTMLInputElement).checked = !(document.getElementById(`group${idx}`) as HTMLInputElement).checked
// }
</script>

<style>
@layer components {
  .drop-overlay {
    width: 14.8%;
    z-index: 98;
    @apply absolute h-40 ml-2
      overflow-auto overscroll-none
    bg-gray-50 rounded-xl
  }

  .drop-enter-active {
    @apply transition-opacity duration-200 ease-out

  }

  .drop-leave-active {
    @apply transition-opacity duration-200
  }

  .drop-enter-from, .drop-leave-to {
    @apply opacity-0
  }
}
</style>
