<script setup>
import Message from './components/message.vue'
import HeaderDrawer from './components/headerDrawer.vue'
import Footer from './components/footer.vue'
import { ref, watch } from 'vue';

const current_channel = ref('')
const reloader = ref(0)

function showChannelName(channel_name) {
  current_channel.value = channel_name
}

const all_channels = [{
  channel_name: "مشروح خبرها",
  profile_url: '../../media/globe.png',
}, {
  channel_name: "منوتو",
  profile_url: '../../media/profiles/ManotoTV.jpg',
},
{
  channel_name: "مهرنیوز",
  profile_url: '../../media/profiles/mehrnews.jpg',
},
{
  channel_name: "ایران اینترنشنال",
  profile_url: '../../media/profiles/iranintlTV.jpg',
},
]

const db = ref([{
  channel: 'تسنیم',
  message: 'هشدار قالیباف به شرکت های دانش بنیان: به سرنوشت ایران خودرو گرفتار نشوید.',
  views: 50,
  media_url: '../../media/11.mp4-Cover_480.mp4',
  media_type: 'video'
},
{
  channel: 'منوتو',
  message: 'علی شریفی زارچی، استاد اخراج شده دانشگاه شریف، از دعوت هیات اجرایی جذب دانشگاه شریف و درخواست تجدید نظر خود خبر داد. او در صفحه توییتر خود نوشت:به دعوت هیات محترم اجرایی جذب دانشگاه شریف در جلسه این هیات حضور یافتم و ضمن تقدیم پرونده علمی و ارایه توضیحات در مورد سوابق آموزشی و پژوهشی، درخواست تجدید نظر ارایه نمودم.',
  views: 1800000,
  media_url: '../../media/photo_6050705465559597201_y.jpg',
  media_type: 'image'
},
{
  channel: 'مهر نیوز',
  message: 'سال تحصیلی جدید دانشگاه ها از سوم مهر ماه آغار میشود. وزیر علوم در گفت و گو با مهر: سال تحصیلی جدید برای دانشجویان از سوم مهر ماه و برای ورودی های جدید از هفته سوم مهرماه آغاز میشود.',
  views: 318,
  media_url: '../../media/photo_6048626100092911940_y.jpg',
  media_type: 'image'
},
{
  channel: 'منوتو',
  message: 'نت بلاکس اعلام کرد: برای دومین شب متوالی از ساعت یک بامداد اختلال در دسترسی به اینترنت در ایران ثبت شده است. میزان دسترسی به اینترنت 71 درصد کمتر از موارد عادی است.',
  views: 16400,
  media_url: '../../media/photo_6050705465559597186_y.jpg',
  media_type: 'image'
},
{
  channel: 'تسنیم',
  message: 'هاشمی برای وزارت ورزش به مجلس معرفی شد. معاون پارلمانی رییس جمهور از معرفی کیومرث هاشمی به عنوان وزیر پیشنهادی ورزش به مجلس خبر داد.',
  views: 67,
  media_url: '../../media/photo_5186221444722437249_y.jpg',
  media_type: 'image'
},
{
  channel: 'ایران اینترنشنال',
  message: 'یک ماه پس از تخریب ناگهانی ورزشگاه آزادی، ابراهیم ریسی، رییس جمهور گفت: باید یک ورزشگاه جامع و آبرومند که در شان و منزلت قهرمانان ملی ما و همچنین میزبانی میهمانان بین المللی در تهران ایجاد شود. ولو اینکه هزینه داشته باشد، این هزینه نیست بلکه سرمایه گذاری است. او همچنین از قهرمانان خواست متوقف نشوند: قهرمانان در جایگاه قهرمانی تلاش خود را افزون کنند و در نقطه ای که قرار دارند متوقف نشوند.',
  views: 19900,
  media_url: '../../media/photo_6052141509349847331_y.jpg',
  media_type: 'image'
},])

