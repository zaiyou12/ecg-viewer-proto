<template>
  <transition name="fade" appear>
    <div v-if="showModal">
      <div class="modal">
        <slot></slot>
      </div>
      <div class="modal-overlay" @click="disableModal"></div>
    </div>
  </transition>
</template>

<script setup lang="ts">

interface ModalProps {
  showModal?: boolean
}

const props = withDefaults(defineProps<ModalProps>(), {
  showModal: false
})

const emits = defineEmits<{
  (e: 'update:showModal', value: boolean): void
}>()

function disableModal() {
  emits('update:showModal', false)
}
</script>

<style>
@layer components {
  .modal {
    z-index: 99;
    @apply absolute top-1/2 left-1/2
    transform -translate-y-1/2 -translate-x-1/4
    w-1/4 h-52 bg-white opacity-100
    rounded-2xl border shadow;
  }

  .modal-overlay {
    z-index: 98;
    width: calc(100vw - 13rem);
    height: 100vh;
    @apply absolute opacity-10 bg-gray-400;
  }

  .fade-enter-active {
    @apply transition-opacity duration-300 ease-out;
  }

  .fade-leave-active {
    @apply transition-opacity duration-300;
  }

  .fade-enter-from,
  .fade-leave-to {
    @apply opacity-0;
  }
}
</style>
