<template>
  <TestDetailHeader :testSeq="paramToString(testSeq)" />
  <TestDetails class="transform translate-y-16" />
</template>

<script lang="ts" setup>
import { useRoute } from 'vue-router'
import TestDetailHeader from '../components/TestView/TestDetailHeader.vue'
import TestDetails from '@/components/TestView/TestDetails.vue'
import { paramToString } from '../utils/helper'

const route = useRoute()
const testSeq = route.params.testSeq
</script>
