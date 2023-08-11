<template>
  <div id="app">
    <NavBar />
    <div class="main container">
      <router-view />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from '@/components/NavBar.vue'
export default {
  components: {
    NavBar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #072f59;
}

body {
  margin: 0;
  padding: 0;
  background-color: #dae8e6;
  /* Adjust the path to your image */
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}
</style>