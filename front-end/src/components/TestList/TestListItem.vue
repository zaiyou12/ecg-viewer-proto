<template>
  <tr class="cursor-pointer hover:bg-blue-50" @click="viewTest(ecgTest.id)">
    <template v-for="(value, prop, index) in ecgTest" :key="index">
      <td v-if="prop === 'condition'">
        <div class="flex justify-center">
          <StatusColor :final-condition="ecgTest.condition.final" />
        </div>
      </td>
      <td v-else>{{ value }}</td>
    </template>
  </tr>
</template>

<script lang="ts" setup>
import { useRouter } from 'vue-router'
import StatusColor from '@/components/StatusColor.vue'
import useTestViewStore from '../../stores/test-view'

const props = defineProps<{
  ecgTest: EcgTest.Meta
}>()

const router = useRouter()
const store = useTestViewStore()

async function viewTest(idx: number | string) {
  router.push({ name: 'testView' })
  await store.viewNewTest(props.ecgTest.id)
}

function whichColor(finalStatus: EcgTest.ConditionType): string {
  if (finalStatus === 'normal') return '#3CB371'
  if (finalStatus === 'abnormal') return '#FF6347'
  else return '#808080'
}
</script>
