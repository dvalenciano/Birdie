<template>
  <div>
    <div>
      <div class="nav-bar">
        <b-nav class="logo-text">
          <div class="grid-container">
            <!-- <img class="gear-logo" src="../assets/gear5.gif"> -->
            <h3 class="nav-h2">Birdie</h3>
            <!-- <h4 class="nav-h3">What bird did you see?</h4> -->
        
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
      <BirdCard v-for="post in posts" :post="post" :key="post.id" />
    </section>
    <section v-else>
      <BirdCard v-for="post in searchResults" :post="post" :username="username" :key="post.id" />
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
    posts: [],
    searchQuery: '',
    searchResults: [],
    searched: false
  }),
  mounted: function() {
    this.getPosts()
  },
  methods: {
    async getPosts() {
      const res = await axios.get(`${BASE_URL}/post`)
      this.posts = res.data
    },
   
    getSearchResults(){
      let posts = this.posts
      let result = posts.filter(post => post.post.includes(this.searchQuery))
      console.log(result)
      this.searchResults = result
      this.searched = true
    }
  }
}
</script>