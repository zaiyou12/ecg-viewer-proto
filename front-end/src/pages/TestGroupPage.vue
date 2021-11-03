<template>
  <GroupPageBp title="Test Groups" groupType="t" :groupCols="groupCols" />
</template>

<script setup lang="ts">
import GroupPageBp from '@/components/Group/GroupPageBp.vue'

const groupCols = [
  { label: 'ID', class: 'id' },
  { label: 'Group Name', class: 'name' },
  { label: 'Description', class: 'desc' },
  { label: '# Tests', class: 'num' },
  { label: 'PID', class: 'pid' },
]
</script>
