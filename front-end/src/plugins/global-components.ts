import AppLink from './AppLink.vue'
import SvgIcon from './SvgIcon.vue'
import type { App } from 'vue'

export default function registerGlobalComponents (app: App): void {
  app.component('AppLink', AppLink)
  app.component('SvgIcon', SvgIcon)
}
