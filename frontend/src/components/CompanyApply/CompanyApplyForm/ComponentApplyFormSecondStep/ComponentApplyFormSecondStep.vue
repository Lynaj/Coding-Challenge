<template>
  <div>

    <transition name="fade">
      <div v-if="!BOOL_dataLoadingSpinner">

        <div style="display: flex;justify-content: center;font-size: 2.5em;margin-bottom: 2em;margin-top: 2em;color: #6e6e6d;text-decoration: 1px solid;text-align: center;line-height: 1em;" v-if="!isEmpty(self_store.getters.GET_currently_viewed_job_offer_answers.linkedCVFile)">
          {{ message.currently_displayed}}
        </div>

      </div>
    </transition>

    <transition name="fade">

      <div v-if="BOOL_dataLoadingSpinner">

        <circle-loader class="spinner-class" loading="self_store.getters.GET_isLoading_FILTERED_jobs_list" color="black" size=135 sizeUnit="px"/>

      </div>

      <div class="text-reader-div" style="margin-bottom: 5em;">
         <div v-on:click="$refs.file.click()" style="display: flex;flex-direction: column;border-radius: 10px 10px 10px 10px;-moz-border-radius: 10px 10px 10px 10px;-webkit-border-radius: 10px 10px 10px 10px;border: 3px solid #d9d9d9;-webkit-box-shadow: -35px 35px 1px 0px rgba(0,0,0,0.75);-moz-box-shadow: -35px 35px 1px 0px rgba(0,0,0,0.75);box-shadow: -24px 23px 0px 0px rgba(0,0,0,0.75);">

            <div class="image-preview" v-if="imageData.length > 0">
              <img class="preview" :src="imageData" @error="imageLoadError" >
            </div>

            <label :style="{ backgroundImage: 'url(\'' + self_store.getters.GET_upload_icon + '\')' }" class="text-reader text-reader-div-inside" >
              <input ref="file" style="display: none" @change="previewImage" type="file">
            </label>

            <div style="font-size: 2em;line-height: 2em;text-align: center;margin-left: 1.2em;margin-right: 1.2em;">
              {{ text_placeholder }}
            </div>

         </div>
      </div>

    </transition>
  </div>
</template>

<style lang="scss">
  @import './ComponentApplyFormFirstStep.css';
</style>

<script type="text/javascript">
import VueSwal from 'vue-swal'
import {validationMixin} from 'vuelidate'
import { CircleLoader } from '@saeris/vue-spinners'
import {required, email} from 'vuelidate/lib/validators'
import Toasted from 'vue-toasted'
import Vuelidate from 'vuelidate'
import { store } from '../../../../store/store'

export default {
  name: 'ComponentApplyFormSecondStep',
  methods: {
    imageLoadError () {
      this.message.currently_displayed = this.message.negative
    },
    isEmpty (obj) {
      for (var key in obj) {
        if (obj.hasOwnProperty(key)) { return false }
      }
      return true
    },
    previewImage: function (event) {
      // Reference to the DOM input element
      this.BOOL_dataLoadingSpinner = true
      var fileTypes = ['jpg', 'jpeg', 'png', 'pdf']
      this.initialLoaderTimeStamp = new Date()
      var self = this

      var input = event.target
      // Ensure that you have a file before attempting to read it
      if (input.files && input.files[0]) {
        var extension = input.files[0].name.split('.').pop().toLowerCase(), // file extension from input file
          isSuccess = fileTypes.indexOf(extension) > -1

        if (isSuccess) {
          // create a new FileReader to read this image and convert to base64 format
          var reader = new FileReader()
          // Define a callback function to run, when FileReader finishes its job
          reader.onload = (e) => {
            if ((new Date() - self.initialLoaderTimeStamp) / 1000 < self.minimumTimeToWaitUntilHideSpinner) {
              setTimeout(
                function () {
                  self.BOOL_dataLoadingSpinner = false
                  self.imageData = e.target.result
                  self.$emit('imageFile', {value: e.target.result})
                }, (self.minimumTimeToWaitUntilHideSpinner * 1000 - (new Date() - self.initialLoaderTimeStamp)))
            } else {
              self.BOOL_dataLoadingSpinner = false
              self.$emit('imageFile', {value: e.target.result})
            }

            self.message.currently_displayed = self.message.positive
          }
          reader.readAsDataURL(input.files[0])
        } else {
          self.BOOL_dataLoadingSpinner = false

          let toast = self.$toasted.show('<div style="display: flex;flex-direction: column;justify-content: center;"><div style="margin-top: 1em;">Wrong file format! <br></div><div style="margin-top: 1em;display: flex;float: left;"><div style="text-align: left;">Accepted:</div><div><ul style="margin: auto;display: block;"> <li>jpg</li><li>jpeg</li><li>png</li><li>pdf</li></ul></div></div></div>', {
            theme: 'bubble',
            position: 'top-right',
            duration: 25000
          })
        }

        // Start the reader job - read file as a data url (base64 format)
      } else {
        self.BOOL_dataLoadingSpinner = false
      }
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
              self.$emit('imageFile', {value: e.target.result })
            }, (self.minimumTimeToWaitUntilHideSpinner * 1000 - (new Date() - self.initialLoaderTimeStamp)))
        } else {
          self.BOOL_dataLoadingSpinner = false
          self.$emit('imageFile', {value: ''})
        }
      }
      reader.readAsDataURL(file)
    }
  },
  components: {
    CircleLoader,
    Toasted
  },
  data () {
    return {
      windowWidth: window.innerWidth,
      initialLoaderTimeStamp: 0,
      minimumTimeToWaitUntilHideSpinner: 3,
      BOOL_dataLoadingSpinner: false,
      imageData: '',
      message: {
        currently_displayed: '',
        positive: 'You have succesfully uploaded an image',
        negative: 'Something went wrong!'
      }
    }
  },
  props: {
    text_placeholder: ''
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
