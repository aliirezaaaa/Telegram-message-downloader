<script setup>
import Message from './components/message.vue'
import HeaderDrawer from './components/headerDrawer.vue'
import Footer from './components/footer.vue'
</script>

<template>
  <!-- <HelloWorld msg="Vite + Vue" /> -->
  <div style="font-family: Vazir;">

    <q-layout view="hHh lpR fff">
      <HeaderDrawer />
      <q-page-container>

        <div style="display: flex;justify-content: center;">
          <suspense>
            <Message />
          </suspense>
        </div>

      </q-page-container>
      <Footer />
    </q-layout>
  </div>
</template>

<style scoped>
body {
  background-color: red;
}

@font-face {
  font-family: "Vazir";
  src: url('fonts/Vazir.woff');
}
</style>
