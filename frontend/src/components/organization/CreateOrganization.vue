<template>
  <div>
    <Drawer/>
    <v-main>
      <v-container>
          <v-row>
              <v-col>
                <v-form @submit.prevent="submitFormData" enctype="multipart/form-data">
                    <v-text-field label="Title" v-model="postData.name" required></v-text-field>
                    <v-text-field label="Url" v-model="postData.url" required></v-text-field>
                    <v-text-field label="Description" v-model="postData.description" required></v-text-field>
                    <v-file-input label="Logo" v-model="postData.logo"></v-file-input>
                    <v-btn type="submit">Submit</v-btn>
                </v-form>
              </v-col>
          </v-row>
      </v-container>
    </v-main>
  </div>

</template>

<script>
import axios from 'axios';
import Drawer from '../Drawer.vue'

export default {
  name: 'Organization',
  components: {
    Drawer,
  },
  data() {
    return {
      postData: {
          name: null,
          url: null,
          description: null,
          logo: null
      },
      postResponse: null,
      errorMessage : null
    }
  },
  methods: {
    submitFormData: function () {
        const formData = new FormData();

        formData.append("name", this.postData.name);
        formData.append("url", this.postData.url);
        formData.append("description", this.postData.description);
        formData.append("logo", this.postData.logo);

      axios.post('http://127.0.0.1:8000/api/organization', formData)
      .then( response => {          
          this.postResponse = response;
      });
    },
  },
}
</script>