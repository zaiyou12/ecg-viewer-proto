<template>
  <li class="w-full p-2 break-all truncate border-t border-gray-300">
    {{ test }}
  </li>
</template>

<script lang="ts" setup>
const props = defineProps<{
  test: string;
  index: number;
}>();
</script>
