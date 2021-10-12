import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import registerGlobalComponents from './plugins/global-components'
import { router } from './router'
import { createPinia } from 'pinia'

const app = createApp(App)
app.use(router)
app.use(createPinia())
registerGlobalComponents(app)
app.mount('#app')
