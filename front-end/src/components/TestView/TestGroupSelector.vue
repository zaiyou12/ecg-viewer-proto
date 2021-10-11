<template>
  <div class="w-full">
    <TestGroupButton :type="type" v-model:showDrop="showDrop" />
    <TestGroupDropdown v-bind="{ type, showDrop }" />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import TestGroupButton from './TestGroupButton.vue'
import TestGroupDropdown from './TestGroupDropdown.vue'

const props = defineProps<{
  type: 'Preprocess' | 'Test' | 'Sample'
}>()

const showDrop = ref(false)
</script>
