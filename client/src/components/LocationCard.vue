<template>
  <div>
    <b-card bg-variant="light" :header="location.bird_type" class="text-center">
        <b-card-text>{{location.location}}</b-card-text>
        <div>
          <LocationDelete :locationId="location.id" />
        </div>
    </b-card>
  </div>
</template>

<script>
import LocationDelete from './LocationDelete.vue'
export default {
  components: { LocationDelete },
  name: 'LocationCard',
  props: ['location'],
  methods: {
  }
}
</script>