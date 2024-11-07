<template>
  <q-page class="row items-center justify-evenly">
    <div id="tester" style="width:600px;height:250px;"></div>
    jeje
  </q-page>
</template>

<script setup lang="ts">

import Plotly from 'plotly.js-basic-dist';
import { onMounted } from 'vue';

  let TESTER: HTMLElement | null = null
  


  onMounted(()=>{
  TESTER = document.getElementById('tester') || new HTMLElement()

  Plotly.newPlot( TESTER, [
    {
      x: [1, 2, 3, 4, 5],
      y: [1, 2, 4, 8, 16] 
    }], 
    {
      margin: { t: 0 } } );

})
</script>
