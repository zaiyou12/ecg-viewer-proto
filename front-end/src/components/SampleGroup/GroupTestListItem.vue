<template>
  <tr
    class="cursor-pointer border-b h-11 hover:bg-blue-50 select-none"
    @click="showPages = !showPages"
    v-bind="$attrs"
  >
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
  <template v-if="showPages">
    <tr
      class="cursor-pointer border-b hover:bg-blue-50"
      v-for="(p, idx) in pages"
      :key="idx"
      @click="viewTest(p)"
    >
      <td>&#8627;</td>
      <td colspan="4" class="text-left">Page {{ p }}</td>
    </tr>
  </template>
</template>

<script lang="ts" setup>
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import useTestViewStore from '../../stores/test-view'

const props = defineProps<{
  sample: [ecgTest: EcgTest.Meta, pages: number[]]
}>()

const router = useRouter()
const store = useTestViewStore()

const ecgTest = computed(() => props.sample[0])
const pages = computed(() => props.sample[1])

const showPages = ref(false)

async function viewTest(page: number) {
  router.push({ name: 'testView' })
  await store.viewNewTest(ecgTest.value.id, page)
}

function whichColor(finalStatus: EcgTest.ConditionType): string {
  if (finalStatus === 'normal') return '#3CB371'
  if (finalStatus === 'abnormal') return '#FF6347'
  else return '#808080'
}
</script>
