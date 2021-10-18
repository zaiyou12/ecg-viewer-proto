<template>
  <div class="w-full">
    <GroupButton :type="type" v-model:showDrop="showDrop" />
    <PreprocessDropdown v-if="type === 'Preprocess'" :showDrop="showDrop"/>
    <TestGroupDropdown v-else v-bind="{ type, showDrop }" />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import GroupButton from './GroupButton.vue'
import PreprocessDropdown from './PreprocessDropdown.vue'
import TestGroupDropdown from './TestGroupDropdown.vue'

const props = defineProps<{
  type: 'Preprocess' | 'Test' | 'Sample'
}>()

const showDrop = ref(false)
</script>
