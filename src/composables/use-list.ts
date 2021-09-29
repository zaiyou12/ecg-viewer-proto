import { ref, reactive } from 'vue'


export default function useList() {
  const listRef = ref(null);

  return {
    listRef
  }
}
