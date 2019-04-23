<template>

  <div>

    <transition name="fadeslower">
      <div v-if="COMPUTED_displaySuccess && COMPUTED_allowToDisplayMessage">

        <div>
          Your application has ben successfuly sent!
        </div>

      </div>
    </transition>

    <transition name="fadeslower">
      <div v-if="COMPUTED_displayWarning && COMPUTED_allowToDisplayMessage">

        <div
          style="margin-top: 2em !important; display: flex !important;justify-content: center;font-size: 3em;line-height: 2em;background: rgba(255,98,41,1);background: -moz-linear-gradient(left, rgba(255,98,41,1) 0%, rgba(246,126,85,0.98) 20%, rgba(255,63,5,0.93) 60%, rgba(255,98,41,0.91) 78%, rgba(248,71,18,0.9) 89%, rgba(242,72,27,0.89) 96%, rgba(238,73,32,0.89) 100%);background: -webkit-gradient(left top, right top, color-stop(0%, rgba(255,98,41,1)), color-stop(20%, rgba(246,126,85,0.98)), color-stop(60%, rgba(255,63,5,0.93)), color-stop(78%, rgba(255,98,41,0.91)), color-stop(89%, rgba(248,71,18,0.9)), color-stop(96%, rgba(242,72,27,0.89)), color-stop(100%, rgba(238,73,32,0.89)));background: -webkit-linear-gradient(left, rgba(255,98,41,1) 0%, rgba(246,126,85,0.98) 20%, rgba(255,63,5,0.93) 60%, rgba(255,98,41,0.91) 78%, rgba(248,71,18,0.9) 89%, rgba(242,72,27,0.89) 96%, rgba(238,73,32,0.89) 100%);background: -o-linear-gradient(left, rgba(255,98,41,1) 0%, rgba(246,126,85,0.98) 20%, rgba(255,63,5,0.93) 60%, rgba(255,98,41,0.91) 78%, rgba(248,71,18,0.9) 89%, rgba(242,72,27,0.89) 96%, rgba(238,73,32,0.89) 100%);background: -ms-linear-gradient(left, rgba(255,98,41,1) 0%, rgba(246,126,85,0.98) 20%, rgba(255,63,5,0.93) 60%, rgba(255,98,41,0.91) 78%, rgba(248,71,18,0.9) 89%, rgba(242,72,27,0.89) 96%, rgba(238,73,32,0.89) 100%);background: #ffe1e1;filter: progid: DXImageTransform.Microsoft.gradient( startColorstr='#ff6229', endColorstr='#ee4920', GradientType=1 );max-width: 22em;border-radius: 10px 10px 10px 10px;-moz-border-radius: 10px 10px 10px 10px;-webkit-border-radius: 10px 10px 10px 10px;display: flex;flex-direction: column;border-radius: 10px 10px 10px 10px;-moz-border-radius: 10px 10px 10px 10px;-webkit-border-radius: 10px 10px 10px 10px;-webkit-box-shadow: -35px 35px 1px 0px rgba(0,0,0,0.75);-moz-box-shadow: -35px 35px 1px 0px rgba(0,0,0,0.75);box-shadow: -8px 7px 5px 0px rgba(255, 61, 61, 0.8);margin: auto;text-shadow: -3px 1px 0px rgb(241, 137, 137);text-align: center;">
          Something went wrong! Please, try again later!
        </div>

      </div>
    </transition>

    <transition name="fade" v-on:after-leave="afterLeave">
      <section v-if="!COMPUTED_displaySuccess && !COMPUTED_displayWarning" class="section">
        <div class="container">
          <div class="columns">
            <div class="column is-8 is-offset-2">

              <div class="main-div-top-banner">


                <div class="position-div-text">
                  Position: {{ formObject.job_title }}
                </div>

                <div class="div-close-button">
                  <button v-on:click="METHOD_resetUserView" class="button-close-class">
                    Close
                  </button>
                </div>


              </div>

              <template v-if="formObject.offer_screening_questions.length == 0">
                <horizontal-stepper :steps="definedSteps" @completed-step="completeStep" @active-step="isStepActive"
                                    @stepper-finished="finalizeApplication">

                </horizontal-stepper>
              </template>

              <template v-else>
                <horizontal-stepper :steps="definedStepsWithScreeningQuestions" @completed-step="completeStep"
                                    @active-step="isStepActive" @stepper-finished="finalizeApplication">
                </horizontal-stepper>
              </template>

            </div>
          </div>
        </div>
      </section>
    </transition>

  </div>
</template>


<style lang="scss">
  @import './ClientApplyForm.css';
</style>

