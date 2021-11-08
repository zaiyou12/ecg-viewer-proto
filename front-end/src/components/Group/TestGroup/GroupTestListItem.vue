<template>
  <tr class="group-test-list-item">
    <td>
      <input
        type="checkbox"
        class="group-test-selector-checkbox"
        v-model="groupStore.checkedTestIds[test.id]"
      />
    </td>
    <template v-for="(value, prop, idx) in test" :key="idx">
      <td v-if="prop === 'condition'" @click="viewTest()" class="prop">
        <StatusColor :final-condition="test.condition.final" />
      </td>
      <td v-else @click="viewTest()" class="prop">{{ value }}</td>
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
}>()

const router = useRouter()
const viewStore = useTestViewStore()
const groupStore = useGroupPageStore()

async function viewTest() {
  router.push({ name: 'testView' })
  await viewStore.viewNewTest(props.test.id)
}
</script>

<style>
@layer components {
  .group-test-list-item {
    @apply border-b select-none text-sm
    hover:bg-blue-50;
  }
  .group-test-list-item .prop {
    @apply cursor-pointer;
  }
}
</style>
