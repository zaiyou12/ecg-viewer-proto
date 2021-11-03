<template>
  <div class="text-2xl font-bold pl-5">{{ title }}</div>
  <div
    class="text-sm ml-5"
  >Add or remove {{ groupType === 't' ? 'test' : 'sample' }} groups</div>
  <div>
    <button class="mx-5 group-modify-btn" @mouseup="$emit('showAdder')">
      <SvgIcon class="h-5 w-5" name="PlusSm" />
    </button>
    <button class="group-modify-btn" @mouseup="$emit('showRemover')">
      <SvgIcon class="h-5 w-5" name="MinusSm" />
    </button>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  title: string
  groupType: Resp.GroupType
}>()

const emits = defineEmits(['showAdder', 'showRemover'])
</script>

<style>
@layer components {
  .group-modify-btn {
    @apply px-1 py-1 rounded-lg
    bg-blue-400 text-white font-bold
    hover:bg-blue-300;
  }
}
</style>
