import { InjectionKey, Ref } from 'vue'


export interface StringSetterFunc {
  (q: string): void
}

export interface VoidFunc {
  (): void
}

/* Used in test searching */
export const QueryKey: InjectionKey<Ref<string>> = Symbol('QueryKey')
export const UpdateQueryKey: InjectionKey<StringSetterFunc> = Symbol('UpdateQueryKey')

/* Used in test filtering */
export const TogglePanelKey: InjectionKey<VoidFunc> = Symbol('TogglePanelKey')
export const DisablePanelKey: InjectionKey<VoidFunc> = Symbol('DisablePanelKey')
