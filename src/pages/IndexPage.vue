<template>
  <q-page class="column items-center justify-evenly" style="min-height: 100%;">
    <div id="params">
      <q-select filled v-model="dayModel" :options="Array.from(map.keys())" label="Día" />
      <q-select filled v-model="exerModel" :options="options" label="Ejercicio" />

      <q-checkbox v-model="reps[0]" label="R1" color="teal" />
      <q-checkbox v-model="reps[1]" label="R2" color="teal" />
      <q-checkbox v-model="reps[2]" label="R3" color="teal" />
      <q-checkbox v-model="reps[3]" label="R4" color="teal" />
    </div>
    <div id="tester" style="width:70%;height:70%;"></div>
  </q-page>
</template>

<script setup lang="ts">
import Plotly from 'plotly.js-basic-dist';
import { computed, onMounted, ref } from 'vue';

const dayModel = ref('lunes')
const map = new Map<string, Array<string>>([
  ['lunes', ['Peso M', 'Peso R', 'GEMELO', ' HT']],
  ['martes', ['CURL', 'MARTILLO', 'ANT. MANCUERNA', 'ANT. BARRA', 'MAN. NEUTRA', 'BAR INV.']],
  ['miercoles', ['PRESS BNC', 'PRESS MLT', 'HOMBRO', 'HOMBRO F', 'CRUCE', 'BANCA INCL', 'HOMBRO T']],
  ['jueves', ['REMO MAN', 'JALON P', ' TRI CUERDA', 'TRI INV', 'JALON SENT', 'PRESS FR', 'JALON BAR']],
  ['viernes', ['SENTADILLA', 'GEMELO', 'BULGARA', 'EXT CUADRI']],
]);

const exerModel = ref('Peso M')
const options = computed(()=>{
  return map.get(dayModel.value)
})
const reps = ref([false, false, false, false])






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
<style lang="css">
#params{
  background-color: rgb(132, 138, 138);
  width: 100%;
  display: flex; 
}
</style>
