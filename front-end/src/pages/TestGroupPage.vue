<template>
  <GroupPageBp title="Test Groups" groupType="t" :groupCols="groupCols" />
</template>

<script setup lang="ts">
import GroupPageBp from '@/components/Group/GroupPageBp.vue'

const groupCols = [
  { label: 'ID', class: 'id', prop: 'id' },
  { label: 'Group Name', class: 'name', prop: 'groupName' },
  { label: 'Description', class: 'desc', prop: 'description' },
  { label: '# Tests', class: 'num', prop: 'numTests' },
  { label: 'PID', class: 'pid', prop: 'pid' },
]
</script>
