<template>
  <GroupPageBp title="Sample Groups" groupType="s" :groupCols="groupCols" />
</template>

<script setup lang="ts">
import GroupPageBp from '@/components/Group/GroupPageBp.vue'

const groupCols = [
  { label: 'ID', class: 'id', prop: 'id' },
  { label: 'Group Name', class: 'name', prop: 'groupName' },
  { label: 'Status', class: 'stat', prop: 'groupStatus' },
  { label: '# Samples', class: 'num', prop: 'numTests' },
  { label: 'PID', class: 'pid', prop: 'pid' },
]
</script>
