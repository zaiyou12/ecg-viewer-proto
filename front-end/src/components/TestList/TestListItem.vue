<template>
  <tr class="cursor-pointer hover:bg-blue-50" @click="viewTest(ecgTest.id)">
    <template v-for="(value, prop, index) in ecgTest" :key="index">
      <td v-if="prop === 'condition'">
        <div class="flex justify-center">
          <svg
            viewBox="0 0 100 100"
            xmlns="http://www.w3.org/2000/svg"
            class="h-3 w-3"
            :fill="whichColor(ecgTest.condition.final)"
          >
            <circle cx="50" cy="50" r="50" />
          </svg>
        </div>
      </td>
      <td v-else>{{ value }}</td>
    </template>
  </tr>
</template>

<script lang="ts" setup>
import { useRouter } from 'vue-router'
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
