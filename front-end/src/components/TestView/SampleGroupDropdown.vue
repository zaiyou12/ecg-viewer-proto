<template>
  <transition name="drop" appear>
    <div v-if="showDrop" class="drop-overlay">
      <ul class="select-none">
        <li
          v-for="(g, idx) in lakeStore.sampleGroups"
          :key="idx"
          class="flex items-center h-8 cursor-pointer hover:bg-blue-50"
          @mouseup="sampleSelected(g)"
        >
          <div
            class="w-4 h-4 flex-none mx-2 border-2 rounded-lg border-gray-400"
            :class="{ 'bg-gray-500': belongsInGroup(g.id) }"
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

function belongsInGroup(gid: number): boolean {
  return gid in viewStore.sampleGroup!
}

async function sampleSelected(g: SampleGroup) {
  await viewStore.toggleSingleGroup('s', g.id, g.groupName, !belongsInGroup(g.id))
}
</script>
