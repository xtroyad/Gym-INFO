<template>
<div class="exform">
    <div>
    <q-checkbox v-model="reps[0]" label="Rep 1" color="teal" />
    <q-checkbox v-model="reps[1]" label="Rep 2" color="teal" />
    <q-checkbox v-model="reps[2]" label="Rep 3" color="teal" />
    <q-checkbox v-model="reps[3]" label="Rep 4" color="teal" />
    </div>
    
    <div>
    <q-field filled>
        <template v-slot:control>
        <div class="self-center full-width no-outline" tabindex="0">{{ Ejercicio[exercise_ID] }}</div>
        </template>
    </q-field>
    </div>

    <div class="input-fields">
    <q-input 
        v-model="kg" 
        label="Peso (kg)" 
        type="number" 
        min="0" 
        :max="500" 
        color="teal" 
    />
    
    <q-select 
        v-model="repsCount" 
        :options="repsOptions" 
        label="Repeticiones" 
        color="teal" 
        emit-value 
        map-options 
    />
    
    <q-select 
        v-model="rir" 
        :options="rirOptions" 
        label="RIR" 
        color="teal" 
        emit-value 
        map-options 
    />
    </div>

</div>
</template>

<script setup lang="ts">
import Ejercicio from 'src/model/enums/EjercicioEnum';
import { ref } from 'vue';

const reps = ref([false, false, false, false]); 
const kg = ref<number>(0); 
const repsCount = ref<number>(1); 
const rir = ref<number>(1); 

const repsOptions = Array.from({ length: 12 }, (_, i) => ({
    label: `${i + 1}`, 
    value: i + 1
})); 

const rirOptions = Array.from({ length: 4 }, (_, i) => ({
    label: `${i + 1}`, 
    value: i + 1
}));

defineProps<{
    exercise_ID: number;
}>();
</script>

<style>
.exform {
    background-color: rgb(188, 190, 190);
    padding: 20px;
    margin: 20px;
    border-radius: 8px;
}

.input-fields {
    margin-top: 20px;
}

.q-input, .q-select {
    margin-bottom: 15px;
}
</style>
