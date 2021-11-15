<template>
  <transition name="drop" appear>
    <div v-if="showDrop" class="drop-overlay">
      <ul class="select-none">
        <li
          v-for="(g, idx) in groupList"
          :key="idx"
          :class="(g as TestGroup | SampleGroup).groupStatus"
          @mouseup="groupSelected(g)"
        >
          <div
            class="drop-item-circle"
            :class="{ 'bg-gray-500': belongsInGroup(g.id) }"
            :key="idx"
          ></div>
          <div class="drop-item-label">{{ g.groupName }}</div>
        </li>
      </ul>
    </div>
  </transition>
</template>

<script lang="ts" setup>
import { computed, toRef } from 'vue'
import useDataLakeStore from '../../stores/data-lake'
import useTestViewStore from '../../stores/test-view'

const props = defineProps<{
  showDrop: boolean
  type: 't' | 's'
}>()

const lakeStore = useDataLakeStore()
const viewStore = useTestViewStore()

const groupVarName = computed(() => {
  return props.type === 't' ? 'testGroups' : 'sampleGroups'
})
const groupList = toRef(lakeStore, groupVarName.value)
const memberGroups = toRef(viewStore, groupVarName.value)

function belongsInGroup(gid: number): boolean {
  return gid in memberGroups.value!
}

async function groupSelected(g: TestGroup): Promise<void> {
  await viewStore.toggleSingleGroup(
    props.type,
    g.id,
    g.groupName,
    !belongsInGroup(g.id)
  )
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
  .drop-overlay li {
    @apply flex items-center h-8 cursor-pointer
    hover:bg-blue-50;
  }
  .drop-overlay li.closed {
    pointer-events: none;
    @apply bg-gray-100 text-gray-500;
  }
  .drop-overlay li div.drop-item-circle {
    @apply w-4 h-4 flex-none mx-2 border-2 rounded-lg
    border-gray-400;
  }
  .drop-overlay li div.drop-item-label {
    @apply h-full flex flex-col justify-center pr-2
    hover:bg-blue-50;
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
