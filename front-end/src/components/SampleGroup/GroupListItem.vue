<template>
  <tr
    class="cursor-pointer hover:bg-blue-50 h-10 border-b"
    :class="{ 'bg-blue-100': store.selectedGroupId === group.id }"
    @mouseup="showTestInGroup(group.id)"
  >
    <td>{{ group.id }}</td>
    <td>{{ group.groupName }}</td>
    <td>{{ group.description === undefined ? '—' : group.description }}</td>
    <td>{{ group.numSamples }}</td>
    <td>{{ group.pid === undefined ? '—' : group.pid }}</td>
  </tr>
</template>

<script setup lang="ts">
import useGroupPageStore from '../../stores/group-page';

const props = defineProps<{
  group: SampleGroup
}>()

const store = useGroupPageStore()

async function showTestInGroup(gid: number) {
  await store.fetchTestList(gid)
}
</script>
