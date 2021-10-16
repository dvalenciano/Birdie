import VueRouter from 'vue-router'
import HomePage from './pages/HomePage'
import About from './pages/About'

const routes = [
  { path: '/', component: HomePage, name: 'HomePage' },
  { path: '/about', component: About, name: 'About' }
]

export default new VueRouter({ routes, mode: 'history' })
