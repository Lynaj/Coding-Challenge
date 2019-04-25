<template>
  <div style="justify-content: center;display: flex;">

      <sui-segments horizontal style="display: flex;flex-direction: column;justify-content: center;">

        <sui-segment style="margin-top: 2em !important; margin-bottom: 2em !important;"  >
          <company-info-box />
        </sui-segment>


        <sui-segment style="width: 100%;display: block;margin: auto;">
          <company-table-with-transactions id="top" />
        </sui-segment>


      </sui-segments>
  </div>
</template>

<style lang="scss">
  @import './Company.css';
</style>

<script type="text/javascript">

import { store } from '../../../store/store'
import CompanyInfoBox from '../../CompanyInfo/CompanyInfoBox/CompanyInfoBox.vue'
import CompanyTableWithTransactions from '../../CompanyMainPanelComponent/CompanyTableWithTransactions/CompanyTableWithTransactions'
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
    self_store () {
      return store
    }
  },
  watch: {
  },
  components: {
    CompanyInfoBox,
    CompanyTableWithTransactions,
    VueRouter
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
