<template>
  <div class="group-test-list-container">
    <table class="group-test-list">
      <thead class="cursor-default border-b-2">
        <th class="checkbox">
          <input
            type="checkbox"
            class="group-test-selector-checkbox"
            :checked="allChecked"
            @click="allChecked ? toggleAll(false) : toggleAll(true)"
          />
        </th>
        <th
          v-for="(col, idx) in listHeaders"
          :key="idx"
          class="h-7 px-3 pb-2"
          :class="col.class"
        >{{ col.label }}</th>
      </thead>
      <tbody>
        <template v-for="(test, idx) in tests" :key="idx">
          <component
            :is="item"
            :test="test"
            :testCols="listHeaders"
            class="h-11"
          />
        </template>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts" setup>
import { computed, markRaw } from 'vue'
import TestItem from '@/components/Group/TestGroup/GroupTestListItem.vue'
import SampleItem from '@/components/Group/SampleGroup/GroupTestListItem.vue'
import useGroupPageStore, {
  TestChecked, SampleChecked, PageChecked
} from '../../stores/group-page'

const store = useGroupPageStore()

const isTestGroup = computed(() => store.type === 't')
const tests = computed(() => isTestGroup.value ? store.tests : store.samples)

const item = computed(() => {
  if (isTestGroup.value) return markRaw(TestItem)
  else return markRaw(SampleItem)
})

const allChecked = computed(() => {
  /**
   * countTests is to disable checked behavior when no test exists in group
   */
  let countTests = 0
  if (isTestGroup.value) {
    for (const id in (store.checkedTestIds as TestChecked)) {
      if (!store.checkedTestIds[id]) return false
      countTests++
    }
  } else {
    for (const id in (store.checkedTestIds as SampleChecked)) {
      const checkedPages = store.checkedTestIds[id] as PageChecked
      countTests++
      for (const page in checkedPages) {
        if (!checkedPages[page]) return false
      }
    }
  }
  return countTests > 0
})

function toggleAll(val: boolean) {
  if (isTestGroup.value) {
    for (const id in (store.checkedTestIds as TestChecked)) {
      store.checkedTestIds[id] = val
    }
  } else {
    for (const id in (store.checkedTestIds as SampleChecked)) {
      const checkedPages = store.checkedTestIds[id] as PageChecked
      for (const page in checkedPages) {
        checkedPages[page] = val
      }
    }
  }
}
/**
 * Must be in order with the deserialized EcgTest.Meta object
 * @see deserializer.deserializeTest
 */
const listHeaders: TestCol[] = [
  { label: 'DB ID', class: 'db-id' },
  { label: 'Test Seq', class: 'test-seq' },
  { label: 'Region', class: 'reg' },
  { label: 'Duration', class: 'dur' },
  { label: 'Status', class: 'stat' },
]
</script>

<style>
@layer components {
  .group-test-list-container {
    @apply border rounded-lg p-5 h-full
    overflow-y-auto overscroll-contain;
  }

  .group-test-list {
    @apply table-fixed w-full;
  }
  .group-test-list th.checkbox,
  td.checkbox {
    width: 5%;
  }
  .group-test-list th.db-id {
    width: 15%;
  }
  .group-test-list th.reg,
  th.dur,
  th.stat {
    width: 15%;
  }

  .group-test-selector-checkbox {
    @apply w-4 h-4 mt-1;
  }
}
</style>
