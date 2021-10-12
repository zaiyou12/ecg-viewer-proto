<template>
  <transition name="drop" appear>
    <div v-if="showDrop" class="drop-overlay">
      <ul class="select-none">
        <li v-for="idx in numGroups" :key="idx"
          class="flex items-center h-8 hover:bg-blue-50"
        >
          <input type="checkbox" :id="`group${idx}`"
            class="mx-2 h-full hover:bg-blue-50"
          >
          <div class="h-full w-full flex items-center hover:bg-blue-50" >
            <label :for="`group${idx}`" class="text-left w-full whitespace-nowrap">
              Group {{ idx }}
            </label>
          </div>
        </li>
      </ul>
    </div>
  </transition>
</template>

<script lang="ts" setup>
const props = defineProps<{
  type: 'Preprocess' | 'Test' | 'Sample'
  showDrop: boolean
}>()

const numGroups = 10

// function groupChecked(idx: number) {
//   (document.getElementById(`group${idx}`) as HTMLInputElement).checked = !(document.getElementById(`group${idx}`) as HTMLInputElement).checked
// }
</script>

<style>
@layer components {
  .drop-overlay {
    width: 14.8%;
    z-index: 98;
    @apply absolute h-40 ml-2
      overflow-auto overscroll-none
    bg-gray-50 rounded-xl
  }

  .drop-enter-active {
    @apply transition-opacity duration-200 ease-out

  }

  .drop-leave-active {
    @apply transition-opacity duration-200
  }

  .drop-enter-from, .drop-leave-to {
    @apply opacity-0
  }
}
</style>
