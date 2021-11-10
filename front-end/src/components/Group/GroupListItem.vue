<template>
  <tr
    class="group-list-item"
    :class="{ 'bg-blue-100': store.selectedGroupId === group.id }"
    @mouseup="showTestInGroup(group.id)"
  >
    <td v-for="(col, idx) in groupCols" :key="idx" :class="col.class">
      <div>{{ renderValue(col.prop!) }}</div>
    </td>
  </tr>
</template>

<script setup lang="ts">
import useGroupPageStore from '../../stores/group-page'
import { hasTypedProperty } from '../../utils/helper'

const props = defineProps<{
  group: TestGroup | SampleGroup
  groupCols: GroupCol[]
}>()

const store = useGroupPageStore()

async function showTestInGroup(gid: number) {
  await store.fetchTestList(gid)
}

function renderValue(k: keyof TestGroup | keyof SampleGroup) {
  const fallback = (v?: any) => v === undefined ? '—' : v
  if (k === 'id') return props.group.id
  else if (k === 'groupName') return props.group.groupName
  else if (k === 'groupStatus') return props.group.groupStatus.toUpperCase()
  else if (k === 'pid') return fallback(props.group.pid)
  else {
    if (hasTypedProperty(props.group, 'numTests')) return props.group.numTests
    else if (hasTypedProperty(props.group, 'numSamples')) return props.group.numSamples
    else return '—'
  }
}
</script>

<style>
@layer components {
  .group-list-item {
    @apply cursor-pointer hover:bg-blue-50 h-10 border-b;
  }
  .group-list-item td div {
    @apply overflow-hidden overflow-ellipsis whitespace-nowrap;
  }
}
</style>
