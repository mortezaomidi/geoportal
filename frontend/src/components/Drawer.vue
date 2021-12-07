<template>
<div>      
    <v-app-bar app color="teal" dense>
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    <v-toolbar-title class="white--text">Knowledge-based Geoportal</v-toolbar-title> <v-spacer></v-spacer>
    </v-app-bar> 
    <v-navigation-drawer v-model="drawer" app>
        <v-list-item>
            <v-list-item-avatar>
                <v-img src="../assets/img/morteza.jpg"></v-img>
            </v-list-item-avatar>
            <v-list-item-content>
                <v-list-item-title>Morteza Omidipoor</v-list-item-title>
                <v-list-item-subtitle>PhD student</v-list-item-subtitle>
            </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
        <v-list dense nav>
            <v-list-item link @click="$router.push({name: 'Home'})">
                <v-list-item-icon> <v-icon>mdi-home</v-icon> </v-list-item-icon>
                <v-list-item-title>Home</v-list-item-title>
            </v-list-item>
            <v-list-item link @click="$router.push({name: 'Organization'})">
                <v-list-item-icon> <v-icon>mdi-plus</v-icon> </v-list-item-icon>
                <v-list-item-title>Organization</v-list-item-title>
            </v-list-item>
            <v-list-item link @click="$router.push({name: 'Logout'})">
                <v-list-item-icon> <v-icon color="red darken-2">mdi-logout</v-icon> </v-list-item-icon>
                <v-list-item-title>Logout</v-list-item-title>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>
</div>
</template>

<script>
export default {
    name: 'Drawer',
    data: () => ({
      drawer: false
    }),    
}
</script>