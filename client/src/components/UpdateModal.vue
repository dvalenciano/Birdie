<template>
  <div>
    <div>
      <b-button id="update-btn" @click="$bvModal.show(birdId)" class="post-button">Update Bird</b-button>

      <b-modal
      :id="birdId"
      ref="modal"
      title="Update Your Bird"
      hide-footer
      >
      <b-form ref="form" @submit="updateBird">
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

        <b-form-group label="Bird Color" label-for="color-input" invalid-feedback="Content is required" >
          <b-form-input id="color-input" v-model="color" ></b-form-input>
        </b-form-group>

      <b-button class="mt-3" block @click="updateBird">Update</b-button>
      </b-form>
    </b-modal>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {BASE_URL} from '../globals'
export default {
  name: 'Modal',
  props: ['birdId'],
  data: () =>({
    bird: '',
    color: ''
  }),
  
  methods: {
      async updateBird(){
          console.log(this.birdId)
        const res = await axios.put(`${BASE_URL}/birds/${this.birdId}`, 
        {
          bird_type: this.bird,
          color: this.color
        })
        this.bird = ''
        this.color = ''
        location.reload()
        return res
      }
  }
}
</script>