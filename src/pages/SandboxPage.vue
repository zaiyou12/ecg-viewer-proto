<template>
  <div class="mt-3 mb-10">
    <p>This is a sandbox page.</p>
    <input class="border-2"
      type="text"
      v-model="inputText"
    >
    <p>Typed: {{ inputText }}</p>
  </div>
  <div>
    <!-- <button>
      <div class="flex items-center">
        <SvgIcon class="w-5 h-5 ml-1"
          name="Adjustments" :strokeColor="null" :strokeWidth="undefined" />
        <div :class="textStyle">{{ btnText }}</div>
      </div>
    </button> -->
    <SvgIconButton icon="Adjustments" text="Filter" />
    <SvgIconButton icon="Adjustments" text="Hey" />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import SvgIconButton from '@/components/SvgIconButton.vue'


const inputText = ref('')

////////////////////////////////
const btnText = "Hey"
const textStyle = 'font-bold'
</script>
