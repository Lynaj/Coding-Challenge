<template>

  <div style="padding: 2rem 3rem; text-align: left;display: flex;flex-direction: column;justify-content: center;">

    <div class="apply-form-first-step-sub-div" style="float: left;display: block;margin: auto;">

         <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">First Name</label>
            <div class="control">
                <input :class="['input ui-input-box-div', ($v.form.firstName.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder=""
                       v-model="form.firstName">
            </div>
            <p v-if="$v.form.firstName.$error" class="help is-danger">Your First name is invalid</p>
        </div>

         <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">Last Name</label>
            <div class="control">
                <input :class="['input ui-input-box-div', ($v.form.lastName.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder=""
                       v-model="form.lastName">
            </div>
            <p v-if="$v.form.lastName.$error" class="help is-danger">Your Last Name is invalid</p>
        </div>

        <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">Expected Salary</label>
            <div class="control">
                <input :class="['input ui-input-box-div', ($v.form.expectedSalary.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder=""
                       v-model="form.expectedSalary">
            </div>
            <p v-if="$v.form.expectedSalary.$error" class="help is-danger">This value is invalid<br>Please remember, that each and every offer is denoted in USD</p>


          </div>

         <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">Twitter</label>
            <div class="control">
                <input :class="['input ui-input-box-div', ($v.form.twitterSocialMedia.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder=""
                       v-model="form.twitterSocialMedia">
            </div>
            <p v-if="$v.form.twitterSocialMedia.$error" class="help is-danger">This field is invalid</p>
        </div>

         <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">Facebook</label>
            <div class="control">
                <input :class="['input ui-input-box-div', ($v.form.facebookSocialMedia.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder=""
                       v-model="form.facebookSocialMedia">
            </div>
            <p v-if="$v.form.facebookSocialMedia.$error" class="help is-danger">This field is invalid</p>
        </div>

        <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">LinkedIn</label>
            <div class="control">
                <input :class="['input ui-input-box-div', ($v.form.linkedInSocialMedia.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder=""
                       v-model="form.linkedInSocialMedia">
            </div>
            <p v-if="$v.form.linkedInSocialMedia.$error" class="help is-danger">This field is invalid</p>
        </div>

         <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
            <label class="label">Email</label>
            <div class="control">
                <input :class="['input ui-input-box-div', ($v.form.email.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder=""
                       v-model="form.email">
            </div>
            <p v-if="$v.form.email.$error" class="help is-danger">This Email is invalid</p>
        </div>

    </div>
  </div>

</template>

<style lang="scss">
  @import './ClientApplyFormFirstStep.css';
</style>

<script type="text/javascript">
import { store } from '../../../../store/store'
import VueSwal from 'vue-swal'
import {validationMixin} from 'vuelidate'
import {required, email, minLength, between} from 'vuelidate/lib/validators'
import Vuelidate from 'vuelidate'

export default {
  name: 'ClientApplyFormFirstStep',
  mixins: [validationMixin],
  props: {
    clickedNext: '',
    currentStep: ''
  },
  validations: {
    form: {
      firstName: {
        required
      },
      lastName: {
        required
      },
      expectedSalary: {
        required,
        between: between(0, 10000000)
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
      email: {
        required,
        email
      }
    }
  },
  data () {
    return {
      windowWidth: window.innerWidth,
      form: {
        firstName: '',
        lastName: '',
        expectedSalary: '',
        twitterSocialMedia: '',
        facebookSocialMedia: '',
        linkedInSocialMedia: '',
        email: '',
        message: ''
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
    VueSwal,
    Vuelidate
  },
  methods: {
    METHOD_init_creation_of_an_offer () {
      this.$swal('Hello word!')
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
