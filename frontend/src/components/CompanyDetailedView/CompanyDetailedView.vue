<template>
  <div>
    <sui-segment raised>

      <company-image-component-image :imageObject="queriedCompany.image" />
    
    <!-- Facebook -->
    <div style="display: flex; flex-direction: row;">
      <template v-if="METHOD_socialMediaIcon('SOCIAL_MEDIA.FACEBOOK')">
        <div style="margin-left: 2em !important;" v-on:click="METHOD_redirect('SOCIAL_MEDIA.FACEBOOK')">
          <svg version="1.1" role="presentation" width="42" height="48" viewBox="0 0 448 512" class="fa-icon" style="font-size: 3em;" color="#3B5998"><path d="M448 56.7V455.2C448 468.9 436.9 479.9 423.3 479.9H309.1V306.5H367.3L376 238.9H309V195.7C309 176.1 314.4 162.8 342.5 162.8H378.3V102.3C372.1 101.5 350.9 99.6 326.1 99.6 274.5 99.6 239.1 131.1 239.1 189V238.9H180.7V306.5H239.1V480H24.7C11.1 480 0 468.9 0 455.3V56.7C0 43.1 11.1 32 24.7 32H423.2C436.9 32 448 43.1 448 56.7z"></path><!----></svg> 
        </div>
      </template>
      <!-- linkedin -->
      <template v-if="METHOD_socialMediaIcon('SOCIAL_MEDIA.TWITTER')">
        <div style="margin-left: 2em !important;" v-on:click="METHOD_redirect('SOCIAL_MEDIA.LINKEDIN')">
         <svg version="1.1" role="presentation" width="42" height="48" viewBox="0 0 448 512" class="fa-icon" style="font-size: 3em;" color="#1DA1F2"><path d="M400 32H48C21.5 32 0 53.5 0 80V432C0 458.5 21.5 480 48 480H400C426.5 480 448 458.5 448 432V80C448 53.5 426.5 32 400 32zM351.1 190.8C351.3 193.6 351.3 196.5 351.3 199.3 351.3 286 285.3 385.9 164.7 385.9 127.5 385.9 93 375.1 64 356.5 69.3 357.1 74.4 357.3 79.8 357.3 110.5 357.3 138.7 346.9 161.2 329.3 132.4 328.7 108.2 309.8 99.9 283.8 110 285.3 119.1 285.3 129.5 282.6 99.5 276.5 77 250.1 77 218.2V217.4C85.7 222.3 95.9 225.3 106.6 225.7A65.4-65.4 0 0 0 77.4 171.1C77.4 158.9 80.6 147.7 86.3 138 118.6 177.8 167.1 203.8 221.5 206.6 212.2 162.1 245.5 126 285.5 126 304.4 126 321.4 133.9 333.4 146.7 348.2 143.9 362.4 138.4 375 130.9 370.1 146.1 359.8 158.9 346.2 167 359.4 165.6 372.2 161.9 384 156.8 375.1 169.9 363.9 181.5 351.1 190.8z"></path><!----></svg>
        </div>
      </template>
      <!-- twitter --> 

      <template v-if="METHOD_socialMediaIcon('SOCIAL_MEDIA.LINKEDIN')">
        <div style="margin-left: 2em !important;" v-on:click="METHOD_redirect('SOCIAL_MEDIA.TWITTER')">
          <svg version="1.1" role="presentation" width="42" height="48" viewBox="0 0 448 512" class="fa-icon" style="font-size: 3em;" color="#0077B5"><path d="M100.3 480H7.4V180.9H100.3V480zM53.8 140.1C24.1 140.1 0 115.5 0 85.8 0 56.1 24.1 32 53.8 32 83.5 32 107.6 56.1 107.6 85.8 107.6 115.5 83.5 140.1 53.8 140.1zM448 480H355.3V334.4C355.3 299.7 354.6 255.2 307 255.2 258.7 255.2 251.3 292.9 251.3 331.9V480H158.5V180.9H247.6V221.7H248.9C261.3 198.2 291.6 173.4 336.8 173.4 430.8 173.4 448.1 235.3 448.1 315.7V480z"></path><!----></svg>
        </div>
      </template>
    </div>
    
    </sui-segment>

    <template v-if="windowWidth <= 1300">

      <sui-segments vertical >

        <sui-segment style="position: relative !important;" >
          
          <template v-if="isEmpty(self_store.getters.GET_currently_viewed_job_offer)">
            
              <company-filter-component-list style="margin-left: 1em; !important display: box !important;position: sticky;top: 5em;"/>
           
           </template>

        </sui-segment>

        <sui-segment style="width: 100%;">

          <div v-if="self_store.getters.GET_current_action == ''">
            <template v-if="isEmpty(self_store.getters.GET_currently_viewed_job_offer)">
              <company-table-component-box id="top"/>
            </template>

            <template v-else>
              <client-apply-form :formObject="self_store.getters.GET_currently_viewed_job_offer" />
            </template>

          </div>

          <div v-if="self_store.getters.GET_current_action == 'createATransfer'">
          

            <company-apply-form :formObject="local_test_item" :screeningQuestions="screeningQuestions"/>

          </div>

        </sui-segment>
        
        <template v-if="isEmpty(self_store.getters.GET_currently_viewed_job_offer)">
        
          <sui-segment class="company-main-info-box-segment" >
            <company-info-box />
          </sui-segment>

        </template>

        <template v-else>
          <company-statistics-stacked-in-table :tableObject="self_store.getters.GET_currently_viewed_job_offer" />
        </template> 


      </sui-segments>

    </template>

    <template v-else>

      <sui-segments horizontal >

        <sui-segment style="position: relative !important;" >


