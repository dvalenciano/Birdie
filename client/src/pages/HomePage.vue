<template>
  <div>
    <h2>Birds</h2>
    <Modal />
    <section>
      <BirdCard v-for="bird in birds" :bird="bird" :key="bird.id" />
    </section>
  </div>
</template>


<script>
import axios from 'axios'
import BirdCard from '../components/BirdCard.vue'
import { BASE_URL } from '../globals'
import Modal from '../components/Modal.vue'
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
    }
  }
}
</script>