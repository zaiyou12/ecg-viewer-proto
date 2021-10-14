<template>
  <transition name="drop" appear>
    <div v-if="showDrop" class="drop-overlay">
      <ul class="select-none">
        <li v-for="(g, idx) in whichGroup()" :key="idx"
          class="flex items-center h-8 cursor-pointer hover:bg-blue-50"
          @mouseup="groupSelected(g)"
        >
          <div class="w-4 h-4 flex-none mx-2 border-2 rounded-lg border-gray-400"
            :class="{'bg-gray-500': testBelongsInGroup(g.id)}" :key="idx"
          ></div>
          <div class="h-full flex flex-col justify-center pr-2 hover:bg-blue-50">
            {{ g.displayName }}
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

function whichGroup() {
  if (props.type === 'Preprocess') return lakeStore.preprocessGroups
  if (props.type === 'Test') return lakeStore.testGroups
  else return lakeStore.sampleGroups
}

function testBelongsInGroup(gid: number): boolean {
  if (props.type === 'Preprocess') return false
  if (props.type === 'Test') return viewStore.selectedTest!.tGroup.includes(gid)
  else return viewStore.selectedTest!.sGroup.includes(gid)
}

function groupSelected(group: PreprocessGroup | TestGroup | SampleGroup): void {
  if (props.type === 'Test') {
    const g = group as TestGroup
    if (testBelongsInGroup(g.id)) {
      viewStore.delTestGroupFromTest(g.id)
      lakeStore.delTestSeqFromTestGroup(g.id, viewStore.selectedTest!.testSeq)
    }
    else {
      viewStore.addTestGroupToTest(g.id)
      lakeStore.addTestSeqToTestGroup(g.id, viewStore.selectedTest!.testSeq)
    }
  }
  // TODO: Change after modying strip logic
  if (props.type === 'Sample') {
    const g = group as SampleGroup
    if (testBelongsInGroup(g.id)) {
      // viewStore.delSampleGroupFromTest(g.id)
    }
    else {
      // viewStore.addSampleGroupToTest(g.id)
    }
  }
}
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
