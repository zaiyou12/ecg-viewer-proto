<template>
  <Modal :showModal="show">
    <div class="flex">
      <p>Group Name</p>
      <input type="text" class="border" v-model="newGroupName" />
    </div>
    <div class="flex items-center">
      <p>Group Status</p>
      <input
        type="radio"
        id="group-open"
        value="open"
        v-model="newGroupStatus"
        checked
      />
      <label for="group-open">Open</label>
      <input
        type="radio"
        id="group-closed"
        value="closed"
        v-model="newGroupStatus"
      />
      <label for="group-closed">Closed</label>
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

const newGroupName = ref('')
const newGroupStatus = ref('open')

async function addGroup() {
  if (newGroupName.value.length === 0) return
  await store.addGroup(newGroupName.value, newGroupStatus.value as GroupStatus)
  disablePanel!()
}
</script>
