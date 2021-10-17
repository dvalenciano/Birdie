import VueRouter from 'vue-router'
import Home from './pages/Home'
import HomePage from './pages/HomePage'
import CommentPage from './pages/CommentPage'
import LocationPage from './pages/LocationPage'
// import About from './pages/About'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/birds', component: HomePage, name: 'HomePage' },
  { path: '/comments', component: CommentPage, name: 'CommentPage' },
  { path: '/locations', component: LocationPage, name: 'LocationPage' }
]

export default new VueRouter({ routes, mode: 'history' })
