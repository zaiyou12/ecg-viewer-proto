<template>
  <TestDetails :testSeq="testSeq" />
</template>

<script lang="ts" setup>
import { useRoute } from 'vue-router'
import TestDetails from '@/components/TestView/TestDetails.vue'

const route = useRoute()
const testSeq = route.params.testSeq
</script>
