<template>
  <tr class="group-test-list-item" v-bind="$attrs">
    <td class="checkbox">
      <input
        type="checkbox"
        class="group-test-selector-checkbox"
        :checked="allPagesChecked"
        @click="allPagesChecked ? toggleAllPages(false) : toggleAllPages(true)"
      />
    </td>
    <template v-for="(col, idx) in testCols" :key="idx">
      <td @click="showPages = !showPages" :class="col.class">
        <div v-if="col.prop === 'condition'">
          <StatusColor :final-condition="ecgTest.condition.final" />
        </div>
        <div v-else>{{ ecgTest[col.prop!] }}</div>
      </td>
    </template>
  </tr>
  <template v-if="showPages">
    <tr
      class="cursor-pointer bg-gray-100 hover:bg-blue-50"
      v-for="(p, idx) in pages"
      :key="idx"
    >
      <td>
        <input
          type="checkbox"
          class="group-test-selector-checkbox"
          v-model="(groupStore.checkedTestIds[ecgTest.id] as PageChecked)[p]"
        />
      </td>
      <td class="border-b pt-1">&#8627;</td>
      <td
        colspan="5"
        class="text-left border-b"
        @click="viewTest(p)"
      >Page {{ p }}</td>
    </tr>
  </template>
</template>

<script lang="ts" setup>
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import StatusColor from '@/components/StatusColor.vue'
import useTestViewStore from '../../../stores/test-view'
import useGroupPageStore from '../../../stores/group-page'

const props = defineProps<{
  test: [ecgTest: EcgTest.Meta, pages: number[]]
  testCols: TestCol[]
}>()

type PageChecked = {
  [page: number]: boolean
}

const router = useRouter()
const viewStore = useTestViewStore()
const groupStore = useGroupPageStore()

const ecgTest = computed(() => props.test[0])
const pages = computed(() => props.test[1])

const showPages = ref(false)

const allPagesChecked = computed(() => {
  const checkedPages = groupStore.checkedTestIds[ecgTest.value.id] as PageChecked
  for (const page in checkedPages) {
    if (!checkedPages[page]) {
      return false
    }
  }
  return true
})

function toggleAllPages(val: boolean) {
  const checkedPages = groupStore.checkedTestIds[ecgTest.value.id] as PageChecked
  for (const page in checkedPages) {
    checkedPages[page] = val
  }
}

async function viewTest(page: number) {
  router.push({ name: 'testView' })
  await viewStore.viewNewTest(ecgTest.value.id, page)
}
</script>
