<template>
  <div>
    <h2>Bird Comments</h2>
    <CommentModal />
    <section>
      <CommentCard v-for="comment in comments" :comment="comment" :key="comment.id" />
    </section>
  </div>
</template>


<script>
import axios from 'axios'
import CommentCard from '../components/CommentCard.vue'
import { BASE_URL } from '../globals'
import CommentModal from '../components/CommentModal.vue'
export default {
  name: 'Home',
  components: {
    CommentCard,
    CommentModal
  },
  data: () => ({
    comments: [],
    searchQuery: '',
    searchResults: [],
    searched: false
  }),
  mounted: function() {
    this.getComments()
  },
  methods: {
    async getComments() {
      const res = await axios.get(`${BASE_URL}/comments`)
      this.comments = res.data
    },
   
    getSearchResults(){
      let comments = this.comments
      let result = comments.filter(comment => comment.comment.includes(this.searchQuery))
      console.log(result)
      this.searchResults = result
      this.searched = true
    }
  }
}
</script>