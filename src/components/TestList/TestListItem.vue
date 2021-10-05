<template>
  <tr>
    <td>{{ testSeq }}</td>
    <td>{{ sampled }}</td>
    <td>{{ normal }}</td>
  </tr>
  <!-- <li class="text-left w-full p-2 break-all truncate border-t border-gray-300">
    {{ testSeq }}
  </li> -->
</template>

<script lang="ts" setup>
// import { withDefaults } from 'vue'

interface TestListItemProps {
  testSeq: string
  sampled?: boolean
  normal?: boolean
  index?: number
}

const props = withDefaults(defineProps<TestListItemProps>(), {
  sampled: false,
  normal: false
})
</script>
