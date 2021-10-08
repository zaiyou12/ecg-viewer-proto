<template>
  <tr class="cursor-pointer hover:bg-blue-50" @click="viewTest(ecgTest.testSeq)">
    <template
      v-for="(value, prop, index) in ecgTest"
      :key="index"
    >
      <template v-if="prop !== 'path'">
        <td v-if="prop === 'sampled'">
          <div class="flex justify-center">
            <SvgIcon
              :name="isNotEmpty(ecgTest.sampled) ? 'InformationCircle' : 'XCircle'" class="h-5 w-5"
              :strokeColor="isNotEmpty(ecgTest.sampled) ? undefined : '#D3D3D3'"
            />
          </div>
        </td>
        <td v-else-if="prop === 'anomaly'">
          <div class="flex justify-center">
            <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"
              class="h-3 w-3" :fill="isNotEmpty(ecgTest.anomaly) ? '#3CB371' : '#FF6347'"
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


const props = defineProps<{
  ecgTest: EcgTest.Meta
}>()

const router = useRouter()

function viewTest(idx: number | string): void {
  router.push({ name: 'testView', params: { testSeq: idx } })
}

function isNotEmpty(arr: any[]): boolean {
  return !!(arr.length)
}
</script>
