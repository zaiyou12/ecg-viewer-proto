<template>
  <div v-if="disabled" :class="`p-1 rounded-lg bg-gray-50 ${margin}`">
    <SvgIcon
      :name="buttonTypeMap[type]"
      :stroke="disabledColor"
      :strokeWidth="strokeWidth"
      :class="size"
    />
  </div>
  <button
    v-else
    :class="`p-1 rounded-lg bg-blue-100 hover:bg-blue-50 ${margin}`"
    @mouseup="pageClick()"
  >
    <SvgIcon
      :name="buttonTypeMap[type]"
      :strokeWidth="strokeWidth"
      :class="size"
    />
  </button>
</template>

<script setup lang="ts">
import useTestsStore from '../../stores/test-list'

interface PageNavButtonProps {
  type: 'ffwLeft' | 'left' | 'right' | 'ffwRight'
  page: number
  disabled: boolean
  routeName?: string
  strokeWidth?: number
  size?: string
  disabledColor?: string
}

const props = withDefaults(defineProps<PageNavButtonProps>(), {
  routeName: 'testPagination',
  strokeWidth: 3,
  size: 'w-5 h-5',
  disabledColor: '#C0C0C0'
})

const margin = props.type === 'ffwLeft' || props.type === 'left' ? 'mr-5' : 'ml-5'

const buttonTypeMap = {
  'ffwLeft': 'ChevronDoubleLeft',
  'left': 'ChevronLeft',
  'right': 'ChevronRight',
  'ffwRight': 'ChevronDoubleRight'
}

const store = useTestsStore()

async function pageClick() {
  store.page = props.page
  await store.fetchEcgTests()
}
</script>
