<template>
  <li class="cursor-pointer text-white text-xl font-bold py-1 my-1 hover:bg-gray-500">
    {{ sidebar_option }}
  </li>
</template>

<script setup lang="ts">
const props = defineProps<{
  sidebar_option: string
}>();
</script>
