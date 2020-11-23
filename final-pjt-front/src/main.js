import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueMoment from 'vue-moment'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VModal from 'vue-js-modal'

import './assets/css/mycss.css'

// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.use(VModal)


Vue.config.productionTip = false
Vue.use(VueMoment)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

