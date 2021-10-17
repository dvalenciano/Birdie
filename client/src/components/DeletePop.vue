<template>
  <div>
  <b-button class="delete-button" id="show-btn" @click="$bvModal.show(birdId)">Delete Bird</b-button>

  <b-modal :id="birdId" hide-footer>
    <template #modal-title>
     Delete?
    </template>
    <div class="d-block text-center">
      <h3>Are you sure you want to delete this bird?</h3>
    </div>
    <b-button class="mt-3" block @click="deleteBird">Delete Bird</b-button>
    </b-modal>
</div>
</template>

<script>
import axios from 'axios'
import {BASE_URL} from '../globals'
  export default {
    name: "DeletePop",
    props: ['birdId'],
   methods: {
      deleteBird() {
        console.log(this.birdId)
      axios.delete(`${BASE_URL}/birds/${this.birdId}`)
      this.$bvModal.hide(this.birdId)
      location.reload()
    }
    }
  }
</script>