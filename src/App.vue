<script setup lang="ts">
import AppNavigation from "./components/AppNavigation.vue";
import ArticlesList from "./components/ArticleList/index.vue";
</script>

<template>
  <AppNavigation />
  <ArticlesList />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.max-w-screen-lg {
  max-width: 1012px;
}
</style>
