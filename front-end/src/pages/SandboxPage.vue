<template>
  <div class="h-full">
    <Modal v-model:showModal="btnClicked" />
    <p class="py-3">This is a sandbox page.</p>
    <input class="border-2 mb-3"
      type="text"
      v-model="inputText"
    >
    <p>Typed: {{ inputText }}</p>
    <div class="py-3">
      <SvgIconButton icon="InformationCircle" :text="btnText"
        @click="btnClick"
        class="border-2 border-blue-400"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import SvgIconButton from '@/components/SvgIconButton.vue'
import Modal from '@/components/Modal.vue'
import TestFilterPanel from '@/components/TestFilterPanel/index.vue'


const inputText = ref('')

////////////////////////////////
const btnText = "Click Me"
const btnClicked = ref(false)

function btnClick(e: Event): void {
  inputText.value = "Clicked"
  btnClicked.value= true
}
</script>
