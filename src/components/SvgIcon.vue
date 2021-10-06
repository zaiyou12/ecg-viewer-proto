<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :class="attrs.class"
    fill="none"
    viewBox="0 0 24 24"
    stroke="currentColor"
    v-html="SvgIcon[name]"
  ></svg>
</template>
<script setup lang="ts">
import { useAttrs } from 'vue'

const attrs = useAttrs()

export type SvgIconIndex = 'ChartPie' |
  'ArrowCircleLeft' |
  'Search' |
  'Filter' |
  'Adjustments'

type SvgIconType = {
  [k in SvgIconIndex]: string
}

const SvgIcon: SvgIconType = {
  ChartPie:
    '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z" />\
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.488 9H15V3.512A9.025 9.025 0 0120.488 9z" />',
  ArrowCircleLeft: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 15l-3-3m0 0l3-3m-3 3h8M3 12a9 9 0 1118 0 9 9 0 01-18 0z" />',
  Search: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />',
  Filter: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />',
  Adjustments: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />'
} as const

const props = defineProps<{
  name: SvgIconIndex
}>()
</script>
