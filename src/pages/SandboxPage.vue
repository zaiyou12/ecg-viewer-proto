<template>
  <p>This is a sandbox page.</p>
  <input class="border-2"
    type="text"
    v-model="inputText"
  >
  <p>Typed: {{ inputText }}</p>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const inputText = ref('')
</script>
