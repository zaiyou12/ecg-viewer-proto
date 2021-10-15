<template>
  <div class="border rounded-md mx-14">
    <img :src="DummyObj[type]" class="w-full h-28"/>
  </div>
</template>

<script setup lang="ts">
import g1 from '@/assets/g1.png'
import g2 from '@/assets/g2.png'
import g3 from '@/assets/g3.png'
import g4 from '@/assets/g4.png'
import g5 from '@/assets/g5.png'
import g6 from '@/assets/g6.png'

const props = defineProps<{
  type: 'g1' | 'g2' | 'g3' | 'g4' | 'g5' | 'g6'
}>()

const DummyObj = {
  'g1': g1,
  'g2': g2,
  'g3': g3,
  'g4': g4,
  'g5': g5,
  'g6': g6
}
</script>
