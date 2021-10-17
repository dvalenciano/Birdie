<template>
  <nav>
    <div class="nav-bar">
    <b-nav class="logo-text">
          <div class="grid-container">
            <img class="birdie-logo" src="../assets/parrotlogo.png">
            <h3 class="nav-h2">Birdie</h3>
        
          </div>
        
        </b-nav>
        <div class="nav-right">
    <router-link to="/">Home</router-link>
    <router-link to="/comments">Comments</router-link>
    <router-link to="/locations">Locations</router-link>
        </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Nav'
}
</script>

<style scoped></style>