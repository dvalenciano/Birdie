<template>
  <div>
    <h2>Location Notes</h2>
    <LocationModal />
    <section>
      <!-- <CommentCard v-for="comment in comments" :comment="comment" :key="comment.id" /> -->
    </section>
  </div>
</template>


<script>
import axios from 'axios'
import LocationModal from '../components/LocationModal.vue'
// import CommentCard from '../components/CommentCard.vue'
import { BASE_URL } from '../globals'
// import CommentModal from '../components/CommentModal.vue'
export default {
  name: 'Home',
  components: {
    // CommentCard,
    // CommentModal
    LocationModal
  },
  data: () => ({
    locations: [],
  }),
  mounted: function() {
    this.getLocations()
  },
  methods: {
    async getLocations() {
      const res = await axios.get(`${BASE_URL}/locations`)
      this.locations = res.data
    }
  }
}
</script>