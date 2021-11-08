import AppLink from './AppLink.vue'
import SvgIcon from './SvgIcon.vue'
import Spinner from './Spinner.vue'
import type { App } from 'vue'

export default function registerGlobalComponents(app: App): void {
  app.component('AppLink', AppLink)
  app.component('SvgIcon', SvgIcon)
  app.component('Spinner', Spinner)
}
