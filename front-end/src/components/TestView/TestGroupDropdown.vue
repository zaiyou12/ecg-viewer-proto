<template>
  <transition name="drop" appear>
    <div v-if="showDrop" class="drop-overlay">
      <ul class="select-none">
        <li
          v-for="(g, idx) in lakeStore.testGroups"
          :key="idx"
          class="flex items-center h-8 cursor-pointer hover:bg-blue-50"
          @mouseup="groupSelected(g)"
        >
          <div
            class="w-4 h-4 flex-none mx-2 border-2 rounded-lg border-gray-400"
            :class="{ 'bg-gray-500': belongsInGroup(g.id) }"
            :key="idx"
          ></div>
          <div
            class="h-full flex flex-col justify-center pr-2 hover:bg-blue-50"
          >{{ g.displayName }}</div>
        </li>
      </ul>
    </div>
  </transition>
</template>

<script lang="ts" setup>
import useDataLakeStore from '../../stores/data-lake'
import useTestViewStore from '../../stores/test-view'

const props = defineProps<{
  showDrop: boolean
}>()

const lakeStore = useDataLakeStore()
const viewStore = useTestViewStore()

function belongsInGroup(gid: number): boolean {
  return gid in viewStore.testGroup!
}

async function groupSelected(g: TestGroup): Promise<void> {
  if (belongsInGroup(g.id)) {
    await viewStore.delFromTestGroup(g.id)
  } else {
    await viewStore.addToTestGroup(g.id, g.displayName)
  }
}
</script>

<style>
@layer components {
  .drop-overlay {
    width: calc(50% / 3 - 1.5rem);
    z-index: 98;
    @apply absolute h-40 ml-2
      overflow-auto overscroll-none
    bg-gray-50 rounded-xl;
  }

  .drop-enter-active {
    @apply transition-opacity duration-200 ease-out;
  }

  .drop-leave-active {
    @apply transition-opacity duration-200;
  }

  .drop-enter-from,
  .drop-leave-to {
    @apply opacity-0;
  }
}
</style>
