<template>
  <AppLink name="testViewer" :params="{index: ecgTest}">
    <article class="w-full p-2 break-all truncate border-t border-gray-300 flex-col hover:bg-gray-200 active:bg-gray-400">
        {{ ecgTest }}
    </article>
  </AppLink>
</template>

<script lang="ts" setup>
const props = defineProps<{
  ecgTest: number;
  index: number;
}>();
</script>
