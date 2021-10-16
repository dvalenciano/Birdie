import VueRouter from 'vue-router'
import HomePage from 
import About from './pages/About'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/details/:game_id', component: GameDetails, name: 'GameDetails' },
  { path: '/genre/:genre_id', component: GameGenre, name: 'GameGenre' },
  { path: '/games', component: ViewGames, name: 'ViewGames' },
  { path: '/about', component: About, name: 'About' }
]

export default new VueRouter({ routes, mode: 'history' })
