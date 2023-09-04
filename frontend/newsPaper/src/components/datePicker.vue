<template>
    <div>
        <q-btn icon="event" round color="primary">
            <q-popup-proxy @before-show="updateProxy" cover transition-show="scale" transition-hide="scale">
                <q-date v-model="proxyDate" calendar="persian">
                    <div class="row items-center justify-end ">
                        <q-btn label="Cancel" color="primary" flat v-close-popup />
                        <q-btn label="OK" color="primary" flat @click="save" v-close-popup />
                    </div>
                </q-date>
            </q-popup-proxy>
        </q-btn>
    </div>
</template>
  
<script>
import { ref } from 'vue'

export default {
    setup() {
        const date = ref(new Date)
        const proxyDate = ref('2019/03/01')

        return {
            date,
            proxyDate,

            updateProxy() {
                proxyDate.value = date.value
            },

            save() {
                date.value = proxyDate.value
            }
        }
    }
}
</script>
  