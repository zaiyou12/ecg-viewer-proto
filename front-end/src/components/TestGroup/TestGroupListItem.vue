<template>
  <tr class="cursor-pointer hover:bg-blue-50 h-10 border-b">
    <template v-for="(value, prop, idx) in group" :key="idx">
      <td v-if="prop !== 'testIds'">{{ value === undefined ? '—' : value }}</td>
    </template>
  </tr>
</template>

<script setup lang="ts">
const props = defineProps<{
  group: TestGroup
}>()
</script>
