<template>
  <div>
  <!--
    <sui-segment raised>
      <company-image-component-box />
    </sui-segment>

    -->

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




          <template v-if="isEmpty(self_store.getters.GET_currently_viewed_job_offer)">
          
            <company-filter-component-list style="margin-left: 1em; !important display: box !important;position: sticky;top: 5em;"/>
         
         </template>

        <template v-else>
          <div class="ui segment" style="position: sticky;top: 1em;">
            <div style="display: flex; flex-direction: column; justify-content: center; font-size: 1em; line-height: 2em; position: sticky; top: 0px; margin: auto; min-width: 60%; "><img :src="self_store.getters.GET_currently_viewed_job_offer.logo" class="ui image image-collapsed-company-version" style="margin-top: 6px; border-radius: 5em; border: 0px solid;"><br></div></div>
         </template>




        </sui-segment>

        <sui-segment style="width: 100%;">

          <!--<div v-if="self_store.getters.GET_current_action == ''">-->
            <template v-if="isEmpty(self_store.getters.GET_currently_viewed_job_offer)">
              <company-table-component-box id="top"/>
            </template>

            <template v-else>
              <client-apply-form :formObject="self_store.getters.GET_currently_viewed_job_offer" />
            </template>

          <!--</div>-->

          <!--<div v-if="self_store.getters.GET_current_action == 'createATransfer'">-->

            <!--<company-apply-form :formObject="local_test_item" :screeningQuestions="screeningQuestions"/>-->

          <!--</div>-->

        </sui-segment>

        <template v-if="isEmpty(self_store.getters.GET_currently_viewed_job_offer)">
          <sui-segment class="company-main-info-box-segment" >
            <company-info-box />
          </sui-segment>
        </template>

        <template v-else>
          <sui-segment class="company-main-info-box-segment" >
            <company-statistics-stacked-in-table  style="position: sticky; top: 1em;"  :tableObject="self_store.getters.GET_currently_viewed_job_offer" />
          </sui-segment>
        </template> 

        
      </sui-segments>

    </template>

  </div>
</template>

<style lang="scss">
  @import './Company.css';
</style>

<script type="text/javascript">

import { store } from '../../../store/store'
import CompanyFilterComponentList from '../../CompanyFilter/CompanyFilterComponentList/CompanyFilterComponentList.vue'
import CompanyImageComponentBox from '../../CompanyImageComponentBox/CompanyImageComponentBox/CompanyImageComponentBox.vue'
import CompanyInfoBox from '../../CompanyInfo/CompanyInfoBox/CompanyInfoBox.vue'
import CompanyTableComponentBox from '../../CompanyTable/CompanyTableComponentBox/CompanyTableComponentBox.vue'
import CompanyApplyForm from '../../CompanyApply/CompanyApplyForm/CompanyApplyForm.vue'
import ClientApplyForm from '../../CompanyApply/ClientApplyForm/ClientApplyForm.vue'
import CompanyStatisticsStackedInTable from '../../CompanyTable/CompanyTableComponentBase/CompanyStatisticsStackedInTable/CompanyStatisticsStackedInTable'

import VueRouter from 'vue-router'

export default {
  name: 'Company',
  data () {
    return {
      windowWidth: window.innerWidth,
      currently_viewed_job_offer: {}
    }
  },
  props: {

  },
  methods: {
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
    }
  },
  mounted () {
    window.addEventListener('resize', () => {
      this.windowWidth = window.innerWidth
      console.log(this.isMobile)
    })
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
    }
  },
  watch: {
    COMPUTED_currently_viewed_job_offer (newObject, oldObject) {
      this.currently_viewed_job_offer = newObject
    }
  },
  components: {
    ClientApplyForm,
    CompanyFilterComponentList,
    CompanyImageComponentBox,
    CompanyInfoBox,
    CompanyTableComponentBox,
    CompanyApplyForm,
    VueRouter,
    CompanyStatisticsStackedInTable
  },
  watch: {
  },
  created () {
    store.dispatch('fetchJobTypes').then(() => {
      store.dispatch('fetchCompaniesAndJobs').then(() => {
      })
    })
  }
}

</script>
