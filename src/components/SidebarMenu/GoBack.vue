<template>
  <div class="go-back-container" @click="goBack()">
    <div class="h-full flex items-center justify-center text-white">
      <SvgIcon name="ArrowCircleLeft" class="h-6 w-6 mr-2" />
      <p class="font-bold">Back</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

function goBack() {
  router.back()
}
</script>

<style>
@layer components {
  .go-back-container {
    @apply cursor-pointer h-14
      bg-gradient-to-l from-blue-300 via-blue-400 to-blue-400
      hover:from-blue-200 hover:via-blue-300 hover:to-blue-300
  }
}
</style>
