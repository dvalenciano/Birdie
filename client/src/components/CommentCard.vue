<template>
  <div>
    <b-card bg-variant="light" :header="comment.bird_type" class="text-center">
        <b-card-text>{{comment.comment}}</b-card-text>
        <div>
          <CommentDelete :commentId="comment.id" />
        </div>
    </b-card>
  </div>
</template>

<script>
import CommentDelete from './CommentDelete.vue'
export default {
  components: { CommentDelete},
  name: 'CommentCard',
  props: ['comment'],
  methods: {
  }
}
</script>