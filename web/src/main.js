import "babel-polyfill"

import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import Element from 'element-ui'
import routers from './routers'

import './assets/js/main.js'

Vue.use(Element)

//开启debug模式
Vue.config.debug = true;

Vue.use(VueRouter);
Vue.use(VueResource);

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: routers
})

const app = new Vue({
  router: router,
  render: h => h(App)
}).$mount('#app')
