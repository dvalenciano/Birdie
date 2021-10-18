<template>
  <nav>
    <div class="nav-bar">
    <b-nav class="logo-text">
          <div class="grid-container">
            <img class="birdie-logo" src="../assets/parrotlogo.png">
            <h2 class="nav-h2">Birdie</h2>
        
          </div>
        
        </b-nav>
        <div class="nav-right"><div>
    <router-link style="text-decoration: none; font-size: 30px; color: inherit;" to="/">Welcome |  </router-link>
          </div>
          <div>
    <router-link style="text-decoration: none; font-size: 30px; color: inherit;" to="/birds">Birds |  </router-link>
          </div>
          <div>
    <router-link style="text-decoration: none; font-size: 30px; color: inherit;" to="/comments">  Comments |  </router-link>
          </div>
          <div>
    <router-link style="text-decoration: none; font-size: 30px; color: inherit;" to="/locations">  Locations  </router-link>
          </div>
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