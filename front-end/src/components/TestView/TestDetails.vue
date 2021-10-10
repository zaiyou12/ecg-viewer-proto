<template>
  <div>
    <div class="mt-5 mb-1 text-left mx-14 font-bold">Details</div>
    <div class="flex justify-around mx-14 py-10 border">
      <div>
        Details
      </div>
    </div>
    <div class="mt-5 mb-1 text-left mx-14 font-bold">60s Strips</div>
    <div>
      <Strip
        v-for="index in numStrips"
        :key="index"
      />
    </div>
    <div class="my-4 h-20">
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
