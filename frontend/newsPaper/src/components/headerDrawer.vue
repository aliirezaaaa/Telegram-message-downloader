<template >
    <q-header bordered class="bg-white text-black" height-hint="98">
        <div class="q-pt-md q-pl-md" style="display: flex; justify-content: space-between;">

            <div style="display: flex;">
                <DatePicker />

            </div>
            <div>
                <q-select dense label="نمایش بر اساس" transition-show="flip-up" transition-hide="flip-down" filled
                    v-model="sortBy" :options="sortByOptions" style="width: 250px" />
            </div>
        </div>

        <q-toolbar style="display: flex; justify-content: space-between;">
            <div style="display: flex;flex-direction: column;">
                <h6 class="text-subtitle1 no-margin">{{ today }}</h6>
            </div>
            <h3 class="text-h3 text-weight-medium text-center no-margin q-py-sm" style="font-family: Chomsky;">Shiraz Times
            </h3>
            <q-btn dense flat round icon="menu" @click="toggleRightDrawer" />
        </q-toolbar>

    </q-header>

    <q-drawer show-if-above v-model="rightDrawerOpen" side="right" bordered>
        <q-scroll-area class="fit">
            <q-list>

                <template v-for="(menuItem, index) in all_channels" :key="index">
                    <q-separator />
                    <q-item @click="switchChannel(menuItem.channel_name)" class="q-pa-sm" clickable
                        :active="menuItem.label === 'Outbox'" v-ripple>

                        <q-item-section style="display: flex;align-items: center;">
                            {{ menuItem.channel_name }}
                        </q-item-section>
                        <q-item-section style="display: flex;align-items: center;">
                            <q-avatar>
                                <img :src="menuItem.profile_url">
                            </q-avatar>
                        </q-item-section>
                    </q-item>

                </template>

            </q-list>
        </q-scroll-area>
    </q-drawer>
</template>

<script>
import { ref, computed } from 'vue'
import DatePicker from './datePicker.vue';

export default {
    emits: ['channel_name'],
    props: ['all_channels'],
    setup(props, { emit }) {
        const propsData = computed(() => {
            return {
                computedChannels: props.all_channels,
            };
        });
        // const all_channels = [{
        //     channel_name: "مشروح خبرها",
        //     profile_url: '../../media/globe.png',
        // }, {
        //     channel_name: "منوتو",

        // }]
        const rightDrawerOpen = ref(false);
        let sortBy = ref(null)
        let sortByOptions = ['جدید ترین', 'پر بازدید ترین', 'قدیمی ترین',]
        let options = [{ weekday: 'long' }, { day: 'numeric' }, { month: 'short' }, { year: 'numeric' }];
        let today = join(new Date, options, ' ');

        function join(date, options, separator) {
            function format(option) {
                let formatter = new Intl.DateTimeFormat('fa', option);
                return formatter.format(date);
            }
            return options.map(format).join(separator);
        }

        // async function fetching() {

        //     const response = await fetch('http://127.0.0.1:8000/channels/api/all/channels/');
        //     const data = await response.json();
        //     data.map(item => {
        //         all_channels.push({
        //             channel_name: item.name,
        //             profile_url: item.profile_url,
        //         })
        //     })

        // }
        // await fetching()

        function switchChannel(channel_name) {
            emit('channel_name', channel_name)
        }

        return {
            today,
            sortBy,
            all_channels: propsData.value.computedChannels,
            sortByOptions,
            rightDrawerOpen,
            toggleRightDrawer() {
                rightDrawerOpen.value = !rightDrawerOpen.value;
            },
            switchChannel,
        };
    },
    components: { DatePicker }
}
</script>
<style>
@font-face {
    font-family: "Chomsky";
    src: url('fonts/Chomsky-399c.woff');
}
</style>