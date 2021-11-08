<template>
  <Modal :showModal="show">
    <div class="group-adder-remover-modal">
      <div class="flex items-center">
        <p>Group Name</p>
        <input
          type="text"
          v-model="newGroupName"
          pattern="^[a-zA-Z_\-0-9]+$"
          title="Allowed: underscore, hyphen, alphabet, numbers."
        />
      </div>
      <label
        class="text-sm text-gray-500 mt-2"
      >Allowed: alphabet, number, underscore, hyphen</label>
      <div class="flex items-center mt-5">
        <p>Group Status</p>
        <div class="mr-8">
          <input
            type="radio"
            id="group-open"
            value="open"
            v-model="newGroupStatus"
            checked
          />
          <label for="group-open">Open</label>
        </div>
        <div>
          <input
            type="radio"
            id="group-closed"
            value="closed"
            v-model="newGroupStatus"
          />
          <label for="group-closed">Closed</label>
        </div>
      </div>
      <div class="mt-5 flex justify-center">
        <button
          @mouseup="addGroup"
          :class="{ 'cursor-not-allowed': !isNameValid }"
        >Confirm</button>
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

const newGroupName = ref('')
const newGroupStatus = ref('open')
const isNameValid = computed(() => {
  const re = new RegExp('^[a-zA-Z_\\-0-9]+$')
  return re.test(newGroupName.value)
})

async function addGroup() {
  if (!isNameValid.value) return
  if (newGroupName.value.length === 0) return
  await store.addGroup(newGroupName.value, newGroupStatus.value as GroupStatus)
  disablePanel!()
}
</script>

<style>
@layer components {
  .group-adder-remover-modal {
    @apply flex flex-col justify-center items-center h-full;
  }
  .group-adder-remover-modal p {
    @apply font-bold mr-2;
  }
  .group-adder-remover-modal input[type="text"] {
    @apply border px-2 py-1 outline-none;
  }
  .group-adder-remover-modal input[type="text"]:invalid {
    @apply bg-red-200;
  }
  .group-adder-remover-modal input[type="radio"] {
    @apply mr-2;
  }
  .group-adder-remover-modal button {
    @apply w-20 h-8 px-2 mx-2 rounded-lg
    text-white font-bold
    bg-blue-400 hover:bg-blue-300;
  }
}
</style>
