<template>
  <Spinner :loading="store.loading" />
  <GroupAdder :show="showAdder" />
  <GroupRemover :show="showRemover" />
  <PageHeader>
    <GroupHeader
      :title="title"
      :groupType="groupType"
      @showAdder="showAdder = true"
      @showRemover="showRemover = true"
    />
  </PageHeader>
  <div class="h-16 w-full"></div>
  <div class="group-list-viewer">
    <GroupList
      class="w-1/2 pr-5"
      :groupType="groupType"
      :groupCols="groupCols"
    />
    <GroupDetail v-if="store.selectedGroupId" class="w-1/2" />
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, provide } from 'vue'
import PageHeader from '@/components/PageHeader.vue'
import GroupHeader from '@/components/Group/GroupHeader.vue'
import GroupAdder from '@/components/Group/GroupAdder.vue'
import GroupRemover from '@/components/Group/GroupRemover.vue'
import GroupList from '@/components/Group/GroupList.vue'
import GroupDetail from '@/components/Group/GroupDetail.vue'
import useGroupPageStore from '../../stores/group-page'
import { DisablePanelKey } from '../../symbols/symbols'

const props = defineProps<{
  title: string
  groupType: Resp.GroupType
  groupCols: GroupCol[]
}>()

const store = useGroupPageStore()

onMounted(() => {
  store.resetGroupPage()
  store.type = props.groupType
})

const showAdder = ref(false)
const showRemover = ref(false)
const disablePanel = () => {
  showAdder.value = false
  showRemover.value = false
}
provide(DisablePanelKey, disablePanel)
</script>

<style>
@layer components {
  .group-list-viewer {
    height: calc(100% - 7rem);
    @apply flex w-full px-10 my-5
    overflow-y-hidden;
  }
}
</style>
