<script setup lang="ts">
import AppNavigation from "./components/AppNavigation.vue";
import HelloWorld from "./components/HelloWorld.vue";
</script>

<template>
  <AppNavigation />
  <HelloWorld msg="Hello World!"/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: rgba(167, 243, 208, 0.4);
}
.max-w-screen-lg {
  max-width: 1012px;
}
</style>
