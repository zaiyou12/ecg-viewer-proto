<template>
  <div class="flex justify-center">
    <svg
      viewBox="0 0 100 100"
      xmlns="http://www.w3.org/2000/svg"
      class="h-3 w-3"
      :fill="whichColor(finalCondition)"
    >
      <circle cx="50" cy="50" r="50" />
    </svg>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  finalCondition: EcgTest.ConditionType
}>()

function whichColor(finalStatus: EcgTest.ConditionType): string {
  if (finalStatus === 'normal') return '#3CB371'
  if (finalStatus === 'abnormal') return '#FF6347'
  else return '#808080'
}
</script>
