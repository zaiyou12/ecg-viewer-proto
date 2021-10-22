import { InjectionKey, Ref } from 'vue'

export interface NumberSetterFunc {
  (x: number): void
}

export interface StringSetterFunc {
  (x: string): void
}

export interface VoidFunc {
  (): void
}

/* Used in test filtering */
export const TogglePanelKey: InjectionKey<VoidFunc> = Symbol('TogglePanelKey')
export const DisablePanelKey: InjectionKey<VoidFunc> = Symbol('DisablePanelKey')
