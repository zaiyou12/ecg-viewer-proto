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

export const TogglePanelKey: InjectionKey<VoidFunc> = Symbol('TogglePanelKey')
export const EnablePanelKey: InjectionKey<VoidFunc> = Symbol('EnablePanelKey')
export const DisablePanelKey: InjectionKey<VoidFunc> = Symbol('DisablePanelKey')
