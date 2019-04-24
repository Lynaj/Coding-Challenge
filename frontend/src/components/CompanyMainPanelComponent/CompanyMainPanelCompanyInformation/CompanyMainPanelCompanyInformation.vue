<template>

  <div style="text-align: left;display: flex;flex-direction: column;justify-content: center;">

    <div class="apply-form-first-step-sub-div" style="float: left;display: block;margin: auto;">

      <!-- Company Name -->

      <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
        <label class="label">Company Name</label>
        <div class="control">
          <input
            :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.name.$error) ? 'ui-input-box-div-is-danger' : '']"
            type="text" style="width: 80%;" placeholder=""
            v-model="form.name">
        </div>
        <p v-if="$v.form.name.$error" class="help is-danger">Your company name is invalid</p>
      </div>

      <!-- Website -->

      <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
        <label class="label">Website</label>
        <div class="control">
          <input
            :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.website.$error) ? 'ui-input-box-div-is-danger' : '']"
            type="text" style="width: 80%;" placeholder=""
            v-model="form.website">
        </div>
        <p v-if="$v.form.website.$error" class="help is-danger">Website address is invalid</p>
      </div>

      <!-- Social Media -->

      <div v-for="(socialMediaPlatform, index) in $v.form.social_media.$each.$iter">


        <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
          <label class="label">{{ socialMediaPlatform.platform_type.$model }}</label>
          <div class="control">

            <input style="width: 80%;"
                   :class="['input ui-input-box-div ui-input-box-div-text', (!socialMediaPlatform.nickname.required) ? 'ui-input-box-div-is-danger' : '']"
                   v-model.trim="socialMediaPlatform.nickname.$model">

<!--            <input disabled style="width: 80%;"-->
<!--                   :class="['input ui-input-box-div ui-input-box-div-text', (!socialMediaPlatform.url.required) ? 'ui-input-box-div-is-danger' : '']"-->
<!--                   v-model.trim="socialMediaPlatform.url.$model">-->

          </div>
          <p v-if="$v.form.website.$error" class="help is-danger">Website address is invalid</p>
        </div>

        <p v-if="!socialMediaPlatform.nickname.required" class="help is-danger">This field cannot be
          empty.</p>


      </div>

      <!-- Logo -->
      <transition name="fade">
        <div v-if="!BOOL_dataLoadingSpinner">

          <div
            style="display: flex;justify-content: center;font-size: 2.5em;margin-bottom: 2em;margin-top: 2em;color: #6e6e6d;text-decoration: 1px solid;text-align: center;line-height: 1em;"
            v-if="form.logo !== null && form.logo !== undefined && form.logo.length > 0 ">

            <div class="text-reader text-reader-div-inside logo-uploaded-div" :style="COMPUTED_logo_div_style">

            </div>

          </div>

        </div>
      </transition>

      <transition name="fade">

        <div v-if="BOOL_dataLoadingSpinner">

          <circle-loader class="spinner-class" loading="self_store.getters.GET_isLoading_FILTERED_jobs_list"
                         color="black" size=135 sizeUnit="px"/>

        </div>

        <div class="text-reader-div" style="margin-bottom: 5em;">
          <div @click="$refs.file.click()" :class="['', ($v.form.logo.$error) ? 'ui-input-box-div-is-danger' : '']"
               style="display: flex;flex-direction: column;border-radius: 10px 10px 10px 10px;-moz-border-radius: 10px 10px 10px 10px;-webkit-border-radius: 10px 10px 10px 10px;border: 3px solid #d9d9d9;-webkit-box-shadow: -35px 35px 1px 0px rgba(0,0,0,0.75);-moz-box-shadow: -35px 35px 1px 0px rgba(0,0,0,0.75);box-shadow: -24px 23px 0px 0px rgba(0,0,0,0.75);">

            <label :style="{ backgroundImage: 'url(\'' + self_store.getters.GET_upload_icon + '\')' }"
                   class="text-reader text-reader-div-inside">
              <input ref="file" style="display: none" @change="loadTextFromFile" type="file">
            </label>

            <div style="font-size: 2em;line-height: 2em;text-align: center;margin-left: 1.2em;margin-right: 1.2em;">
              <template v-if="form.logo !== null && form.logo !== undefined && form.logo.length > 0 ">
                Upload your Logo
              </template>
              <template v-else>
                Change your Logo
              </template>
            </div>

          </div>


        </div>

        <p style="margin: auto;" v-if="$v.form.logo.$error" class="help is-danger">This field is invalid.</p>


      </transition>


      <transition name="fade">

        <!-- <div v-if="!loading"> -->

        <button v-on:click="updateCompanyInformation" data-v-3ee86246="" class="bottom only-next">
          <div data-v-3ee86246="" class="next-main-div-button stepper-button next deactivated">
            <span data-v-3ee86246="">Update</span>
          </div>
        </button>

        <!-- </div>

        <div v-else>
          <circle-loader class="spinner-class" loading=true color="black" size="135" sizeUnit="px"/>
        </div>
 -->
      </transition>

    </div>

  </div>

</template>

<style lang="scss">
  @import './CompanyMainPanelCompanyInformation.css';
