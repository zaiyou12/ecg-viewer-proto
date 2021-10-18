<template>
  <tr class="cursor-pointer">
    <template v-for="(prop, idx) in group" :key="idx">
      <td v-if="prop !== 'ecgTests'">
        {{ prop }}
      </td>
    </template>
  </tr>
</template>

<script setup lang="ts">
const props = defineProps<{
  group: TestGroup
}>()
</script>
