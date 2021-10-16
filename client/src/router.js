import VueRouter from 'vue-router'
import HomePage from './pages/HomePage'
import CommentPage from './pages/CommentPage'
// import About from './pages/About'

const routes = [
  { path: '/', component: HomePage, name: 'HomePage' },
  { path: '/comments', component: CommentPage, name: 'CommentPage' }
]

export default new VueRouter({ routes, mode: 'history' })
