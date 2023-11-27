<template>
    <div class="q-pa-md row q-gutter-md" style="display: flex;justify-content: center;">
        <q-card style="width: 70%; min-width: 10rem;" v-for="(single_message, index) in all_news" :key="single_message" flat
            bordered dir="rtl">
            <q-img v-if="single_message.media_type == 'image'" :src="single_message.media_url" />
            <q-video v-if="single_message.media_type == 'video'" :ratio="16 / 9" :src="single_message.media_url" />
            <q-card-section>
                <div style="display: flex;justify-content: space-between;align-items: center;">
                    <div class="text-overline text-orange-9">{{ single_message.channel }}</div>
                    <div style="display: flex;">
                        {{ single_message.views }}
                        <q-icon class="q-mx-sm" name="img:../../public/icon/eyeVector.svg" />
                    </div>
                </div>
                <div class="text-caption text-grey ellipsis-2-lines">
                    {{ single_message.message }}
                </div>
            </q-card-section>

            <q-card-actions>
                <q-btn color="grey" round flat dense :icon="expanded[index] ? 'keyboard_arrow_up' : 'keyboard_arrow_down'"
                    @click="toggle_expansion(index)" />
                <q-space />
                <q-btn flat color="primary" label="Share" />

            </q-card-actions>

            <q-slide-transition>
                <div v-show="expanded[index]">
                    <q-separator />
                    <q-card-section class="text-subitle2">
                        {{ single_message.message }}
                    </q-card-section>
                </div>
            </q-slide-transition>
        </q-card>
    </div>
</template>
  
<script>
import { ref, computed } from 'vue'

export default {
    props: ['all_news'],
    setup(props) {

        const propsData = computed(() => {
            return {
                computedNews: props.all_news,
            };
        });
        let expanded = ref([])
        // const all_news = []

        // async function fetching() {
        //     const response = await fetch('http://127.0.0.1:8000/news/api/all/news/');
        //     const data = await response.json();
        //     data.map(item => {
        //         let media_type = ''
        //         if (item.image_url.slice(-3) == "jpg") {
        //             media_type = 'image';
        //         } else {
        //             if (item.image_url.slice(-3) == "mp4") {
        //                 media_type = 'video';
        //             }
        //         }

        //         all_news.push({
        //             channel: item.channel,
        //             message: item.message,
        //             views: item.views,
        //             media_url: item.image_url,
        //             media_type: media_type
        //         })
        //     })

        // }
        // await fetching()

        function toggle_expansion(index) {
            expanded.value[index] = !expanded.value[index]
        }
        console.log("from msg: ", propsData.value.computedNews);
        return {
            expanded,
            all_news: propsData.value.computedNews,
            toggle_expansion,
        }
    }
}
</script>
  