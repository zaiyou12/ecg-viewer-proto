<template>
  <tr class="cursor-pointer hover:bg-blue-50" @click="viewTest(testSeq)">
    <td>{{ testSeq }}</td>
    <td>{{ duration }}</td>
    <td>{{ region }}</td>
    <td>{{ sampled }}</td>
    <td>{{ normal }}</td>
  </tr>
</template>

<script lang="ts" setup>
import { getCurrentInstance } from 'vue'

interface TestListItemProps {
  testSeq: string
  duration: number
  region: string
  sampled?: boolean
  normal?: boolean
  index?: number
}

const props = withDefaults(defineProps<TestListItemProps>(), {
  sampled: false,
  normal: false
})

const instance = getCurrentInstance()

function viewTest(idx: string): void {
  instance!.appContext.config.globalProperties.$router.push({ name: 'testView', params: { testSeq: idx } })
}
</script>
