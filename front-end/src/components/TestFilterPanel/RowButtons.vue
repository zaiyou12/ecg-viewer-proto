<template>
  <div class="flex justify-evenly">
    <button
      v-for="(label, idx) in labels"
      :key="idx"
      class="row-btn-base"
      :class="{
        'border-l-2 border-r rounded-l-md': whichTypeBtn(idx) < 0,
        'border-l border-r': whichTypeBtn(idx) === 0,
        'border-l border-r-2 rounded-r-md': whichTypeBtn(idx) > 0,
        'bg-blue-400 text-white font-bold': isSelected(label),
        'capitalize': type === 'condition'
      }"
      @click="clicked(label)"
    >{{ label }}</button>
  </div>
</template>

<script setup lang="ts">
import useTestsStore from '../../stores/test-list'

const props = defineProps<{
  /* Only works for 1 < labels.length !!!!!! */
  labels: string[] | number[]
  type: 'duration' | 'region' | 'condition'
}>()

const store = useTestsStore()

/* left: -1, middle: 0, right: 1 */
function whichTypeBtn(idx: number): number {
  const len = props.labels.length
  if (idx === 0) return -1
  if (idx === len - 1) return 1
  return 0
}

function isSelected(x: number | string) {
  switch (props.type) {
    case 'duration':
      return store.duration.includes(x as EcgTest.Duration)
    case 'region':
      return store.region.includes(x as EcgTest.Region)
    case 'condition':
      return store.condition.includes(x as EcgTest.ConditionType)
  }
}

function clicked(x: number | string) {
  switch (props.type) {
    case 'duration':
      store.toggleDuration(x as EcgTest.Duration)
      break
    case 'region':
      store.toggleRegion(x as EcgTest.Region)
      break
    case 'condition':
      store.toggleCondition(x as EcgTest.ConditionType)
      break
  }
}
</script>

<style>
@layer components {
  .row-btn-base {
    @apply w-1/2 h-8 border-t-2 border-b-2 border-blue-300 text-sm
    hover:bg-blue-300;
  }

  .capitalize::first-letter {
    text-transform: uppercase;
  }
}
</style>
