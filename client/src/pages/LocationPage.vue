<template>
  <div>
    <h2>Location Notes</h2>
    <LocationModal />
    <section>
      <LocationCard v-for="location in locations" :location="location" :key="location.id" />
    </section>
  </div>
</template>


<script>
import axios from 'axios'
import LocationModal from '../components/LocationModal.vue'
import LocationCard from '../components/LocationCard.vue'
import { BASE_URL } from '../globals'
export default {
  name: 'LocationPage',
  components: {
    LocationModal,
    LocationCard
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