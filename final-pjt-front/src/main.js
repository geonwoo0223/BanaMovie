import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueMoment from 'vue-moment'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VModal from 'vue-js-modal'

// import './assets/css/mycss.css'
require('@/assets/css/mycss.css') 


// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.use(VModal)


Vue.config.productionTip = false
Vue.use(VueMoment)

const truncate = function (text, length, clamp) {
  clamp = clamp || '...'
  const node = document.createElement('div')
  node.innerHTML = text
  const content = node.textContent
  return content.length > length ? content.slice(0, length) + clamp : content
}
Vue.filter('truncate', truncate)

const halfStar = function (rate) {
  return rate/2
}
Vue.filter('half', halfStar)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

