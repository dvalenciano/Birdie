<template>
  <div>
  <b-button id="show-btn" @click="$bvModal.show(commentId)">Delete Comment</b-button>

  <b-modal :id="commentId" hide-footer>
    <template #modal-title>
     Delete?
    </template>
    <div class="d-block text-center">
      <h3>Are you sure you want to delete this comment?</h3>
    </div>
    <b-button class="mt-3" block @click="deleteComment">Delete Comment</b-button>
    </b-modal>
</div>
</template>

<script>
import axios from 'axios'
import {BASE_URL} from '../globals'
  export default {
    name: "CommentDelete",
    props: ['commentId'],
   methods: {
      deleteComment() {
        console.log(this.commentId)
      axios.delete(`${BASE_URL}/comments/${this.commentId}`)
      this.$bvModal.hide(this.commentId)
      location.reload()
    }
    }
  }
</script>