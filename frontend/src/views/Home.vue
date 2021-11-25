<template>
  <div>
      <Drawer/>      
      <v-main>
        <h1>Welcome!</h1>
      </v-main>       
  </div>
</template>

<script>
import Drawer from '../components/Drawer.vue'
export default {
  name: 'Home',
  components: {
    Drawer,
  }
}
</script>