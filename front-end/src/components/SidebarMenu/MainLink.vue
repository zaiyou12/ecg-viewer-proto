<template>
  <div class="flex justify-center">
    <AppLink name="main">
      <div class="flex items-center">
        <img :src="logo" class="w-12 h-12"/>
        <p class="text-white text-xl font-bold mr-3">ECG-Proto</p>
      </div>
    </AppLink>
  </div>
</template>

<script setup lang="ts">
import logo from '@/assets/logo.png'
</script>
