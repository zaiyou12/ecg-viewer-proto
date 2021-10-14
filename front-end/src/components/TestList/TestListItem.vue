<template>
  <tr class="cursor-pointer hover:bg-blue-50" @click="viewTest(ecgTest.testSeq)">
    <template
      v-for="(value, prop, index) in ecgTest"
      :key="index"
    >
      <template v-if="prop !== 'path' && prop !== 'sGroup' && prop !== 'startTime'">
        <td v-if="prop === 'tGroup'">
          <div class="flex justify-center">
            <SvgIcon
              :name="isNotEmpty(ecgTest.tGroup) ? 'InformationCircle' : 'XCircle'" class="h-5 w-5"
              :strokeColor="isNotEmpty(ecgTest.tGroup) ? undefined : '#D3D3D3'"
            />
          </div>
        </td>
        <td v-else-if="prop === 'status'">
          <div class="flex justify-center">
            <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"
              class="h-3 w-3" :fill="whichColor(ecgTest.status.final)"
            >
              <circle cx="50" cy="50" r="50"/>
            </svg>
          </div>
        </td>
        <td v-else>{{ value }}</td>
      </template>
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

function viewTest(idx: number | string): void {
  store.selectedTest = props.ecgTest
  router.push({ name: 'testView', params: { testSeq: idx } })
}

function isNotEmpty(arr: any[]): boolean {
  return !!(arr.length)
}

function whichColor(finalStatus: EcgTest.StatusType): string {
  if (finalStatus === 'normal') return '#3CB371'
  if (finalStatus === 'abnormal') return '#FF6347'
  else return '#808080'
}
</script>
