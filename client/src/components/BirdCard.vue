<template>
  <div>
    <b-card bg-variant="light" :header="bird.bird_type" class="text-center">
        <b-card-text>{{bird.bird}}</b-card-text>
        <div>
          <DeletePop :birdId="bird.id" />
        </div>
        <div>
          <UpdateModal :birdId="bird.id" />
        </div>
    </b-card>
  </div>
</template>

<script>
import DeletePop from './DeletePop.vue'
import UpdateModal from './UpdateModal.vue'
export default {
  components: {DeletePop, UpdateModal},
  name: 'BirdCard',
  props: ['bird'],
  methods: {
  }
}
</script>