
<template>

  <div class="ui centered grid">

    <template v-if="self_store.getters.GET_FILTERED_jobs_list.length > this.numberOfElementsPerPage">

      <carousel :perPage="COMPUTED_per_page" :navigationEnabled="true">
        <slide v-for="(queried_packetsArray, index) in METHOD_divded_packetsArray(1)">

          <div class="eight wide mobile eight wide tablet eight wide computer column main-div-style" v-for="queried_packetObject in queried_packetsArray" >

              <div class="ui large image">
                 <div class="ui compact menu" style="width: 100%;">
                    <a class="item" style="width: 50%;font-size: 2em;">
                       <i class="icon mail"></i> Messages
                       <div class="floating ui red label" style="font-size: 0.79em;">22</div>
                    </a>
                    <a class="item" style="width: 50%;font-size: 2em;">
                       <i class="icon users"></i> Friends
                       <div class="floating ui teal label" style="font-size: 0.79em;">22</div>
                    </a>
                 </div>
                 <img :src="queried_packetObject.image" class="company-image-main-image"> <button class="ui bottom attached label company-image-leading-button"><i class="icon user"></i>
                  Show More
                 </button>
              </div>

          </div>
        </slide>
      </carousel>

    </template>

    <template v-else-if="self_store.getters.GET_FILTERED_jobs_list.length > 0">

      <div v-on class="six wide mobile six wide tablet four wide computer column" v-for="queried_packetObject in self_store.getters.GET_FILTERED_jobs_list">

            <div class="ui large image">
               <div class="ui compact menu" style="width: 100%;">
                  <a class="item" style="width: 50%;font-size: 2em;">
                     <i class="icon mail"></i> Messages
                     <div class="floating ui red label" style="font-size: 0.79em;">22</div>
                  </a>
                  <a class="item" style="width: 50%;font-size: 2em;">
                     <i class="icon users"></i> Friends
                     <div class="floating ui teal label" style="font-size: 0.79em;">22</div>
                  </a>
               </div>
               <img :src="queried_packetObject.image" class="company-image-main-image"> <button class="ui bottom attached label company-image-leading-button"><i class="icon user"></i>
                Show More
               </button>
            </div>

      </div>

    </template>

    </div>
</template>

<style lang="scss">
  @import './CompanyImageComponentBox.css';
</style>

<script type="text/javascript'">

import { store } from '../../../store/store'

import SuiVue from 'semantic-ui-vue'

export default {
  name: 'CompanyImageComponentBox',
  props: {

  },
  data () {
    return {
      numberOfElementsPerPage: 1,
      socialMediaBoxObjectStyle: 'margin-left: 50% !important;',
      windowWidth: window.innerWidth
    }
  },
  mounted () {
    window.addEventListener('resize', () => {
      this.windowWidth = window.innerWidth
      console.log(this.isMobile)
    })
  },
  computed: {
    COMPUTED_per_page () {
      if (this.windowWidth <= 1200) {
        return 2
      } return 4
    },
    self_store () {
      return store
    }
  },
  filters: {
    FILTER_days: function (value) {
      value = parseInt(value)
      var daysTitle = 'days'
      if (value === 1) { daysTitle = 'day' } else if (value == -1 || value == 'Lifetime') {
        value = 'Lifetime'
        daysTitle = ''
        return (new String(value) + daysTitle)
      }
    }
  },
  created () {

  },
  components: {
    SuiVue
  },
  methods: {
    METHOD_divded_packetsArray (numer_of_elements) {
      var groupped_packetsArray = []
      if (this.windowWidth <= 1200) { numer_of_elements = 1 }
      if (store.getters.GET_FILTERED_jobs_list.length > numer_of_elements) {
        for (var i = 0; i <= Math.round(store.getters.GET_FILTERED_jobs_list.length / numer_of_elements); i++) {
          var local_groupped_packetsArray = []
          if ((i + 1) * numer_of_elements <= store.getters.GET_FILTERED_jobs_list.length) {
            local_groupped_packetsArray = store.getters.GET_FILTERED_jobs_list.slice(i * numer_of_elements, (i + 1) * numer_of_elements)
          } else {
            local_groupped_packetsArray = store.getters.GET_FILTERED_jobs_list.slice(i * numer_of_elements, store.getters.GET_FILTERED_jobs_list.length)
          }
          groupped_packetsArray.push(local_groupped_packetsArray)
        }
      } else {
        return store.getters.GET_FILTERED_jobs_list
      }
      return groupped_packetsArray
    }
  }
}

</script>
