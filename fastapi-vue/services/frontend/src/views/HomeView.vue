<template>
  <section class="home-section">
    <h1>Welcome to My App</h1>
    <p>This is a simple app built with FastAPI and Vue.js.</p>
    <p>Start by registering or logging in to explore the features!</p>

    <footer class="footer">
      <p>{{ customText }}</p>
    </footer>
  </section>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'Home-layout',
  data() {
    return {
      customText: 'Your custom text goes here!',
    };
  },
});
</script>

<style scoped>
.home-section {
  margin-top: 200px;
  /* Add margin to create space */
}

.footer {
  margin-top: 20px;
  text-align: center;
  color: #777;
}
</style>