<!-- 

    1. logo

    2. company table wiht job offers

    3. company information

id:1
image:"http://localhost:8000/media/binance-logo.png"
name:"Binance"
social_media:Array[2]
0:Object
1:Object
website:"https://www.glassdoor.com/Jobs/Binance-Jobs-E1816824.htm"

-->



          <template v-if="isEmpty(self_store.getters.GET_currently_viewed_job_offer)">
          
            <company-filter-component-list style="margin-left: 1em; !important display: box !important;position: sticky;top: 5em;"/>
         
         </template>

        <template v-else>
          <div class="ui segment" style="position: sticky;top: 1em;">
            <div style="display: flex; flex-direction: column; justify-content: center; font-size: 1em; line-height: 2em; position: sticky; top: 0px; margin: auto; min-width: 60%; "><img :src="self_store.getters.GET_currently_viewed_job_offer.logo" class="ui image image-collapsed-company-version" style="margin-top: 6px; border-radius: 5em; border: 0px solid;"><br></div></div>
         </template>




        </sui-segment>

        <sui-segment style="width: 100%;">

          <div v-if="self_store.getters.GET_current_action == ''">
            <template v-if="isEmpty(self_store.getters.GET_currently_viewed_job_offer)">
              <company-table-component-box id="top"/>
            </template>

            <template v-else>
              <client-apply-form :formObject="self_store.getters.GET_currently_viewed_job_offer" />
            </template>

          </div>

          <div v-if="self_store.getters.GET_current_action == 'createATransfer'">

            <company-apply-form :formObject="local_test_item" :screeningQuestions="screeningQuestions"/>

          </div>

        </sui-segment>

        
      </sui-segments>

    </template>

  </div>
</template>

<style lang="scss">
  @import './CompanyDetailedView.css';
</style>

<script type="text/javascript">

import { mapState } from 'vuex';
import { store } from '../../store/store'
import CompanyFilterComponentList from '../CompanyFilter/CompanyFilterComponentList/CompanyFilterComponentList.vue'
import CompanyImageComponentImage from '../CompanyImageComponentBox/CompanyImageComponentImage/CompanyImageComponentImage.vue'
import CompanyInfoBox from '../CompanyInfo/CompanyInfoBox/CompanyInfoBox.vue'
import CompanyTableComponentBox from '../CompanyTable/CompanyTableComponentBox/CompanyTableComponentBox.vue'
import CompanyApplyForm from '../CompanyApply/CompanyApplyForm/CompanyApplyForm.vue'
import ClientApplyForm from '../CompanyApply/ClientApplyForm/ClientApplyForm.vue'
import CompanyStatisticsStackedInTable from '../CompanyTable/CompanyTableComponentBase/CompanyStatisticsStackedInTable/CompanyStatisticsStackedInTable'
import { Facebook, Twitter, LinkedIn } from 'vue-socialmedia-share';
import VueRouter from 'vue-router'
import Toasted from 'vue-toasted'

