<template>
  <div>
    <Drawer/>
    <v-main>      
      <div class="organization-items">
        <v-flex d-flex>
          <v-layout wrap>
              <v-flex md3 v-for="item in this.items" :key="item.id">
                  <v-card>
                    <img :src='item.logo'/>
                    <v-card-title>{{ item.name }}</v-card-title>
                    <v-card-text>{{ item.description }}</v-card-text>
                  </v-card>
                  <br>
              </v-flex>
          </v-layout>
        </v-flex>
      </div>
    </v-main>
  </div>

</template>

<script>
import axios from 'axios';
import Drawer from '../components/Drawer.vue'

export default {
  name: 'Organization',
  components: {
    Drawer,
  },
  data() {
    return {
      items: [],
    }
  },
  methods: {
    getItems: function () {
      axios.get('http://127.0.0.1:8000/api/organization')
      .then( response => {
          this.items = response.data;
      });
    }
  },
  created () {
    this.getItems();
  }
}
</script>