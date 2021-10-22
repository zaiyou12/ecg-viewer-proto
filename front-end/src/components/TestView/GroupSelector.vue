<template>
  <div class="w-full">
    <GroupButton :type="type" v-model:showDrop="showDrop" />
    <PreprocessDropdown v-if="type === 'Preprocess'" :showDrop="showDrop" />
    <TestGroupDropdown v-if="type === 'Test'" :showDrop="showDrop" />
    <SampleGroupDropdown v-else :showDrop="showDrop" />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import GroupButton from './GroupButton.vue'
import PreprocessDropdown from './PreprocessDropdown.vue'
import TestGroupDropdown from './TestGroupDropdown.vue'
import SampleGroupDropdown from './SampleGroupDropdown.vue'

const props = defineProps<{
  type: 'Preprocess' | 'Test' | 'Sample'
}>()

const showDrop = ref(false)
</script>
