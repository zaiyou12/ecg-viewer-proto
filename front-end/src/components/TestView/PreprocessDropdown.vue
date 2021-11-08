<template>
  <transition name="drop" appear>
    <div v-if="showDrop" class="drop-overlay">
      <ul class="select-none">
        <li
          v-for="(g, idx) in lakeStore.preprocessGroups"
          :key="idx"
          class="flex items-center h-8 cursor-pointer hover:bg-blue-50"
          @mouseup="preprocessSelected(g.id)"
        >
          <div
            class="w-4 h-4 flex-none mx-2 border-2 rounded-lg border-gray-400"
            :class="{ 'bg-gray-500': viewStore.pid === g.id }"
            :key="idx"
          ></div>
          <div
            class="h-full flex flex-col justify-center pr-2 hover:bg-blue-50"
          >{{ g.groupName }}</div>
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

async function preprocessSelected(pid: number) {
  if (viewStore.pid === pid) viewStore.pid = undefined
  else viewStore.pid = pid
  await viewStore.getStrips()
}
</script>
