<template>
  <div class="group-list-container">
    <table class="table-group-list">
      <thead class="cursor-default">
        <th
          v-for="(col, idx) in groupCols"
          :key="idx"
          class="border-b-2 h-7 px-3 py-1"
          :class="col.class"
        >{{ col.label }}</th>
      </thead>
      <tbody>
        <GroupListItem
          v-for="(g, idx) in groups"
          :key="idx"
          :group="g"
          :groupCols="groupCols"
        />
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { toRef, computed } from 'vue'
// @ts-ignore
import useDataLakeStore from '@/stores/data-lake'
import GroupListItem from './GroupListItem.vue';

const props = defineProps<{
  groupType: Resp.GroupType
  groupCols: GroupCol[]
}>()

const store = useDataLakeStore()
const groupVarName = computed(() => {
  return props.groupType === 't' ? 'testGroups' : 'sampleGroups'
})
const groups = toRef(store, groupVarName.value)

</script>

<style>
@layer components {
  .group-list-container {
    @apply overflow-x-hidden overflow-y-auto overscroll-contain;
  }
  .group-list-container::-webkit-scrollbar {
    @apply opacity-0;
  }

  .table-group-list {
    @apply table-fixed w-full;
  }
  .table-group-list th.id,
  th.pid,
  td.id,
  td.pid {
    width: 10%;
  }
  .table-group-list th.stat,
  td.stat {
    width: 10%;
  }
  .table-group-list th.name,
  td.name {
    width: 60%;
  }
  .table-group-list th.num,
  td.num {
    width: 20%;
  }
}
</style>
