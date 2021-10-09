<template>
  <div class="flex justify-evenly">
    <button v-for="(label, idx) in labels" :key="idx" class="row-btn-base"
      :class="{
        'border-l-2 border-r rounded-l-md': whichTypeBtn(idx) < 0,
        'border-l border-r': whichTypeBtn(idx) === 0,
        'border-l border-r-2 rounded-r-md': whichTypeBtn(idx) > 0
      }"
      @click="log(label)"
    >
      {{ label }}
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'


const props = defineProps<{
  /* Only works for 1 < labels.length !!!!!! */
  labels: Array<number | string>
}>()

/* left: -1, middle: 0, right: 1 */
function whichTypeBtn(idx: number): number {
  const len = props.labels.length
  if (idx === 0) return -1
  if (idx === len-1) return 1
  return 0
}

function log(x: number | string) {
  console.log(x)
}
</script>

<style>
@layer components {
  .row-btn-base {
    @apply w-1/2 h-8 border-t-2 border-b-2 border-blue-200
    hover:bg-blue-50 text-sm focus:bg-blue-100
  }
}
</style>