const all_news = ref([{
  channel: 'تسنیم',
  message: 'هشدار قالیباف به شرکت های دانش بنیان: به سرنوشت ایران خودرو گرفتار نشوید.',
  views: 50,
  media_url: '../../media/11.mp4-Cover_480.mp4',
  media_type: 'video'
},
{
  channel: 'منوتو',
  message: 'علی شریفی زارچی، استاد اخراج شده دانشگاه شریف، از دعوت هیات اجرایی جذب دانشگاه شریف و درخواست تجدید نظر خود خبر داد. او در صفحه توییتر خود نوشت:به دعوت هیات محترم اجرایی جذب دانشگاه شریف در جلسه این هیات حضور یافتم و ضمن تقدیم پرونده علمی و ارایه توضیحات در مورد سوابق آموزشی و پژوهشی، درخواست تجدید نظر ارایه نمودم.',
  views: 1800000,
  media_url: '../../media/photo_6050705465559597201_y.jpg',
  media_type: 'image'
},
{
  channel: 'مهرنیوز',
  message: 'سال تحصیلی جدید دانشگاه ها از سوم مهر ماه آغار میشود. وزیر علوم در گفت و گو با مهر: سال تحصیلی جدید برای دانشجویان از سوم مهر ماه و برای ورودی های جدید از هفته سوم مهرماه آغاز میشود.',
  views: 318,
  media_url: '../../media/photo_6048626100092911940_y.jpg',
  media_type: 'image'
},
{
  channel: 'منوتو',
  message: 'نت بلاکس اعلام کرد: برای دومین شب متوالی از ساعت یک بامداد اختلال در دسترسی به اینترنت در ایران ثبت شده است. میزان دسترسی به اینترنت 71 درصد کمتر از موارد عادی است.',
  views: 16400,
  media_url: '../../media/photo_6050705465559597186_y.jpg',
  media_type: 'image'
},
{
  channel: 'تسنیم',
  message: 'هاشمی برای وزارت ورزش به مجلس معرفی شد. معاون پارلمانی رییس جمهور از معرفی کیومرث هاشمی به عنوان وزیر پیشنهادی ورزش به مجلس خبر داد.',
  views: 67,
  media_url: '../../media/photo_5186221444722437249_y.jpg',
  media_type: 'image'
},
{
  channel: 'ایران اینترنشنال',
  message: 'یک ماه پس از تخریب ناگهانی ورزشگاه آزادی، ابراهیم ریسی، رییس جمهور گفت: باید یک ورزشگاه جامع و آبرومند که در شان و منزلت قهرمانان ملی ما و همچنین میزبانی میهمانان بین المللی در تهران ایجاد شود. ولو اینکه هزینه داشته باشد، این هزینه نیست بلکه سرمایه گذاری است. او همچنین از قهرمانان خواست متوقف نشوند: قهرمانان در جایگاه قهرمانی تلاش خود را افزون کنند و در نقطه ای که قرار دارند متوقف نشوند.',
  views: 19900,
  media_url: '../../media/photo_6052141509349847331_y.jpg',
  media_type: 'image'
},])

async function fetchingNews() {
  const response = await fetch('http://127.0.0.1:8000/news/api/all/news/');
  const data = await response.json();
  data.map(item => {
    let media_type = ''
    if (item.image_url.slice(-3) == "jpg") {
      media_type = 'image';
    } else {
      if (item.image_url.slice(-3) == "mp4") {
        media_type = 'video';
      }
    }

    all_news.push({
      channel: item.channel,
      message: item.message,
      views: item.views,
      media_url: item.image_url,
      media_type: media_type
    })
  })

}
// await fetchingNews()

async function fetchingChannels() {

  const response = await fetch('http://127.0.0.1:8000/channels/api/all/channels/');
  const data = await response.json();
  data.map(item => {
    all_channels.push({
      channel_name: item.name,
      profile_url: item.profile_url,
    })
  })

}
// await fetchingChannels()

async function fetchingNews_specific(channel_id) {
  const response = await fetch(`http://127.0.0.1:8000/news/api/v1/news/${channel_id}/`);
  const data = await response.json();
  data.map(item => {
    let media_type = ''
    if (item.image_url.slice(-3) == "jpg") {
      media_type = 'image';
    } else {
      if (item.image_url.slice(-3) == "mp4") {
        media_type = 'video';
      }
    }

    all_news.push({
      channel: item.channel,
      message: item.message,
      views: item.views,
      media_url: item.image_url,
      media_type: media_type
    })
  })

}

async function fetchingNews_date(day) {
  const response = await fetch(`http://127.0.0.1:8000/news/api/v2/news/${day}/`);
  const data = await response.json();
  data.map(item => {
    let media_type = ''
    if (item.image_url.slice(-3) == "jpg") {
      media_type = 'image';
    } else {
      if (item.image_url.slice(-3) == "mp4") {
        media_type = 'video';
      }
    }

    all_news.push({
      channel: item.channel,
      message: item.message,
      views: item.views,
      media_url: item.image_url,
      media_type: media_type
    })
  })

}

async function fetchingNews_sort() {
  const response = await fetch(`http://127.0.0.1:8000/news/api/v3/news/`);
  const data = await response.json();
  data.map(item => {
    let media_type = ''
    if (item.image_url.slice(-3) == "jpg") {
      media_type = 'image';
    } else {
      if (item.image_url.slice(-3) == "mp4") {
        media_type = 'video';
      }
    }

    all_news.push({
      channel: item.channel,
      message: item.message,
      views: item.views,
      media_url: item.image_url,
      media_type: media_type
    })
  })

}
async function filterNews(db, filter) {
  all_news.value = []
  await db.value.map(item => {
    if (item.channel == filter) {
      all_news.value.push(item)
    }
  })
}

watch(
  () => [current_channel.value],
  async () => {
    await filterNews(db, current_channel.value)
    reloader.value += 1
  },
);
</script>

<template>
  <!-- <HelloWorld msg="Vite + Vue" /> -->
  <div style="font-family: Vazir;">

    <q-layout view="hHh lpR fff">

      <HeaderDrawer @channel_name="showChannelName" :all_channels="all_channels" />

      <q-page-container>

        <div style="display: flex;justify-content: center;">
          {{ vis }}
          <Message :key="reloader" :all_news="all_news" />

        </div>

      </q-page-container>
      <Footer />
    </q-layout>
  </div>
</template>

<style scoped>
body {
  background-color: red;
}

@font-face {
  font-family: "Vazir";
  src: url('fonts/Vazir.woff');
}
</style>
