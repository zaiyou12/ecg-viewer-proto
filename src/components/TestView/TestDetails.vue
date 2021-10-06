<template>
  <div class="my-1 py-5 border-2 border-red-400">
    Test info - {{ testSeq }}
  </div>
  <div class="flex justify-around">
    <button class="my-4 bg-blue-200">
      Add to Preprocess Group
    </button>
    <button class="my-4 bg-blue-200">
      Add to Test Group
    </button>
    <button class="my-4 bg-blue-200">
      Add Sample to Test
    </button>
  </div>
  <div class="mt-5 text-left mx-10 font-bold">60s Strips</div>
  <div>
    <Strip
      v-for="index in numStrips"
      :key="index"
    />
  </div>
  <div class="my-4">
    &lt;&lt; Prev | Next &gt;&gt;
  </div>
</template>

<script setup lang="ts">
import Strip from '@/components/Strip60s.vue'

const props = defineProps<{
  testSeq: string
  testInfo?: any
}>()

const numStrips = 6
</script>
