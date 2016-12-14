import "babel-polyfill"

import Vue from 'vue'
import App from './App.vue'
import VueRouter from "vue-router";
import VueResource from 'vue-resource'
import Element from 'element-ui'

import './assets/js/main.js'

Vue.use(Element)

//开启debug模式
Vue.config.debug = true;

Vue.use(VueRouter);
Vue.use(VueResource);


import iconComponent from './components/icon.vue'
import buttonComponent from './components/button.vue'
import radioComponent from './components/radio.vue'
import chkboxComponent from './components/checkbox.vue'
import selectComponent from './components/select.vue'
import switchComponent from './components/switch.vue'
import dateComponent from './components/date.vue'
import uploadComponent from './components/upload.vue'
import formComponent from './components/form.vue'
import cardComponent from './components/card.vue'
import noticeComponent from './components/notice.vue'

let routers = [
  {
    path: '/icon',
    component: iconComponent
  },
  {
    path: '/button',
    component: buttonComponent
  },
  {
    path: '/radio',
    component: radioComponent
  },
  {
    path: '/checkbox',
    component: chkboxComponent
  },
  {
    path: '/select',
    component: selectComponent
  },
  {
    path: '/switch',
    component: switchComponent
  },
  {
    path: '/date',
    component: dateComponent
  },
  {
    path: '/upload',
    component: uploadComponent
  },
  {
    path: '/form',
    component: formComponent
  },
  {
    path: '/card',
    component: cardComponent
  },
  {
    path: '/notice',
    component: noticeComponent
  }
]

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: routers
})


const app = new Vue({
  router: router,
  render: h => h(App)
}).$mount('#app')
