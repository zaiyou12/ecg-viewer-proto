<template>
  <PageHeader>
    <div class="w-1/2 flex items-center cursor-default justify-between">
      <div class="flex items-center">
        <p
          class="ml-5 font-bold xl:text-2xl text-xl text-left"
        >Test {{ store.selectedTest!.seq }}</p>
        <p
          class="ml-5 text-left xl:text-base text-sm"
        >DB#{{ store.selectedTest!.id }}</p>
      </div>
      <div class="flex flex-wrap text-sm">
        <p class="w-1/2 text-left">
          <b>HR</b>
          {{ store.details!.hr }}
        </p>
        <p class="w-1/2 text-left">
          <b>DUR</b>
          {{ store.selectedTest!.duration }}H
        </p>
        <p class="w-full text-left">
          <b>STAT</b>
          {{ store.selectedTest!.condition.final.toUpperCase() }}
        </p>
      </div>
    </div>
    <div class="w-1/2 border-l">
      <GroupSelectorBar />
    </div>
  </PageHeader>
</template>

<script lang="ts" setup>
import PageHeader from '@/components/PageHeader.vue';
import GroupSelectorBar from './GroupSelectorBar.vue'
import useTestViewStore from '../../stores/test-view'

const store = useTestViewStore()
</script>

<style>
</style>
