<script lang="ts" setup>
import TestPreview from "./TestPreview.vue";
const testDownloading = false
const ecgTests = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
</script>

<template>
  <section class="w-full max-w-8xl mx-auto pb-5">
    <div v-if="testDownloading">Loading...</div>
    <div v-else-if="ecgTests.length === 0">No articles are here</div>
    <template v-else>
      <div class="bg-white shadow text-base text-gray-600 text-left ">
        <TestPreview
          v-for="(ecgTest, index) in ecgTests"
          :key="index"
          :ecgTest="ecgTest"
          :index="index"
        />
      </div>
      <!-- <div class="flex justify-start">
        <button class="p-3 underline" v-on:click="loadMoreArticles">
          더 불러오기
        </button>
      </div> -->
    </template>
  </section>
</template>
