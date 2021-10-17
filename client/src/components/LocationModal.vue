<template>
  <div>
    <div>
      <b-button v-b-modal.modal-prevent-closing class="post-button">Note Location</b-button>

      <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="Log Your Notes"
      hide-footer
      >
      <b-form ref="form" @submit="newLocation">
        <b-form-group
          label="Bird Name"
          label-for="bird-input"
          invalid-feedback="Bird Info is required"
          
        >
          <b-form-input
            id="bird-input" 
            
            v-model="bird"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group label="Location" label-for="location-input" invalid-feedback="Content is required" >
          <b-form-input id="location-input" v-model="location" ></b-form-input>
        </b-form-group>

        <b-form-group label="Notes" label-for="note-input" invalid-feedback="Content is required" >
          <b-form-input id="note-input" v-model="note" ></b-form-input>
        </b-form-group>

      <b-button class="mt-3" block @click="newLocation">Add Notes</b-button>
      </b-form>
    </b-modal>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {BASE_URL} from '../globals'
export default {
  name: 'LocationModal',
  data: () =>({
    bird_type: '',
    location: '',
    note: ''
  }),
  
  methods: {
      async newLocation(){
        const res = await axios.post(`${BASE_URL}/locations`, 
        {
          bird_type: this.bird,
          location: this.location,
          note: this.note
        })
        this.bird = ''
        this.location = ''
        this.note = ''
        location.reload()
        return res
      }
  }
}
</script>