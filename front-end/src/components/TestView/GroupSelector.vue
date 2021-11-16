<template>
  <div class="w-full">
    <GroupButton :type="type" v-model:showDrop="showDrop" />
    <PreprocessDropdown v-if="type === 'p'" :showDrop="showDrop" />
    <GroupDropdown v-else-if="type === 't'" :showDrop="showDrop" type="t" />
    <GroupDropdown v-else :showDrop="showDrop" type="s" />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import GroupButton from './GroupButton.vue'
import PreprocessDropdown from './PreprocessDropdown.vue'
import GroupDropdown from './GroupDropdown.vue'

const props = defineProps<{
  type: Resp.GroupType
}>()

const showDrop = ref(false)
</script>
