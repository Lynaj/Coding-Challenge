<template>
  <div>

    <transition name="fade">
      <div v-if="!BOOL_dataLoadingSpinner">

        <div style="display: flex;justify-content: center;font-size: 2.5em;margin-bottom: 2em;margin-top: 2em;color: #6e6e6d;text-decoration: 1px solid;text-align: center;line-height: 1em;" v-if="!isEmpty(self_store.getters.GET_currently_viewed_job_offer_answers.linkedCVFile)">
          You have succesfully uploaded a file!
        </div>

      </div>
    </transition>

    <transition name="fade">

      <div v-if="BOOL_dataLoadingSpinner">

        <circle-loader class="spinner-class" loading="self_store.getters.GET_isLoading_FILTERED_jobs_list" color="black" size=135 sizeUnit="px"/>

      </div>

      <div class="text-reader-div" style="margin-bottom: 5em;">
         <div @click="$refs.file.click()" style="display: flex;flex-direction: column;border-radius: 10px 10px 10px 10px;-moz-border-radius: 10px 10px 10px 10px;-webkit-border-radius: 10px 10px 10px 10px;border: 3px solid #d9d9d9;-webkit-box-shadow: -35px 35px 1px 0px rgba(0,0,0,0.75);-moz-box-shadow: -35px 35px 1px 0px rgba(0,0,0,0.75);box-shadow: -24px 23px 0px 0px rgba(0,0,0,0.75);">

            <label :style="{ backgroundImage: 'url(\'' + self_store.getters.GET_upload_icon + '\')' }" class="text-reader text-reader-div-inside" >
              <input ref="file" style="display: none" @change="loadTextFromFile" type="file">
            </label>

            <div style="font-size: 2em;line-height: 2em;text-align: center;margin-left: 1.2em;margin-right: 1.2em;">
              Upload your CV
            </div>

         </div>
      </div>

    </transition>
  </div>
</template>

<style lang="scss">
  @import './ClientApplyFormSecondStep.css';
</style>

<script type="text/javascript">
import VueSwal from 'vue-swal'
import {validationMixin} from 'vuelidate'
import { CircleLoader } from '@saeris/vue-spinners'
import {required, email} from 'vuelidate/lib/validators'
import Vuelidate from 'vuelidate'
import { store } from '../../../../store/store'

export default {
  name: 'ClientApplyFormSecondStep',
  methods: {

    isEmpty (obj) {
      for (var key in obj) {
        if (obj.hasOwnProperty(key)) { return false }
      }
      return true
    },

    loadTextFromFile (ev) {
      this.BOOL_dataLoadingSpinner = true
      this.initialLoaderTimeStamp = new Date()
      const file = ev.target.files[0]
      const reader = new FileReader()
      var self = this
      reader.onload = function (e) {
        store.commit('MUTATE_CURRENTLY_VIEWED_JOB_OFFER_ANSWER_CV', e.target.result)
        if ((new Date() - self.initialLoaderTimeStamp) / 1000 < self.minimumTimeToWaitUntilHideSpinner) {
          setTimeout(
            function () {
              self.BOOL_dataLoadingSpinner = false
              self.$emit('can-continue', {value: true})
            }, (self.minimumTimeToWaitUntilHideSpinner * 1000 - (new Date() - self.initialLoaderTimeStamp)))
        } else {
          self.BOOL_dataLoadingSpinner = false
          self.$emit('can-continue', {value: true})
        }
      }
      reader.readAsDataURL(file)
    }
  },
  components: {
    CircleLoader
  },
  data () {
    return {
      windowWidth: window.innerWidth,
      initialLoaderTimeStamp: 0,
      minimumTimeToWaitUntilHideSpinner: 3,
      BOOL_dataLoadingSpinner: false,
      form: {
        username: '',
        demoEmail: '',
        message: ''
      }
    }
  },
  computed: {
    getViewedJobs () {
      return store.getters.GET_currently_viewed_job_offer_answers
    },
    self_store () {
      return store
    }
  }
}
</script>

<style>
.text-reader-div {
  display: flex;
  justify-content: center;
}
.text-reader {
  position: relative;
  overflow: hidden;
  display: inline-block;

  /* Fancy button looking */
  border-radius: 5px;
  padding: 8px 12px;
  cursor: pointer;
}
.text-reader input {
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
  opacity: 0;
}
</style>
