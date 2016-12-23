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
    path: '/infos/:uid',
    component: DetailComponent
  },
  {
    path: '/blogs',
    component: BlogsComponent
  },
  {
    path: '/blogs/:uid',
    component: DetailComponent
  }
]

export default routers;
