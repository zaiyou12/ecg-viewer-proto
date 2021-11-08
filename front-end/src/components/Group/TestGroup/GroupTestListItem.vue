<template>
  <tr class="group-test-list-item">
    <td class="checkbox">
      <input
        type="checkbox"
        class="group-test-selector-checkbox"
        v-model="groupStore.checkedTestIds[test.id]"
      />
    </td>
    <template v-for="(value, prop, idx) in test" :key="idx">
      <td
        v-if="prop === 'condition'"
        @click="viewTest()"
        :class="testCols[idx].class"
      >
        <div>
          <StatusColor :final-condition="test.condition.final" />
        </div>
      </td>
      <td v-else @click="viewTest()" :class="testCols[idx].class">
        <div>{{ value }}</div>
      </td>
    </template>
  </tr>
</template>

<script lang="ts" setup>
import { useRouter } from 'vue-router'
import StatusColor from '@/components/StatusColor.vue'
//@ts-ignore
import useTestViewStore from '@/stores/test-view'
//@ts-ignore
import useGroupPageStore from '@/stores/group-page'

const props = defineProps<{
  test: EcgTest.Meta
  testCols: TestCol[]
}>()

const router = useRouter()
const viewStore = useTestViewStore()
const groupStore = useGroupPageStore()

async function viewTest() {
  router.push({ name: 'testView' })
  await viewStore.viewNewTest(props.test.id)
}
console.log(props.testCols)
</script>

<style>
@layer components {
  .group-test-list-item {
    @apply border-b select-none text-sm
    hover:bg-blue-50;
  }
  .group-test-list-item td {
    @apply cursor-pointer;
  }
  .group-test-list-item td div {
    @apply overflow-hidden overflow-ellipsis whitespace-nowrap;
  }
}
</style>
