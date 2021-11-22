<template>
  <tr class="test-list-item" @mouseup="viewTest()">
    <template v-for="(col, idx) in testCols" :key="idx">
      <td :class="col.class">
        <div v-if="col.prop === 'condition'" class="flex justify-center">
          <StatusColor :final-condition="ecgTest.condition.final" />
        </div>
        <div v-else>{{ ecgTest[col.prop!] }}</div>
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
