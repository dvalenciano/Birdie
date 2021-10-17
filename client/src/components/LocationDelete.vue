<template>
  <div>
  <b-button class="delete-button" id="show-btn" @click="$bvModal.show(locationId)">Delete Note</b-button>

  <b-modal :id="locationId" hide-footer>
    <template #modal-title>
     Delete Note?
    </template>
    <div class="d-block text-center">
      <h3>Are you sure you want to delete this Note?</h3>
    </div>
    <b-button class="mt-3" block @click="deleteLocation">Delete Note</b-button>
    </b-modal>
</div>
</template>

<script>
import axios from 'axios'
import {BASE_URL} from '../globals'
  export default {
    name: "LocationDelete",
    props: ['locationId'],
   methods: {
      deleteLocation() {
      axios.delete(`${BASE_URL}/locations/${this.locationId}`)
      this.$bvModal.hide(this.locationId)
      location.reload()
    }
    }
  }
</script>