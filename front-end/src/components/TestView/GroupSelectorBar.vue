<template>
<div class="flex items-center">
  <GroupSelector type="Preprocess" class="w-1/3" />
  <GroupSelector type="Test" class="w-1/3"/>
  <GroupSelector type="Sample" class="w-1/3" />
</div>
</template>

<script lang="ts" setup>
import GroupSelector from './GroupSelector.vue'
</script>
