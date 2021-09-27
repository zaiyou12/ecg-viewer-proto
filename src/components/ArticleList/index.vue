<template>
  <section class="w-full max-w-8xl mx-auto pb-5">
    <div v-if="articlesDownloading">Loading...</div>
    <div v-else-if="articles.length === 0">No articles are here</div>
    <template v-else>
      <div class="bg-white shadow text-base text-gray-600 text-left">
        <ArticlePreview
          v-for="(article, index) in articles"
          :key="index"
          :article="article"
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

<script lang="ts" setup>
import ArticlePreview from "./ArticlePreview.vue";
const articlesDownloading = false
const articles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
</script>
