<template>
    <Header />
    <div class="container px-6 mx-auto block">
        <div class="flex items-center justify-center py-5"><span class="font-bold text-gray-600">SOLICITUD NOTA DE CRÉDITO -
                SERVICIOS</span></div>
        <div class="grid grid-cols-3 pt-2">
            <div class="flex"></div>
            <div class="block">
                <form action="">
                    <div class="py-2"><span class="text-sm font-bold text-gray-600 py-5">Datos de Documento de Origen</span></div>
                    <div class="space-y-1 py-2">
                        <label class="text-sm">Fecha emisión del comprobantes:</label>
                        <VueDatePicker v-model="date"></VueDatePicker>
                    </div>
                    <div class="space-y-1 py-2">
                        <label class="text-sm">Nro. Comprobante:</label>
                        <input type="text" class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400
      focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none
      invalid:border-pink-500 invalid:text-pink-600
      focus:invalid:border-pink-500 focus:invalid:ring-pink-500
    " />
                    </div>
                    <div class="space-y-1 py-2">
                        <label class="text-sm">Motivo:</label>
                        <input type="text" class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400
      focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none
      invalid:border-pink-500 invalid:text-pink-600
      focus:invalid:border-pink-500 focus:invalid:ring-pink-500
    " />
                    </div>
                    <div class="space-y-1 py-2">
                        <label class="text-sm">Importe de Nota de Crédito:</label>
                        <input type="text" class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400
      focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none
      invalid:border-pink-500 invalid:text-pink-600
      focus:invalid:border-pink-500 focus:invalid:ring-pink-500
    " />
                    </div>
                    <div class="space-y-1 py-2">
                        <label class="text-sm">Fecha emisión de la nota de crédito:</label>
                        <VueDatePicker v-model="date"></VueDatePicker>
                    </div>
                    <div class="py-2"></div>
                </form>
            </div>
        </div>
    </div>
</template>
<script setup>
// Importando layouts
import Header from '../../layouts/Header.vue'
// 
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';
//
import Multiselect from 'vue-multiselect';
//
</script>
<script>
export default {
    name: "NotaServicios",
    components: { VueDatePicker, Multiselect },
    data() {
        return {
            date: null,
            options: [{ name: 'Vue.js', language: 'JavaScript' },
            { name: 'Adonis', language: 'JavaScript' },
            { name: 'Rails', language: 'Ruby' },
            { name: 'Sinatra', language: 'Ruby' },
            { name: 'Laravel', language: 'PHP' },
            { name: 'Phoenix', language: 'Elixir' }],
            value: null,
            selectedOptions: [],
        }
    },
}
</script>
<style scope></style>