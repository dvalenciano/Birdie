<template>
  <nav>
    <div class="nav-bar">
    <b-nav class="logo-text">
          <div class="grid-container">
            <h3 class="nav-h2">Birdie</h3>
        
          </div>
        
        </b-nav>
    <router-link to="/">Home</router-link>
    <router-link to="/comments">Comments</router-link>
    <router-link to="/locations">Locations</router-link>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Nav'
}
</script>

<style scoped></style>