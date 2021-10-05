import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import registerGlobalComponents from './plugins/global-components'
import {router} from './router'

const app = createApp(App)
app.use(router)
registerGlobalComponents(app)
app.mount('#app')
