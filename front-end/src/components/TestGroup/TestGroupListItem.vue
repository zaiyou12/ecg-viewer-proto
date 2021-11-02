<template>
  <tr class="cursor-pointer hover:bg-blue-50 h-10 border-b">
    <td>{{ group.id }}</td>
    <td>{{ group.groupName }}</td>
    <td>{{ group.description === undefined ? '—' : group.description }}</td>
    <td>{{ group.numTests }}</td>
    <td>{{ group.pid === undefined ? '—' : group.pid }}</td>
  </tr>
</template>

<script setup lang="ts">
const props = defineProps<{
  group: TestGroup
}>()
</script>