<script type="text/javascript">

  import {store} from '../../../store/store'
  import HorizontalStepper from 'vue-stepper'
  import ClientApplyFormFirstStep from './ClientApplyFormFirstStep/ClientApplyFormFirstStep.vue'
  import ClientApplyFormScreeningQuestions
    from './ClientApplyFormScreeningQuestionsStep/ClientApplyFormScreeningQuestions.vue'
  import ClientApplyFormSecondStep from './ClientApplyFormSecondStep/ClientApplyFormSecondStep.vue'
  import VueRouter from 'vue-router'

  export default {
    name: 'ClientApplyForm',
    components: {
      VueRouter,
      HorizontalStepper,
      ClientApplyFormFirstStep,
      ClientApplyFormScreeningQuestions,
      ClientApplyFormSecondStep
    },
    computed: {
      self_store() {
        return store
      },
      COMPUTED_currentlyViewedJobOffer_title() {
        return store.getters.GET_currently_viewed_job_offer.job_title
      },
      COMPUTED_currentlyViewedJobOffer_company() {
        return store.getters.GET_currently_viewed_job_offer.company_name
      },
      COMPUTED_displayWarning() {
        return this.displayWarning
      },
      COMPUTED_displaySuccess() {
        return this.displaySuccess
      },
      COMPUTED_allowToDisplayMessage() {
        return this.allowToDisplayMessage
      }
    },
    props: {
      formObject: {
        type: Object,
        default: () => ({
          company_id: '',
          image: '',
          offerId: '',
          job_title: '',
          description: '',
          salary: '',
          salary_currency: '',
          remote: '',
          equity: '',
          equity_percentage: '',
          offer_screening_questions: '',
          offer_type: '',
          offer_category: '',
          offer_skill: '',
          offer_location: '',
          offer_type_controller: '',
          registered_at: '',
          company_name: ''
        })
      }
    },
    data() {
      return {
        allowToDisplayMessage: false,
        definedSteps: [
          {
            icon: 'info',
            name: 'Personal Information',
            title: 'Personal Information',
            subtitle: '',
            component: ClientApplyFormFirstStep,
            completed: false

          },
          {
            icon: 'cloud_upload',
            name: 'CV',
            title: 'Upload your CV',
            subtitle: '',
            component: ClientApplyFormSecondStep,
            completed: false
          }
        ],
        definedStepsWithScreeningQuestions: [
          {
            icon: 'info',
            name: 'Personal Information',
            title: 'Personal Information',
            subtitle: '',
            component: ClientApplyFormFirstStep,
            completed: false

          },
          {
            icon: 'question_answer',
            name: 'Screening Questions',
            title: 'Screening Questions',
            subtitle: '',
            component: ClientApplyFormScreeningQuestions,
            completed: false

          },
          {
            icon: 'cloud_upload',
            name: 'CV',
            title: 'Upload your CV',
            subtitle: '',
            component: ClientApplyFormSecondStep,
            completed: false
          }
        ],
        displayWarning: false,
        displaySuccess: false
      }
    },
    methods: {
      METHOD_resetUserView: function() {
        store.commit('MUTATE_currentAction', '');
        store.commit('MUTATE_CURRENTLY_VIEWED_JOB_OFFER', {})
      },
      resetCurrentlyViewedItem: function () {
        store.commit('MUTATE_CURRENTLY_VIEWED_JOB_OFFER', {})
      },
      // Executed when @completed-step event is triggered
      afterLeave: function (el) {
        this.allowToDisplayMessage = true
      },
      completeStep(payload) {
        this.definedSteps.forEach((step) => {
          if (step.name === payload.name) {
            step.completed = true
          }
        })
      },
      // Executed when @active-step event is triggered
      isStepActive(payload) {
        this.definedSteps.forEach((step) => {
          if (step.name === payload.name) {
            if (step.completed === true) {
              step.completed = false
            }
          }
        })
      },
      // Executed when @stepper-finished event is triggered
      finalizeApplication() {
        var queriedObject = {
          id: store.getters.GET_currently_viewed_job_offer.offerId,
          answers: store.getters.GET_currently_viewed_job_offer_answers
        };

        store.dispatch('commitCurrentlyViewedUserApplication', queriedObject).then(() => {
          this.$swal('Your application has been sent!').then(() => {
            store.commit('MUTATE_currentAction', '');
            store.commit('MUTATE_CURRENTLY_VIEWED_JOB_OFFER', {})
          })
        }).catch(() => {
          this.$swal('Something went wrong!');
        })
      }
    },
    created() {
      var queriedObject = {
        id: store.getters.GET_currently_viewed_job_offer.id,
        answers: store.getters.GET_currently_viewed_job_offer_answers
      }
    }
  }

</script>
