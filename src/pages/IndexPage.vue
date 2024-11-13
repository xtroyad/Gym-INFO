<template>
  <q-page class="column items-center justify-evenly" style="min-height: 100%;">
    <div id="params">
      <q-select filled v-model="dayModel" :options="Array.from(map.keys())" label="Día" />
      <q-select filled v-model="exerModel" :options="options"  option-value="value"
      option-label="label" label="Ejercicio" />
    </div>
    <div class="gra">
      <div id="tester" style="width:70%; height:70%;"></div>
      <formExerComponent :exercise_ID="exerModel.value"/>
    </div>
    
  </q-page>
</template>

<script setup lang="ts">
import Plotly from 'plotly.js-basic-dist';
import { computed, onMounted, ref, watch } from 'vue';
import DataFrame, { GroupedDataFrame } from 'dataframe-js';
import Ejercicio from 'src/model/enums/EjercicioEnum';
import formExerComponent from 'src/components/formExerComponent.vue';
const dayModel = ref('LUNES')

const map = new Map<string, Array<{ value: number, label: string }>>([
  ['LUNES', [
    { value: Ejercicio.PESO_M, label: Ejercicio[Ejercicio.PESO_M] },
    { value: Ejercicio.PESO_R, label: Ejercicio[Ejercicio.PESO_R] },
    { value: Ejercicio.GEMELO, label: Ejercicio[Ejercicio.GEMELO] },
    { value: Ejercicio.HT, label: Ejercicio[Ejercicio.HT] }
  ]],
  ['MARTES', [
    { value: Ejercicio.CURL, label: Ejercicio[Ejercicio.CURL] },
    { value: Ejercicio.MARTILLO, label: Ejercicio[Ejercicio.MARTILLO] },
    { value: Ejercicio.ANT_MANC, label: Ejercicio[Ejercicio.ANT_MANC] },
    { value: Ejercicio.ANT_BARRA, label: Ejercicio[Ejercicio.ANT_BARRA] },
    { value: Ejercicio.MAN_NEUTRO, label: Ejercicio[Ejercicio.MAN_NEUTRO] },
    { value: Ejercicio.BAR_INV, label: Ejercicio[Ejercicio.BAR_INV] }
  ]],
  ['MIERCOLES', [
    { value: Ejercicio.PRESS_BNC, label: Ejercicio[Ejercicio.PRESS_BNC] },
    { value: Ejercicio.PRESS_MANC, label: Ejercicio[Ejercicio.PRESS_MANC] },
    { value: Ejercicio.HOMBRO, label: Ejercicio[Ejercicio.HOMBRO] },
    { value: Ejercicio.HOMBRO_F, label: Ejercicio[Ejercicio.HOMBRO_F] },
    { value: Ejercicio.CRUCE, label: Ejercicio[Ejercicio.CRUCE] },
    { value: Ejercicio.BANCA_INCL, label: Ejercicio[Ejercicio.BANCA_INCL] },
    { value: Ejercicio.HOMBRO_T, label: Ejercicio[Ejercicio.HOMBRO_T] }
  ]],
  ['JUEVES', [
    { value: Ejercicio.REMO_MANC, label: Ejercicio[Ejercicio.REMO_MANC] },
    { value: Ejercicio.JALON_P, label: Ejercicio[Ejercicio.JALON_P] },
    { value: Ejercicio.TRI_CUERDA, label: Ejercicio[Ejercicio.TRI_CUERDA] },
    { value: Ejercicio.TRI_INV, label: Ejercicio[Ejercicio.TRI_INV] },
    { value: Ejercicio.JALON_SENT, label: Ejercicio[Ejercicio.JALON_SENT] },
    { value: Ejercicio.PRESS_FR, label: Ejercicio[Ejercicio.PRESS_FR] },
    { value: Ejercicio.JALON_BARRA, label: Ejercicio[Ejercicio.JALON_BARRA] }
  ]],
  ['VIERNES', [
    { value: Ejercicio.SENTADILLA, label: Ejercicio[Ejercicio.SENTADILLA] },
    { value: Ejercicio.GEMELO, label: Ejercicio[Ejercicio.GEMELO] },
    { value: Ejercicio.BULGARA, label: Ejercicio[Ejercicio.BULGARA] },
    { value: Ejercicio.EXT_QUAD, label: Ejercicio[Ejercicio.EXT_QUAD] }
  ]]
]);


const exerModel = ref({ value: Ejercicio.PESO_M, label: Ejercicio[Ejercicio.PESO_M] })

const options = computed(()=>{
  return map.get(dayModel.value) || [{ value: Ejercicio.PESO_M, label: Ejercicio[Ejercicio.PESO_M] }];
})


let TESTER: HTMLElement | null = null

let dataframe = new DataFrame([])
const loadCsv = async () => {
  try {
    dataframe = await  DataFrame.fromCSV('src/temp/myEntre.csv')
  } catch (error) {
    console.error('Error:', error);
  }
  updateGraph(exerModel.value.value.toString());
};

const updateGraph = (ex_ID: string) => {
  const df: DataFrame = dataframe
  TESTER = document.getElementById('tester') || new HTMLElement();

  const new_df: GroupedDataFrame = df.groupBy('exercise_ID')

  const groups = new_df.toCollection().filter(group => {
    return group['groupKey']['exercise_ID'] === (ex_ID)
  })

  const traces: object[] = []; 

  groups.forEach(group => {
  const dataframe: DataFrame = group['group'];
  const id: string = group['groupKey']['exercise_ID'];

  for (let i = 1; i <= 4; i++) {
    const weightColumn = `weight${i}`; 
    
    
    const trace = {
      x: dataframe.toArray('day').map(day => new Date(day)),
      y: dataframe.toArray(weightColumn),
      mode: 'scatter',
      name: `Exercise ${id} - ${weightColumn}`,
      width: 3
    };
    
    traces.push(trace);
  }
});

  const layout = {
    margin: { t: 0 },
    title: 'Exercise Data Over Days',
    xaxis: { title: 'Day' },
    yaxis: { title: 'Value' }
  };

  if (TESTER.hasChildNodes()) {
      Plotly.react(TESTER, traces, layout); 
    } else {
      Plotly.newPlot(TESTER, traces, layout);
    }
  };

watch(() => exerModel.value.value, (newValue) => {
  console.log('exerModel.value.value ha cambiado a', newValue);
  updateGraph(exerModel.value.value.toString());
});

onMounted(()=>{
  loadCsv()
})


</script>
<style lang="css">
#params{
  background-color: rgb(132, 138, 138);
  width: 100%;
  display: flex; 
}

.gra{
  display: flex; 
  width: 100%;
}
</style>
