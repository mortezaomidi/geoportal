<template>
  <div>
    <Drawer/>
    <v-main>
      <v-container fluid fill-height>
        <v-row>
          <v-col>
            <v-btn @click="$router.push({name: 'CreateOrganization'})">Add Organization</v-btn>  
          </v-col>
        </v-row>      
        <v-row>
          <v-col xs="12" sm="6" md="4" lg="3" xl="3" v-for="item in this.items" :key="item.id" >
            <v-card height="100%">
              <v-img :src="item.logo" max-height="auto" width="100px"></v-img>
              <v-card-title> {{item.name}} </v-card-title>
              <v-card-text justify> {{item.description}} </v-card-text>           
            </v-card>
          </v-col>
        </v-row>
      </v-container>
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