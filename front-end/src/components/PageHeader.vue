<template>
  <div class="page-header-container">
    <div class="page-header-content">
      <slot></slot>
    </div>
  </div>
</template>

<script lang="ts" setup>
</script>

<style>
@layer components {
  .page-header-container {
    z-index: 97;
    min-width: 1024px;
    @apply fixed left-0 top-0 right-52 h-16
      transform translate-x-52
      bg-white;
  }

  .page-header-container div.page-header-content {
    @apply h-full flex items-center
    mx-5 border-b-2 border-gray-100
    select-none;
  }
}
</style>
