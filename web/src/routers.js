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
import HomeComponent from './components/home.vue'
import BlogsComponent from './components/blogs.vue'
import InfosComponent from './components/infos.vue'
import DetailComponent from './components/detail.vue'
import AboutComponent from './components/about.vue'

let routers = [
  {
    path: '/',
    component: HomeComponent
  },
  {
    path: '/about',
    component: AboutComponent
  },
  {
    path: '/infos',
    component: InfosComponent
  },
  {
    path: '/blogs',
    component: BlogsComponent
  },
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
  },
  {
    path: '/detail/:uid',
    component: DetailComponent
  }
]

export default routers;
