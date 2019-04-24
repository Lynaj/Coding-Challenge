import { storiesOf } from '@storybook/vue'
import { action } from '@storybook/addon-actions'
import ClientApplyFormSingleScreeningQuestion from './ClientApplyFormSingleScreeningQuestion'
import Vue from 'vue'
import VueSwal from 'vue-swal'

Vue.use(VueSwal)

var localquestion_placeholder = 'Your age'

storiesOf('ClientApplyFormSingleScreeningQuestion', module)
  .add('Fully Working', () => {
    return {
      components: { ClientApplyFormSingleScreeningQuestion },
      template: `<client-apply-form-single-screening-question :question_placeholder="localquestion_placeholder" />`,
      data: () => ({ localquestion_placeholder })
    }
  })
