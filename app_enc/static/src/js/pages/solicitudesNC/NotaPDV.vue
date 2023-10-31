<template>
    <Header />
    <div class="container px-6 mx-auto block">
        <div class="flex items-center justify-center py-5"><span class="font-bold text-gray-600">SOLICITUD NOTA DE CRÉDITO -
                PUNTOS DE VENTA</span></div>
        <div class="grid grid-cols-3 pt-2">
            <div class="flex"></div>
            <div class="block">
                <form action="">
                    <div class="py-2"><span class="text-sm font-bold text-gray-600 py-5">Datos de Documentos de
                            Origen</span></div>
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
                        <label class="text-sm">Importe Total:</label>
                        <input type="text" class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400
      focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none
      invalid:border-pink-500 invalid:text-pink-600
      focus:invalid:border-pink-500 focus:invalid:ring-pink-500
    " />
                    </div>
                    <div class="pt-4 pb-1"><span class="text-sm font-bold text-gray-600 py-5">Detalle de la Solicitud</span>
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
                        <label class="text-sm">Justificación:</label>
                        <textarea name="textarea-name" rows="5"
                            class="focus:shadow-soft-primary-outline min-h-unset text-sm leading-5.6 ease-soft block h-auto w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 outline-none transition-all placeholder:text-gray-500 focus:border-sky-500 focus:outline-none focus:ring-1 focus:ring-sky-500"></textarea>
                    </div>
                    <div class="space-y-1 py-2">
                        <label class="text-sm">Método:</label>
                        <fieldset class="blocks">
                            <div class="my-8"></div>
                            <input id="draft" class="sr-only my-5 peer/draft" type="radio" name="status" checked />
                            <label
                                class="p-5 mx-3 my-5 bg-white border rounded-lg cursor-pointer peer-checked/draft:border-sky-500 hover:border-sky-500 peer-checked/draft:border-sky-500 peer-checked/draft:ring-1 peer-checked/draft:bg-sky-100"
                                for="draft">Total</label>
                            <input id="published" class="sr-only peer/published" type="radio" name="status" />
                            <label
                                class="p-5 mx-3 my-5 bg-white border rounded-lg cursor-pointer peer-checked/published:border-sky-500 hover:border-sky-500 peer-checked/published:border-sky-500 peer-checked/published:ring-1 peer-checked/published:bg-sky-100"
                                for="published">Parcial</label>
                            <div class="my-8"></div>
                            <div class="hidden flex items-center justify-center peer-checked/draft:block"></div>
                            <div class="hidden peer-checked/published:block">
                                <div class="space-y-1 py-2">
                                    <div id="app" class="relative">
                                        <!-- <select v-model="selectedOptions" multiple id="multiselect"
                                            class="block w-full px-4 py-2 pr-8 leading-tight bg-white border border-gray-300 rounded appearance-none focus:outline-none focus:bg-white focus:border-gray-500">
                                            <option v-for="option in options" :key="option" :value="option">{{ option }}</option>
                                        </select>
                                        <div class="absolute inset-y-0 right-0 flex items-center px-2 pointer-events-none">
                                            <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor"
                                                viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                    d="M15 19l-7-7 7-7"></path>
                                            </svg>
                                        </div> -->
                                        <div>
                                            <label class="typo__label text-sm">Producto:</label>
                                            <multiselect v-model="value" id="multiselect" :options="options"
                                                :multiple="true" :close-on-select="false" :clear-on-select="false"
                                                :preserve-search="true" placeholder="Seleccionar producto..." label="name"
                                                track-by="name">
                                                <!-- <template slot="selection" slot-scope="{ values, search, isOpen }"><span
                                                        class="multiselect__single" v-if="values.length" v-show="!isOpen">{{
                                                            values.length }} options selected</span></template> -->
                                            </multiselect>
                                            <div class="py-2"></div>
                                            <div v-for="val in value" class="py-2">
                                                <div class="text-center text-sm font-bold bg-gray-600 text-white rounded-lg py-1">{{ val["name"] }}</div>
                                                <div class="flex">
                                                    <div class="space-y-1 py-2 px-2">
                                                        <label class="text-sm text-center">Unidad:</label>
                                                        <input type="text" class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400
      focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none
      invalid:border-pink-500 invalid:text-pink-600
      focus:invalid:border-pink-500 focus:invalid:ring-pink-500
    " />
                                                    </div>
                                                    <div class="space-y-1 py-2 px-2">
                                                        <label class="text-sm">Precio:</label>
                                                        <input type="text" class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400
      focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none
      invalid:border-pink-500 invalid:text-pink-600
      focus:invalid:border-pink-500 focus:invalid:ring-pink-500
    " />
                                                    </div>
                                                    <div class="space-y-1 py-2 px-2">
                                                        <label class="text-sm">Cantidad:</label>
                                                        <input type="text" class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400
      focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none
      invalid:border-pink-500 invalid:text-pink-600
      focus:invalid:border-pink-500 focus:invalid:ring-pink-500
    " />
                                                    </div>
                                                    <div class="space-y-1 py-2 px-2">
                                                        <label class="text-sm">Monto Total:</label>
                                                        <input type="text" class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400
      focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none
      invalid:border-pink-500 invalid:text-pink-600
      focus:invalid:border-pink-500 focus:invalid:ring-pink-500
    " />
                                                    </div>
                                                </div>

                                            </div>
                                        </div>
                                    </div>
                                    <!-- 
                                    <div id="etiquetas" class="mt-4 flex flex-wrap">
                                        <span v-for="option in selectedOptions" :key="option"
                                            class="inline-flex items-center px-2 py-1 mr-2 mt-2 text-sm font-medium text-gray-700 bg-gray-200 rounded-full">
                                            {{ value }}
                                        </span>
                                    </div> -->
                                </div>

                            </div>
                        </fieldset>
                    </div>

                </form>
            </div>
        </div>
    </div>
</template>
<script setup>
// Importando layouts
import Header from '../../layouts/Header.vue';
// 
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';
//
import Multiselect from 'vue-multiselect';
</script>
<script>
export default {
    name: "NotaPDV",
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
    mounted() {
        //
        //        tags = document.getElementsByClassName("multiselect__tags")

        //
    }
}
</script>
<style scope>
@import 'https://unpkg.com/vue-multiselect@2.1.6/dist/vue-multiselect.min.css';
</style>