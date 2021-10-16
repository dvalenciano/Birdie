<template>
  <div id="app">
    <header>
      <Nav/>
    </header>
    <main>
      <router-view ></router-view>
    </main>
  </div>
</template>

<script>
// imports go here
import HomePage from './pages/HomePage.vue'

export default {
  name: 'App',
  components: {
    HomePage
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>
