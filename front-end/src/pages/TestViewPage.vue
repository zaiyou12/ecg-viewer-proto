<template>
  <div class="view-min-width overflow-auto overscroll-none">
    <TestDetailHeader :testSeq="paramToString(testSeq)" />
    <TestDetails class="transform translate-y-16" />
  </div>
</template>

<script lang="ts" setup>
import { useRoute } from 'vue-router'
import TestDetailHeader from '../components/TestView/TestDetailHeader.vue'
import TestDetails from '@/components/TestView/TestDetails.vue'
import { paramToString } from '../utils/helper'

const route = useRoute()
const testSeq = route.params.testSeq
</script>

<style>
.view-min-width {
  min-width: 1024px;
}
</style>
