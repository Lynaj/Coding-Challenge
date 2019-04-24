<template>

  <div style="padding: 2rem 3rem; text-align: left;display: flex;flex-direction: column;justify-content: center;">

    <div class="apply-form-first-step-sub-div" style="float: left;display: block;margin: auto;">

        <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">Company Name</label>
            <div class="control">
                <input :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.companyName.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder=""
                       v-model="form.companyName">
            </div>
            <p v-if="$v.form.companyName.$error" class="help is-danger">Your comapny name is invalid</p>
        </div>

        <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">Job Title</label>
            <div class="control">
                <input :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.jobTitle.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder=""
                       v-model="form.jobTitle">
            </div>
            <p v-if="$v.form.jobTitle.$error" class="help is-danger">Your job title is invalid</p>
        </div>

        <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">Description</label>
            <div class="control">
                <textarea :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.description.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder=""
                       v-model="form.description">
                 </textarea>
            </div>
            <p v-if="$v.form.description.$error" class="help is-danger">Your description is invalid</p>
        </div>

        <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">Salary</label>
            <div class="control">
                <input placeholder="$5000/month" :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.salary.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;"
                       v-model="form.salary">
            </div>
            <p v-if="$v.form.salary.$error" class="help is-danger">Your salary is invalid</p>
        </div>

        <div class="field" style="margin: 3em; width: 100%;display: flex;flex-direction: row;justify-content: flex-start;">
           <div style=" display: flex;flex-direction: row;justify-content: left;">
              <label class="label" style="line-height: 131%;margin-right: 1em;">Location</label>
              <div class="control">
                <places
                  :class="['', ($v.form.location.$error) ? 'ui-input-box-div-is-danger' : '']"
                  v-model="form.location.label"
                  placeholder="Choose Location"
                  @change="val => { form.location.data = val }"
                  >
                </places>

              </div>
              <p v-if="$v.form.location.$error" class="help is-danger">Your location is invalid</p>
          </div>

          <div style="display: flex;flex-direction: row;justify-content: left;margin-left: 5em;" class="field">
              <label class="label" style="line-height: 131%;margin-right: 1em;">Remote</label>
              <div class="control">
                  <input :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.remote.$error) ? 'ui-input-box-div-is-danger' : '']" type="checkbox" style="width: 20%; float:left; margin-top: 50%" placeholder=""
                         v-model="form.remote">
              </div>
              <p v-if="$v.form.remote.$error" class="help is-danger">Your remote is invalid</p>
          </div>
       </div>

         <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">Type</label>
            <div class="control">
              <multiselect style="max-width: 50% !important;" :class="['input', ($v.form.type.$error) ? 'ui-input-box-div-is-danger' : '']":searchable="true" :close-on-select="true" :show-labels="false" placeholder="Choose type" :multiple="false"  v-model="form.type" :options="arrayOfTypes"></multiselect>
            </div>
            <p v-if="$v.form.type.$error" class="help is-danger">Your job type is invalid</p>
        </div>

        <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">Category</label>
            <div class="control">
              <multiselect style="max-width: 50% !important;" :class="['input', ($v.form.type.$error) ? 'ui-input-box-div-is-danger' : '']":searchable="true" :close-on-select="false" :show-labels="false" placeholder="Choose categories" :multiple="true"  v-model="form.category" :options="arrayOfCategories"></multiselect>
            </div>
            <p v-if="$v.form.category.$error" class="help is-danger">Your category is invalid</p>
        </div>

        <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">Skills</label>
            <div class="control">
                <multiselect style="max-width: 50% !important;" :class="['input', ($v.form.type.$error) ? 'ui-input-box-div-is-danger' : '']":searchable="true" :close-on-select="false" :show-labels="false" placeholder="Choose skills" :multiple="true"  v-model="form.skills" :options="arrayOfSkills"></multiselect>
            </div>
            <p v-if="$v.form.skills.$error" class="help is-danger">Your skills are invalid</p>
        </div>

        <!-- Company Information -->

         <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">Company Twitter</label>
            <div class="control">
                <input :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.twitterSocialMedia.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder=""
                       v-model="form.twitterSocialMedia">
            </div>
            <p v-if="$v.form.twitterSocialMedia.$error" class="help is-danger">This field is invalid</p>
        </div>

         <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">Company Facebook</label>
            <div class="control">
                <input :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.facebookSocialMedia.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder=""
                       v-model="form.facebookSocialMedia">
            </div>
            <p v-if="$v.form.facebookSocialMedia.$error" class="help is-danger">This field is invalid</p>
        </div>

        <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">Company LinkedIn</label>
            <div class="control">
                <input :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.linkedInSocialMedia.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder=""
                       v-model="form.linkedInSocialMedia">
            </div>
            <p v-if="$v.form.linkedInSocialMedia.$error" class="help is-danger">This field is invalid</p>
        </div>

         <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">Contact Email</label>
            <div class="control">
                <input :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.email.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder=""
                       v-model="form.email">
            </div>
            <p v-if="$v.form.email.$error" class="help is-danger">This Email is invalid</p>
        </div>

        <!-- Logo -->

        <component-apply-form-second-step :text_placeholder="logo_text_placeholder" @imageFile="METHOD_replaceImageFile"/>

        <vue-recaptcha
          ref="recaptcha"
          @verify="onCaptchaVerified"
          @expired="onCaptchaExpired"
          size="invisible"
          sitekey="6LfeSowUAAAAAKOf0EEmNfrFpaMSm_T8p-tlLn34">
        </vue-recaptcha>

        <transition name="fade">

            <div v-if="!loading">

              <div v-on:click="initializeTransfer" data-v-3ee86246="" class="bottom only-next">
                <div data-v-3ee86246="" class="next-main-div-button stepper-button next deactivated">
                  <span data-v-3ee86246="">Post</span>
                </div>
              </div>

            </div>

            <div v-else>
              <circle-loader class="spinner-class" loading=true color="black" size="135" sizeUnit="px"/>
            </div>

          </transition>

    </div>
  </div>

