<template>
  <div>
    <b-card bg-variant="light" :header="bird.bird_type" class="text-center">
        <b-card-text>{{bird.bird}}</b-card-text>
        <DeletePop :birdId="bird.id" :key="bird.id"/>
        <UpdateModal :birdId="bird.id" :key="bird.id" />
    </b-card>
  </div>
</template>

<script>
import DeletePop from './DeletePop.vue'
export default {
  components: {DeletePop},
  name: 'BirdCard',
  props: ['bird'],
  methods: {
  }
}
</script>