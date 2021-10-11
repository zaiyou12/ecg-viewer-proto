<template>
  <div>
    <div class="flex items-baseline">
      <div class="mt-5 mb-1 text-left mx-14 font-bold">Details</div>
      <div class="text-sm mr-10">Recording Start Time: 2021-10-31:00:00:00</div>
      <div class="text-sm mr-10">Actual Duration: 12:29:32</div>
      <div class="text-sm">And Something Else: That I can't think of</div>
    </div>
    <div class="mt-5 mb-1 text-left mx-14 font-bold">60s Strips</div>
    <div>
      <Strip
        v-for="index in numStrips"
        :key="index"
        :type="`g${index}`"
      />
    </div>
    <div class="my-4 h-16">
      &lt;&lt; Prev | Next &gt;&gt;
    </div>
  </div>
</template>

<script setup lang="ts">
import Strip from '@/components/Strip60s.vue'

// const props = defineProps<{
//   testSeq: string
//   testInfo?: any
// }>()

const numStrips = 6
</script>
