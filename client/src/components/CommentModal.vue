<template>
  <div>
    <div>
      <b-button v-b-modal.modal-prevent-closing class="post-button">Log a Bird</b-button>

      <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="Log Your Bird"
      hide-footer
      >
      <b-form ref="form" @submit="newBird">
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

      <b-button class="mt-3" block @click="newBird">Submit</b-button>
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
  data: () =>({
    bird_type: '',
    color: ''
  }),
  
  methods: {
      async newcomment(){
        const res = await axios.post(`${BASE_URL}/birds`, 
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