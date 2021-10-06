<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :class="attrs.class"
    fill="none"
    viewBox="0 0 24 24"
    stroke="currentColor"
    v-html="SvgIcon[name]"
  />
</template>
<script setup lang="ts">
import { useAttrs } from 'vue'

const attrs = useAttrs()

export type SvgIconIndex = 'ChartPie' | 'ArrowCircleLeft' | 'Search'
type SvgIconType = {
  [k in SvgIconIndex]: string
}

const SvgIcon: SvgIconType = {
  ChartPie:
    '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z" />\
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.488 9H15V3.512A9.025 9.025 0 0120.488 9z" />',
  ArrowCircleLeft: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 15l-3-3m0 0l3-3m-3 3h8M3 12a9 9 0 1118 0 9 9 0 01-18 0z" />',
  Search: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />'
} as const

const props = defineProps<{
  name: SvgIconIndex
}>()
</script>