</style>

<script type="text/javascript">
  import {store} from '../../../store/store'
  import VueSwal from 'vue-swal'
  import {validationMixin} from 'vuelidate'
  import {required, email, url, minLength} from 'vuelidate/lib/validators'
  import Vuelidate from 'vuelidate'
  import {mapGetters, mapActions} from 'vuex'
  import SuiVue from 'semantic-ui-vue'
  import {CircleLoader} from '@saeris/vue-spinners'

  export default {
    name: 'CompanyMainPanelCompanyInformation',
    mixins: [validationMixin],
    props: {
      clickedNext: '',
      currentStep: ''
    },
    validations: {
      form: {
        id: {},
        name: {
          required
        },
        website: {
          required
          // url
        },
        logo: {
          required
        },
        social_media: {
          required: true,
          $each: {
            platform_type: {
              required
              // minLength: minLength(2)
            },
            nickname: {
              required
            },
            url: {
              // minLength: minLength(2)
            }
          }
        }
      }
    },
    data() {
      return {
        windowWidth: window.innerWidth,
        form: {
          id: '',
          name: '',
          website: '',
          logo: '',
          social_media: []
        },
        initialLoaderTimeStamp: 0,
        minimumTimeToWaitUntilHideSpinner: 3,
        BOOL_dataLoadingSpinner: false
      }
    },
    computed: {
      self_store() {
        return store;
      },
      COMPUTED_logo_div_style() {
        return "background-image: url('" + this.form.logo + "');"
        // http://localhost:8000/media/company/logo/9bf582a0e22343e0948d2784259e3cc8.jpeg
      },
      COMPUTED_company_info() {
        return store.getters['user/GET_COMPANY_INFORMATION']
      }
    },
    components: {
      CircleLoader,
      VueSwal,
      Vuelidate,
      SuiVue
    },
    methods: {
      loadTextFromFile(ev) {
        this.BOOL_dataLoadingSpinner = true
        this.initialLoaderTimeStamp = new Date()
        const file = ev.target.files[0]
        const reader = new FileReader()
        var self = this
        reader.onload = function (e) {
          self.form.logo = e.target.result;
          if ((new Date() - self.initialLoaderTimeStamp) / 1000 < self.minimumTimeToWaitUntilHideSpinner) {
            setTimeout(
              function () {
                self.BOOL_dataLoadingSpinner = false
              }, (self.minimumTimeToWaitUntilHideSpinner * 1000 - (new Date() - self.initialLoaderTimeStamp)))
          } else {
            self.BOOL_dataLoadingSpinner = false
          }
        }
        reader.readAsDataURL(file)
      },
      updateCompanyInformation() {
        var self = this
        this.$v.$touch()
        // if (!self.$v.$invalid) {
        self.loading = true;

        var localData = {
          data: this.form,
          token: localStorage.getItem('jwt')
        };

        store.dispatch('user/changeCompanyInformation', localData).then((response) => {
          if (response.status == 200) {
            this.$swal('Account data has been updated').then(() => {
              console.log('done')
            })
          } else if (response.response.status == 401) {
            let payload = {
              router: this.$router,
              swal: this.$swal
            };
            store.dispatch('informUserNotLoggedIn', payload);
          } else {
            // Building error message
            var wrapper = document.createElement('div');

            for (var property in response.response.data.offer) {
              if (response.response.data.offer.hasOwnProperty(property)) {
                if (response.response.data.offer[property][0] !== undefined) {
                  var fieldName = property.replace(/.+_/g, "");
                  wrapper.innerHTML += (fieldName.charAt(0).toUpperCase() + fieldName.substring(1) + ': ' + response.response.data.offer[property][0] + '<br>');
                }
              }
            }

            this.$swal(
              {
                text: "Something went wrong!:",
                content: wrapper
              }
            );
          }
          self.loading = false;
          self.METHOD_resetCurrentView()
        }).catch(error => {

          console.log('error: ' + JSON.stringify((error)));
          // Building error message
          var wrapper = document.createElement('div');
          wrapper.innerHTML = error;

          this.$swal(
            {
              text: "Something aawent wrong!:",
              content: wrapper
            }
          );


          self.METHOD_resetCurrentView();
          console.log(error)
        })
        // }
      }
    },
    watch: {
      $v: {
        handler: function (val) {
          if (!val.$invalid) {
            this.$emit('can-continue', {value: true})
          } else {
            this.$emit('can-continue', {value: false})
          }
        },
        deep: true
      },
      clickedNext(val) {
        if (val === true) {
          this.$v.form.$touch()
        }
      },
      COMPUTED_form_message(val) {

      }
    },
    created() {
      window.addEventListener('resize', () => {
        this.windowWidth = window.innerWidth
      });

      // fetching user data information
      var self = this;
      var data = {
        token: localStorage.getItem('jwt')
      };

      store.dispatch('user/fetchCompanyInformation', data).then(() => {
        var local_form = store.getters['user/GET_COMPANY_INFORMATION'];
        self.form = store.getters['user/GET_COMPANY_INFORMATION'];
        self.loading = false;
      });

    }
  }

</script>
