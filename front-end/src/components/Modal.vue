<template>
<transition name="fade" appear>
  <div v-if="showModal" class="modal-overlay" @click="disableModal">
    <!-- <div class="modal"></div> -->
    <!-- <SvgIconButton -->
  </div>
</transition>
</template>

<script setup lang="ts">
import SvgIconButton from '@/components/SvgIconButton.vue'

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
    @apply fixed top-1/2 left-1/2
      transform -translate-y-1/2 -translate-x-1/2
      w-full bg-white
  }

  .modal-overlay {
    z-index: 98;
    @apply absolute w-full h-full
    bg-black bg-opacity-30
  }

  .fade-enter-active {
    @apply transition-opacity duration-300 ease-out
  }

  .fade-leave-active {
    @apply transition-opacity duration-300
  }

  .fade-enter-from, .fade-leave-to {
    @apply opacity-0
  }
}
</style>
