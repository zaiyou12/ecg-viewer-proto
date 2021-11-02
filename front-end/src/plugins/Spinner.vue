<!-- https://pjs21s.github.io/spinner-vuejs/ -->
<template>
  <template v-if="loading">
    <div class="spinner-screen-overlay"></div>
    <div class="spinner">
      <div></div>
      <div></div>
      <div></div>
    </div>
  </template>
</template>

<script setup lang="ts">
const props = withDefaults(defineProps<{ loading: boolean }>(), { loading: true })
</script>

<style>
.spinner {
  z-index: 99;
  transform: translateX(-50%) translateY(40vh);
  @apply inline-block absolute w-16 h-16;
}
.spinner div {
  left: 6px;
  width: 13px;
  animation: spinner 1.2s cubic-bezier(0, 0.5, 0.5, 1) infinite;
  @apply inline-block absolute bg-blue-300;
}
.spinner div:nth-child(1) {
  left: 6px;
  animation-delay: -0.24s;
}
.spinner div:nth-child(2) {
  left: 26px;
  animation-delay: -0.12s;
}
.spinner div:nth-child(3) {
  left: 45px;
  animation-delay: 0;
}
@keyframes spinner {
  0% {
    top: 6px;
    height: 51px;
  }
  50%,
  100% {
    top: 19px;
    height: 25px;
  }
}

.spinner-screen-overlay {
  z-index: 99;
  width: calc(100vw - 13rem);
  height: 100vh;
  @apply absolute opacity-10 bg-gray-400;
}
</style>
