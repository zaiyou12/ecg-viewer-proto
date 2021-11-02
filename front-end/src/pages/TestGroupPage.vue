<template>
  <Spinner :loading="store.loading" />
  <GroupAdder :show="showAdder" />
  <GroupRemover :show="showRemover" />
  <PageHeader>
    <div class="text-2xl font-bold pl-5">Test Groups</div>
    <div class="text-sm ml-5">Add or remove test groups</div>
    <div>
      <button class="mx-5 group-modify-btn">
        <SvgIcon class="h-5 w-5" name="PlusSm" @mouseup="showAdder = true" />
      </button>
      <button class="group-modify-btn">
        <SvgIcon class="h-5 w-5" name="MinusSm" @mouseup="showRemover = true" />
      </button>
    </div>
  </PageHeader>
  <div class="h-16 w-full"></div>
  <div class="group-list-viewer">
    <GroupList class="w-1/2 pr-5" />
    <GroupTestList v-if="store.selectedGroupId" class="w-1/2" />
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, provide } from 'vue'
import PageHeader from '@/components/PageHeader.vue'
import GroupAdder from '@/components/TestGroup/GroupAdder.vue'
import GroupRemover from '@/components/TestGroup/GroupRemover.vue'
import GroupList from '@/components/TestGroup/GroupList.vue'
import GroupTestList from '@/components/TestGroup/GroupTestList.vue'
import useGroupPageStore from '../stores/group-page'
import { DisablePanelKey } from '../symbols/symbols'

const store = useGroupPageStore()
onMounted(() => {
  store.resetGroupPage()
  store.type = 't'
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
  .group-modify-btn {
    @apply px-1 py-1 rounded-lg
    bg-blue-400 text-white font-bold
    hover:bg-blue-300;
  }

  .group-list-viewer {
    height: calc(100% - 7rem);
    @apply flex w-full px-10 my-5
    overflow-y-hidden;
  }
}
</style>
