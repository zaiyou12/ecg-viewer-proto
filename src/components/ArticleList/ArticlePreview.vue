<template>
  <article class="w-full p-2 break-all truncate border-t border-gray-300 flex-col">
    {{ article }}
  </article>
</template>

<script lang="ts" setup>
const props = defineProps<{
  article: number;
  index: number;
}>();
</script>
