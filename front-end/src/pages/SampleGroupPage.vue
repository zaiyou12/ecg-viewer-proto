<template>
  <GroupPageBp title="Sample Groups" groupType="s" :groupCols="groupCols" />
</template>

<script setup lang="ts">
import GroupPageBp from '@/components/Group/GroupPageBp.vue'

const groupCols = [
  { label: 'ID', class: 'id' },
  { label: 'Group Name', class: 'name' },
  { label: 'Description', class: 'desc' },
  { label: '# Samples', class: 'num' },
  { label: 'PID', class: 'pid' },
]
</script>
