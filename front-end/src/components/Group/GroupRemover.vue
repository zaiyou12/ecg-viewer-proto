<template>
  <Modal :showModal="show">
    <div class="group-adder-remover-modal">
      <div class="flex items-center">
        <p>Group ID</p>
        <input
          type="text"
          v-model="removeGroupId"
          pattern="^[0-9]+$"
          title="Allowed: number"
        />
      </div>
      <label class="text-sm text-gray-500 mt-2">Allowed: number</label>
      <div class="mt-5">
        <button @mouseup="addGroup" :class="{ 'disabled': !isIdValid }">Confirm</button>
        <button @mouseup="disablePanel">Cancel</button>
      </div>
    </div>
  </Modal>
</template>

<script setup lang="ts">
import { ref, inject, computed } from 'vue'
import Modal from '@/components/Modal.vue'
import useGroupPageStore from '../../stores/group-page'
import { DisablePanelKey } from '../../symbols/symbols'

const props = withDefaults(defineProps<{ show: boolean }>(), { show: false })
const store = useGroupPageStore()

const disablePanel = inject(DisablePanelKey)

const removeGroupId = ref()
const isIdValid = computed(() => {
  const re = new RegExp('^[0-9]+$')
  return re.test(removeGroupId.value)
})

async function addGroup() {
  /**
   * The following commented functionality relies on disable CSS
   * If CSS is modified, the following must be turned back on
   */
  // if (!isIdValid.value) return
  // if (removeGroupId.value < 1) return
  await store.delGroup(removeGroupId.value)
  removeGroupId.value = undefined
  disablePanel!()
}
</script>
