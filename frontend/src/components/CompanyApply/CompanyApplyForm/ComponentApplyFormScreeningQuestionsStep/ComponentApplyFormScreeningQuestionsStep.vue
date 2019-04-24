<template>

  <div style="padding: 2rem 3rem; text-align: left;display: flex;flex-direction: column;justify-content: center;">

    <template v-for="(queriedScreeningQuestion, localIndex) in screeningQuestions">
      <component-apply-form-sinngle-screening-question :mountedQuestion="queriedScreeningQuestion" :index="localIndex" v-on:can-continue="checkEachQuestion" />
    </template>

  </div>
</template>

<style lang="scss">
  @import './ComponentApplyFormScreeningQuestionsStep.css';
</style>

<script type="text/javascript">
import { store } from '../../../../store/store'
import VueSwal from 'vue-swal'
import {validationMixin} from 'vuelidate'
import {required, email} from 'vuelidate/lib/validators'
import Vuelidate from 'vuelidate'
import ComponentApplyFormSinngleScreeningQuestion from './ComponentApplyFormSinngleScreeningQuestion/ComponentApplyFormSinngleScreeningQuestion.vue'

export default {
  name: 'ComponentApplyFormScreeningQuestionsStep',
  mixins: [validationMixin],
  data () {
    return {
      screeningQuestions: store.getters.GET_currently_viewed_job_offer.offer_screening_questions,
      windowWidth: window.innerWidth,
      screeningQuestionsAnswers: []
    }
  },
  computed: {
    self_store () {
      return store
    },
    computedscreeningQuestionsAnswers () {
      return this.screeningQuestionsAnswers
    }
  },
  methods: {
    checkEachQuestion (value) {
      if (this.screeningQuestionsAnswers.length == 0) {
        for (var i = this.screeningQuestions.length - 1; i >= 0; i--) {
          this.screeningQuestionsAnswers.push(false)
        }
      }
      this.screeningQuestionsAnswers[value.index] = value.value
      this.determineWhetherWeShouldEmit()
    },
    determineWhetherWeShouldEmit () {
      var globalHandler = true
      for (var i = this.screeningQuestions.length - 1; i >= 0; i--) {
        if (this.screeningQuestionsAnswers[i] == false) {
          globalHandler = false
          break
        }
      }
      if (globalHandler) {
        this.$emit('can-continue', {value: true})
      } else {
        this.$emit('can-continue', {value: false})
      }
    }
  },
  components: {
    VueSwal,
    Vuelidate,
    ComponentApplyFormSinngleScreeningQuestion
  },
  mounted: function () {
    // being ready for determining whether particular value is ready for change
    // for (var i = this.screeningQuestions.length - 1; i >= 0; i--) {
    //   this.screeningQuestionsAnswers[i].push(false);
    // }

    window.addEventListener('resize', () => {
      this.windowWidth = window.innerWidth
    })
  }
}

</script>