</template>

<style lang="scss">
  @import './ComponentApplyFormFirstStep.css';
</style>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<script type="text/javascript">
import { store } from '../../../../store/store'
import VueSwal from 'vue-swal'
import {validationMixin} from 'vuelidate'
import Multiselect from 'vue-multiselect'
import {required, email} from 'vuelidate/lib/validators'
import Vuelidate from 'vuelidate'
import ComponentApplyFormSecondStep from '../ComponentApplyFormSecondStep/ComponentApplyFormSecondStep.vue'
import dropdown from 'vue-dropdowns'
import Places from 'vue-places'
import VueRecaptcha from 'vue-recaptcha'

export default {
  name: 'ComponentApplyFormFirstStep',
  mixins: [validationMixin],
  props: {
    clickedNext: '',
    currentStep: ''
  },
  validations: {

    form: {
      companyName: {
        required
      },
      jobTitle: {
        required
      },
      type: {
        required
      },
      category: {
        required
      },
      location: {
        required
      },
      remote: {
        required
      },
      description: {
        required
      },
      skills: {
        required
      },
      twitterSocialMedia: {
        required
      },
      facebookSocialMedia: {
        required
      },
      linkedInSocialMedia: {
        required
      },
      salary: {
        required
      },
      email: {
        required,
        email
      }
    }
  },
  data () {
    return {
      arrayOfSkills: ['web3.js', 'Photoshop'],
      arrayOfLocations: ['Sweden', 'London'],
      arrayOfTypes: ['Contract', 'Full-time'],
      arrayOfCategories: ['developer', 'artist'],
      logo_text_placeholder: 'Upload the logo',
      windowWidth: window.innerWidth,
      form: {
        imageData: '',
        companyName: '',
        jobTitle: '',
        type: '',
        category: '',
        location: {
          label: null,
          data: {}
        },
        salary: '',
        remote: '',
        description: '',
        skills: [],
        twitterSocialMedia: '',
        facebookSocialMedia: '',
        linkedInSocialMedia: '',
        email: '',
        message: '',
        loading: false
      }
    }
  },
  computed: {
    COMPUTED_form_firstName () {
      return this.form.firstName
    },
    COMPUTED_form_lastName () {
      return this.form.lastName
    },
    COMPUTED_form_expectedSalary () {
      return this.form.expectedSalary
    },
    COMPUTED_form_twitterSocialMedia () {
      return this.form.twitterSocialMedia
    },
    COMPUTED_form_facebookSocialMedia () {
      return this.form.facebookSocialMedia
    },
    COMPUTED_form_linkedInSocialMedia () {
      return this.form.linkedInSocialMedia
    },
    COMPUTED_form_email () {
      return this.form.email
    },
    COMPUTED_form_message () {
      return this.form.message
    }
  },
  components: {
    Places,
    Multiselect,
    VueSwal,
    Vuelidate,
    'dropdown': dropdown,
    ComponentApplyFormSecondStep,
    VueRecaptcha
  },
  methods: {
    methodToRunOnSelect (payload) {
      this.object = payload
    },
    METHOD_replaceImageFile (content) {
      if (content.value.length > 0) {
        this.logo_text_placeholder = 'Change the logo'
      } else {
        this.logo_text_placeholder = 'Upload the logo'
      }
      this.form.imageData = content.value
    },
    initializeTransfer () {
      var self = this
      this.$v.$touch()
      if (!self.$v.$invalid) {
        self.$refs.recaptcha.execute()
        self.loading = true
      }
    },
    onCaptchaVerified: function (recaptchaToken) {
      const self = this
      self.$refs.recaptcha.reset()
      var obtainedData = self.form
      obtainedData.recaptchaToken = recaptchaToken
      store.dispatch('[user/initializeTransfer]', obtainedData).then(() => {
        self.loading = false
      }).catch(error => {
        console.log(error)
      })
    },
    // reseting captcha
    onCaptchaExpired: function () {
      this.$refs.recaptcha.reset()
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
    clickedNext (val) {
      if (val === true) {
        this.$v.form.$touch()
      }
    },
    COMPUTED_form_firstName (val) {
      store.commit('MUTATE_firstName', val)
    },
    COMPUTED_form_lastName (val) {
      store.commit('MUTATE_lastName', val)
    },
    COMPUTED_form_expectedSalary (val) {
      store.commit('MUTATE_expectedSalary', val)
    },
    COMPUTED_form_twitterSocialMedia (val) {
      store.commit('MUTATE_twitterSocialMedia', val)
    },
    COMPUTED_form_facebookSocialMedia (val) {
      store.commit('MUTATE_facebookSocialMedia', val)
    },
    COMPUTED_form_linkedInSocialMedia (val) {
      store.commit('MUTATE_linkedInSocialMedia', val)
    },
    COMPUTED_form_email (val) {
      store.commit('MUTATE_email', val)
    },
    COMPUTED_form_message (val) {
      store.commit('MUTATE_message', val)
    }
  },
  mounted () {
    window.addEventListener('resize', () => {
      this.windowWidth = window.innerWidth
    })
    if (!this.$v.$invalid) {
      this.$emit('can-continue', {value: true})
    } else {
      this.$emit('can-continue', {value: false})
    }
  }
}

</script>
