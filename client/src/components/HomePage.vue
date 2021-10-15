<template>
  <div>
    <div>
      <div class="nav-bar">
        <b-nav class="logo-text">
          <div class="grid-container">
            <h3 class="nav-h2">Birdie</h3>
        
          </div>
        
        </b-nav>
        <form v-on:submit="getSearchResults" @submit.prevent>
          <b-input-group class="mt-1">
            <template #append >
              <b-button type="submit">Search</b-button>
            </template>
            <b-form-input type="search" sm="3" v-model="searchQuery" :value='searchQuery'></b-form-input>
          </b-input-group>
        </form>
      </div>
      
    </div>
    <h2>Birds</h2>
    <Modal />
    <section v-if="searched === false">
      <BirdCard v-for="bird in birds" :color="color" :key="bird.id" />
    </section>
    <section v-else>
      <BirdCard v-for="bird in searchResults" :color="color" :bird="bird" :key="bird.id" />
    </section>
  </div>
</template>


<script>
import axios from 'axios'
import BirdCard from './BirdCard.vue'
import { BASE_URL } from '../globals'
import Modal from './Modal.vue'
// import { b-nav } from 'bootstrap-vue'
export default {
  name: 'Home',
  components: {
    BirdCard,
    Modal
  },
  data: () => ({
    birds: [],
    searchQuery: '',
    searchResults: [],
    searched: false
  }),
  mounted: function() {
    this.getBirds()
  },
  methods: {
    async getBirds() {
      const res = await axios.get(`${BASE_URL}/birds`)
      this.birds = res.data
    },
   
    getSearchResults(){
      let birds = this.birds
      let result = birds.filter(bird => bird.bird.includes(this.searchQuery))
      console.log(result)
      this.searchResults = result
      this.searched = true
    }
  }
}
</script>