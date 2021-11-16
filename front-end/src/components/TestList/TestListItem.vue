<template>
  <tr class="test-list-item" @click="viewTest()">
    <template v-for="(value, prop, idx) in ecgTest" :key="idx">
      <td v-if="prop === 'condition'" :class="testCols[idx].class">
        <div class="flex justify-center">
          <StatusColor :final-condition="ecgTest.condition.final" />
        </div>
      </td>
      <td v-else :class="testCols[idx].class">
        <div>{{ value }}</div>
      </td>
    </template>
  </tr>
</template>

<script lang="ts" setup>
import { useRouter } from 'vue-router'
import StatusColor from '@/components/StatusColor.vue'
import useTestViewStore from '../../stores/test-view'

const props = defineProps<{
  ecgTest: EcgTest.Meta
  testCols: TestCol[]
}>()

const router = useRouter()
const store = useTestViewStore()

async function viewTest() {
  router.push({ name: 'testView' })
  await store.viewNewTest(props.ecgTest.id)
}
</script>

<style>
@layer components {
  .test-list-item {
    @apply cursor-pointer hover:bg-blue-50;
  }
  .test-list-item td div {
    @apply overflow-hidden overflow-ellipsis whitespace-nowrap;
  }
}
</style>
