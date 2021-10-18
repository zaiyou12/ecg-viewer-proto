<template>
<div class="flex items-center">
  <TestGroupSelector type="Preprocess" class="w-1/3" />
  <TestGroupSelector type="Test" class="w-1/3"/>
  <TestGroupSelector type="Sample" class="w-1/3" />
</div>
</template>

<script lang="ts" setup>
import TestGroupSelector from './TestGroupSelector.vue'
</script>
