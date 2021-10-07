<template>
  <tr class="cursor-pointer hover:bg-blue-50" @click="viewTest(ecgTest.testSeq)">
    <template
      v-for="(value, propertyName, index) in ecgTest"
      :key="index"
    >
      <td v-if="propertyName !== 'path'">{{ value }}</td>
    </template>
  </tr>
</template>

<script lang="ts" setup>
import { useRouter } from 'vue-router'


const props = defineProps<{
  ecgTest: EcgTest.Meta
}>()

const router = useRouter()

function viewTest(idx: number | string): void {
  router.push({ name: 'testView', params: { testSeq: idx } })
}
</script>
