import { storiesOf } from '@storybook/vue'
import { action } from '@storybook/addon-actions'
import ComponentApplyFormSinngleScreeningQuestion from './ComponentApplyFormSinngleScreeningQuestion'
import Vue from 'vue'
import VueSwal from 'vue-swal'

Vue.use(VueSwal)

var localquestion_placeholder = 'Your age'

storiesOf('ComponentApplyFormSinngleScreeningQuestion', module)
  .add('Fully Working', () => {
    return {
      components: { ComponentApplyFormSinngleScreeningQuestion },
      template: `<component-apply-form-sinngle-screening-question :question_placeholder="localquestion_placeholder" />`,
      data: () => ({ localquestion_placeholder })
    }
  })
