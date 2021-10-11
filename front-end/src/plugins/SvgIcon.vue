<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :class="$attrs.class"
    fill="none"
    viewBox="0 0 24 24"
    :stroke="strokeColor"
    :stroke-width="strokeWidth"
    v-html="SvgIcon[name]"
  ></svg>
</template>
<script setup lang="ts">
interface SvgIconProp {
  name: SvgIconIndex
  strokeColor?: string
  strokeWidth?: number
}

const props = withDefaults(defineProps<SvgIconProp>(), {
  strokeColor: 'currentColor',
  strokeWidth: 2
})

export type SvgIconIndex = 'ChartPie' |
  'Collection' |
  'ArrowCircleLeft' |
  'Search' |
  'Filter' |
  'Adjustments' |
  'ChevronDoubleLeft' |
  'ChevronDoubleRight' |
  'ChevronLeft' |
  'ChevronRight' |
  'InformationCircle' |
  'XCircle' |
  'ChevronDown'

type SvgIconType = {
  [k in SvgIconIndex]: string
}

const SvgIcon: SvgIconType = {
  ChartPie:
    '<path stroke-linecap="round" stroke-linejoin="round" d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z" />\
    <path stroke-linecap="round" stroke-linejoin="round" d="M20.488 9H15V3.512A9.025 9.025 0 0120.488 9z" />',
  Collection: '<path stroke-linecap="round" stroke-linejoin="round" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />',
  ArrowCircleLeft: '<path stroke-linecap="round" stroke-linejoin="round" d="M11 15l-3-3m0 0l3-3m-3 3h8M3 12a9 9 0 1118 0 9 9 0 01-18 0z" />',
  Search: '<path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />',
  Filter: '<path stroke-linecap="round" stroke-linejoin="round" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />',
  Adjustments: '<path stroke-linecap="round" stroke-linejoin="round" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />',
  ChevronDoubleLeft: '<path stroke-linecap="round" stroke-linejoin="round" d="M11 19l-7-7 7-7m8 14l-7-7 7-7" />',
  ChevronDoubleRight: '<path stroke-linecap="round" stroke-linejoin="round" d="M13 5l7 7-7 7M5 5l7 7-7 7" />' ,
  ChevronLeft: '<path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />',
  ChevronRight: '<path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />',
  InformationCircle: '<path stroke-linecap="round" stroke-linejoin="round" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />',
  XCircle: '<path stroke-linecap="round" stroke-linejoin="round" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />',
  ChevronDown: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />'
} as const

</script>
