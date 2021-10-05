<script lang="ts" setup>
import { useRoute } from "vue-router";
import TestDetails from "../components/TestDetails.vue";

const route = useRoute()
const index = route.params.index
</script>

<template>
  <div class="my-8">Test Viwer - {{ index }}</div>
  <TestDetails />
  <div class="my-4">
    <AppLink name="testList"> > GO BACK TO TestList </AppLink>
  </div>
</template>
