<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  data() {
    return {

    };
  },
  methods: {

  },
  mounted() {
      
  },
})
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-primary">
    <div class="container-fluid">
      <a class="navbar-brand me-5" href="#">Weather Nest</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <router-link to="/" class="nav-link">Home</router-link>
          <router-link to="/measurements" class="nav-link">Measurements</router-link>
          <router-link to="/configurate" class="nav-link">Configurate</router-link>
        </div>
      </div>
    </div>
  </nav>


</template>

<style lang="scss">
$navbar-text-color: rgb(235, 235, 235);
.navbar {
  .nav-link, .navbar-brand  {
    color: $navbar-text-color;
    margin-right: 20px;
  }
}
</style>