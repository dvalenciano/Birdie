<template>
  <div>
    <div>
      <b-button v-b-modal.modal-prevent-closing class="post-button">Comment on a bird</b-button>

      <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="Log Your comment"
      hide-footer
      >
      <b-form ref="form" @submit="newComment">
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

        <b-form-group label="Comment" label-for="comment-input" invalid-feedback="Content is required" >
          <b-form-input id="comment-input" v-model="comment" ></b-form-input>
        </b-form-group>

      <b-button class="mt-3" block @click="newComment">Add Comment</b-button>
      </b-form>
    </b-modal>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {BASE_URL} from '../globals'
export default {
  name: 'CommentModal',
  data: () =>({
    bird_type: '',
    comment: ''
  }),
  
  methods: {
      async newComment(){
        const res = await axios.post(`${BASE_URL}/comments`, 
        {
          bird_type: this.bird,
          comment: this.comment
        })
        this.bird = ''
        this.comment = ''
        location.reload()
        return res
      }
  }
}
</script>