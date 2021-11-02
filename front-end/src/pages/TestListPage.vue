<template>
  <Spinner :loading="store.loading" />
  <div class="flex flex-col">
    <TestFilterPanel v-model:showPanel="showPanel" />
    <TestFilterBar class="flex-none" />
    <div class="flex-grow mx-5">
      <TestList :maxPageDisplay="maxPageDisplay" />
    </div>
    <div class="flex-none my-10">
      <Pagination :maxPageDisplay="maxPageDisplay" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, provide } from 'vue'
import TestFilterBar from '@/components/TestFilterBar/index.vue'
import TestFilterPanel from '@/components/TestFilterPanel/TestFilterPanel.vue'
import TestList from '@/components/TestList/index.vue'
import Pagination from '@/components/Pagination/index.vue'
import useTestsStore from '../stores/test-list'
import { TogglePanelKey, DisablePanelKey } from '../symbols/symbols'

const store = useTestsStore()
const maxPageDisplay = 10

const showPanel = ref(false)
const togglePanel = () => showPanel.value = !showPanel.value
const disablePanel = () => showPanel.value = false
provide(TogglePanelKey, togglePanel)
provide(DisablePanelKey, disablePanel)
</script>
