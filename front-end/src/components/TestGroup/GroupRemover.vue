<template>
  <Modal :showModal="show">
    <div class="flex">
      <p>Group ID</p>
      <input type="text" class="border" v-model="removeGroupId" />
    </div>
    <button class="border" @mouseup="addGroup">Confirm</button>
    <button class="border" @mouseup="disablePanel">Cancel</button>
  </Modal>
</template>

<script setup lang="ts">
import { ref, inject } from 'vue'
import Modal from '@/components/Modal.vue'
import useGroupPageStore from '../../stores/group-page'
import { DisablePanelKey } from '../../symbols/symbols'

const props = withDefaults(defineProps<{ show: boolean }>(), { show: false })
const store = useGroupPageStore()

const disablePanel = inject(DisablePanelKey)

const removeGroupId = ref()

async function addGroup() {
  if (removeGroupId.value < 1) return
  await store.delGroup(removeGroupId.value)
  disablePanel!()
}
</script>
