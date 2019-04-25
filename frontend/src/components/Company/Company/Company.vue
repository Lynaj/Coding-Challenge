<template>
  <div style="justify-content: center;display: flex;">

      <sui-segments horizontal>

        <template v-if="isEmpty(self_store.getters.GET_currently_viewed_transaction)">
          <sui-segment class="company-main-info-box-segment" >
            <company-info-box />
          </sui-segment>
        </template>

        
      </sui-segments>
  </div>
</template>

<style lang="scss">
  @import './Company.css';
</style>

<script type="text/javascript">

import { store } from '../../../store/store'
import CompanyInfoBox from '../../CompanyInfo/CompanyInfoBox/CompanyInfoBox.vue'

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
