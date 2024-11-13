<template>
  <q-page class="column items-center justify-evenly" style="min-height: 100%;">
    <div id="params">
      <q-select filled v-model="dayModel" :options="Array.from(map.keys())" label="Día" />
      <q-select filled v-model="exerModel" :options="options"  option-value="value"
      option-label="label" label="Ejercicio" />

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
import DataFrame, { GroupedDataFrame } from 'dataframe-js';
import Ejercicio from 'src/model/enums/EjercicioEnum';

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

// const setExercise = {
//   'LUNES': [1, 2, 3, 4],
//   'MARTES': [5, 6, 7, 8, 9, 10],
//   'MIERCOLES': [11, 12, 13 , 14, 15, 16],
//   'JUEVES': [17, 18, 19, 20, 21, 22, 23],
//   'VIERNES': [24, 25, 26, 27],
// }

const exerModel = ref({ value: Ejercicio.PESO_M, label: Ejercicio[Ejercicio.PESO_M] })

const options = computed(()=>{
  return map.get(dayModel.value);
})

const reps = ref([false, false, false, false])

let TESTER: HTMLElement | null = null

const loadCsv = async () => {
  let response: DataFrame  = new DataFrame([])
  try {
    response = await  DataFrame.fromCSV('src/temp/myEntre.csv')
  } catch (error) {
    console.error('Error:', error);
  }
  plotData(response);

};

const plotData = (df: DataFrame) => {
  TESTER = document.getElementById('tester') || new HTMLElement();
  console.log(df)
  const ids : string[] = df.distinct('exercise_ID').toArray('exercise_ID')
  console.log(ids)

  const new_df: GroupedDataFrame = df.groupBy('exercise_ID')
  console.log(new_df.toCollection())
  const trace = new_df.toCollection().map(group =>{
    console.log(group)
    const dataframe: DataFrame = group['group']
    const id: string = group['groupKey']['exercise_ID']
    console.log(id)
    return {
        x: dataframe.toArray('day').map(day => new Date(day)),
        y: dataframe.toArray('weight1'),
        mode: 'scatter',
        name: `Exercise ${id}`,
        width: 3
      };
  })


  const layout = {
    margin: { t: 0 },
    title: 'Exercise Data Over Days',
    xaxis: { title: 'Day' },
    yaxis: { title: 'Value' }
  };

  Plotly.newPlot(TESTER, trace, layout);
};

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
</style>
