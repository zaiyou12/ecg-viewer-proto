import { InjectionKey, Ref } from 'vue'

/* Used in test searching */
export const QueryKey: InjectionKey<Ref<string>> = Symbol('QueryKey')
export interface UpdateQueryFunc {
  (q: string): void
}
export const UpdateQueryKey: InjectionKey<UpdateQueryFunc> = Symbol('UpdateQueryKey')
