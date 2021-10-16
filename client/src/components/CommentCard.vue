<template>
  <div>
    <b-card bg-variant="light" :header="comment.comment" class="text-center">
        <b-card-text>{{comment.comment}}</b-card-text>
        <div>
          <CommentDelete :commentId="comment.id" />
        </div>
        <div>
          <CommentModal :commentId="comment.id" />
        </div>
    </b-card>
  </div>
</template>

<script>
// import DeletePop from './DeletePop.vue'
import CommentModal from './CommentModal.vue'
export default {
  components: { CommentModal},
  name: 'CommentCard',
  props: ['comment'],
  methods: {
  }
}
</script>