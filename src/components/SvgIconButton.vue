<template>
  <button>
    <div class="flex items-center justify-center">
      <SvgIcon :class="svgIconStyle"
        :name="icon" :strokeColor="iconColor" :strokeWidth="iconStrokeWidth" />
      <div :class="textStyle">{{ text }}</div>
    </div>
  </button>
</template>

<script setup lang="ts">
import { ref } from 'vue'


interface SvgIconButtonProps {
  icon: string
  text: string
  iconSize?: string
  iconTextMargin?: string
  iconColor?: string
  iconStrokeWidth?: string
  textStyle?: string
}
const props = withDefaults(defineProps<SvgIconButtonProps>(), {
  iconSize: 'w-5 h-5',
  iconTextMargin: 'mr-1',
  textStyle: 'font-bold',
})

const svgIconStyle = ref(`${props.iconSize} ${props.iconTextMargin}`)
</script>

<style>
</style>
