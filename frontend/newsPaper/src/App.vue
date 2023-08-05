<script setup>
import HelloWorld from './components/HelloWorld.vue'
import HeaderDrawer from './components/headerDrawer.vue'
import Footer from './components/footer.vue'
</script>

<template>
  <!-- <HelloWorld msg="Vite + Vue" /> -->
  <q-layout view="hHh lpR fff">
    <HeaderDrawer />
    <q-page-container>

    </q-page-container>
    <Footer />
  </q-layout>
</template>

<style scoped>
body {
  background-color: red;
}
</style>