export default {
  name: 'CompanyDetailedView',
  data () {
    return {
      windowWidth: window.innerWidth,
      queriedCompany: {
        id: 0
      },
      emptyData: false,
      initialJobsList: store.getters.GET_jobs_list
    }
  },
  props: {

  },
  methods: {
    METHOD_querySocialMediaPlatform(platformName, objectToReceive) {
      var queriedPlatform = this.queriedCompany.social_media.find(
        socialMediaPlatform => socialMediaPlatform.platform_type.toLowerCase() === platformName.toLowerCase()
      )
      if(queriedPlatform !== undefined && queriedPlatform !== 'undefined') {
        try {
          return queriedPlatform[objectToReceive];
        } catch(e) {
          return false;
        }
      } else {
        return false;
      }
    },
    METHOD_socialMediaIcon: function(platformName) {
      if(this.queriedCompany.social_media !== undefined
        && this.queriedCompany.social_media !== 'undefined') {
          return this.METHOD_querySocialMediaPlatform(
            platformName,
            'nickname'
          );
      } else {
        return false;
      }
    },
    METHOD_redirect: function(platformName) {
      let queriedUrl = this.METHOD_querySocialMediaPlatform(
        platformName,
        'url'
      )
      if(queriedUrl !== undefined 
        && queriedUrl !== 'undefined'){
        window.open(queriedUrl, '_blank'); 
      } else {
        let toast = self.$toasted.show('Something went wrong! Please, contact administration!', {
            theme: 'bubble',
            position: 'top-right',
            duration: 25000
          })
        }
    },
    isEmpty: function (obj) {
      for (var key in obj) {
        if (obj.hasOwnProperty(key)) { return false }
      }
      return true
    },
    METHOD_change_path: function (nameOfThePath) {
      if (nameOfThePath == 'login') {
        store.commit('MUTATE_currentAction', 'login')
      }
      this.$router.push(nameOfThePath)
    },
    FilterCompany() {
      var self = this;
      var localCompanyName = self.$route.params.company_name.split(' ').join('_').toLowerCase();
      if(localCompanyName.length > 0) {
        var localQuriedCompany = {};
        var localQuriedCompany = store.getters.GET_companies_list.find(
          company => company.name.split(' ').join('_').toLowerCase() === localCompanyName
        );

        if(Object.keys(localQuriedCompany).length) {
          // preparing data for job listing
          self.queriedCompany = localQuriedCompany;
          this.FilterJobs();
        }

      } else {
        this.emptyData = true;
      }
    },
    FilterJobs() {
      var self = this;
      var localJobList = store.getters.GET_jobs_list.filter(
        job => job.company_name.split(' ').join('_').toLowerCase() === self.queriedCompany.name.split(' ').join('_').toLowerCase()
      )
      store.commit('MUTATE_JOBS_LIST', localJobList);
      store.commit('MUTATE_FILTERED_JOB_LIST', localJobList);
    }
  },
  mounted () {
    window.addEventListener('resize', () => {
      this.windowWidth = window.innerWidth
    })

  },
  destroyed() {
    if(this.initialJobsList.length > 0){
      store.commit('MUTATE_JOBS_LIST', this.initialJobsList)
    } else {
      store.commit('MUTATE_JOBS_LIST', localJobs_list)
    }
  },
  computed: {
    COMPUTED_currently_viewed_job_offer () {
      return store.getters.GET_currently_viewed_job_offer
    },
    COMPUTED_local_currently_viewed_job_offer () {
      return this.currently_viewed_job_offer
    },
    self_store () {
      return store
    },
    STORE_JOBS_LIST() {
      return store.getters.GET_jobs_list
    }
  },
  components: {
    Facebook,
    Toasted, 
    Twitter, 
    LinkedIn,
    ClientApplyForm,
    CompanyFilterComponentList,
    CompanyImageComponentImage,
    CompanyInfoBox,
    CompanyTableComponentBox,
    CompanyApplyForm,
    VueRouter,
    CompanyStatisticsStackedInTable
  },
  watch: {
    STORE_FILTERED_JOB_LIST(newVal, oldVal) {

    }
  },
  created () {
    var self = this;
    store.dispatch('fetchJobTypes').then(() => {
      store.dispatch('fetchCompaniesAndJobs').then(() => {
        self.FilterCompany();
      })
    })
  }
}

</script>
