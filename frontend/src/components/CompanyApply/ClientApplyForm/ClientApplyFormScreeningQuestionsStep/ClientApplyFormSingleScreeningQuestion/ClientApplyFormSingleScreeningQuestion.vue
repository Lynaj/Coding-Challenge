<template>

  <div style="margin: auto;margin-top: 3em;">
      <div class="field">
          <label class="label"></label>
          <div class="control">
              <input :class="['input ui-input-box-div', ($v.question.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" :placeholder="mountedQuestion.question" v-model="question">
          </div>
          <p v-if="$v.question.$error" class="help is-danger">This question is invalid</p>
      </div>
  </div>

</template>

<style lang="scss">
  @import './ClientApplyFormSingleScreeningQuestion.css';
</style>

<script type="text/javascript">
import VueSwal from 'vue-swal'
import {validationMixin} from 'vuelidate'
import {required, email} from 'vuelidate/lib/validators'
import Vuelidate from 'vuelidate'
import { store } from '../../../../../store/store'

export default {
  name: 'ClientApplyFormSingleScreeningQuestion',
  mixins: [validationMixin],
  props: {
    mountedQuestion: {
      id: 0,
      question: ''
    },
    arrayIndex: 0,
    index: 0
  },
  validations: {
    question: {
      required
    }
  },
  data () {
    return {
      windowWidth: window.innerWidth,
      question: ''
    }
  },
  computed: {
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
    question (val) {
      if (val.length > 0) {
        store.commit('MUTATE_screeningQuestionsAnswers', {
          index: this.mountedQuestion.id,
          answer: this.question
        })

        this.$emit('can-continue', {value: true, index: this.arrayIndex})
      } else {
        this.$emit('can-continue', {value: false, index: this.arrayIndex})
      }
    },
    clickedNext (val) {
      if (val === true) {
        this.$v.form.$touch()
      }
    }
  },
  mounted () {
    window.addEventListener('resize', () => {
      this.windowWidth = window.innerWidth
    })
    if (!this.$v.$invalid) {
      this.$emit('can-continue', {value: true, index: this.index})
    } else {
      this.$emit('can-continue', {value: false, index: this.index})
    }
  }
}

</script>
