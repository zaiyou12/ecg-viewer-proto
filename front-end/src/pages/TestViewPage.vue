<template>
  <div class="view-min-width overflow-auto overscroll-none">
    <template v-if="store.selectedTest == undefined">
      <p>Invalid test view request</p>
    </template>
    <template v-else>
      <TestDetailHeader />
      <TestDetails class="transform translate-y-16" />
    </template>
  </div>
</template>

<script lang="ts" setup>
// import { useRoute } from 'vue-router'
import TestDetailHeader from '@/components/TestView/TestDetailHeader.vue'
import TestDetails from '@/components/TestView/TestDetails.vue'
import { paramToString } from '../utils/helper'
import useTestViewStore from '../stores/test-view';

// const route = useRoute()
// const testSeq = route.params.testSeq
const store = useTestViewStore()
</script>

<style>
.view-min-width {
  min-width: 1024px;
}
</style>
