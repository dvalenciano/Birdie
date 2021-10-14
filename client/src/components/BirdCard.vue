<template>
  <div>
    <b-card bg-variant="light" :header="post.username" class="text-center">
        <b-card-text>{{post.post}}</b-card-text>
        <DeletePop :postId="post.id" :key="post.id"/>
    </b-card>
  </div>
</template>

<script>
import DeletePop from './DeletePop.vue'
export default {
  components: {DeletePop},
  name: 'PostCard',
  props: ['post'],
  methods: {
  }
}
</script>