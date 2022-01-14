<template>
  <div>
    <Drawer/>
    <v-main>
      <v-row>
        <v-col cols="12" sm="3" md="4" v-for="item in this.items" :key="item.id" >
            <ul>
              <li>{{ item.id }}</li>
              <li>{{ item.name }}</li>
              <li>{{ item.logo }}</li>
              <li>{{ item.description }}</li>
            </ul>
        </v-col>
      </v-row>         
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