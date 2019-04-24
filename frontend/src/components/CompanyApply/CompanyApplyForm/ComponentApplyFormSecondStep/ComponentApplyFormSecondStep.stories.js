import { storiesOf } from '@storybook/vue'
import { action } from '@storybook/addon-actions'
import ComponentApplyFormSecondStep from './ComponentApplyFormSecondStep'
import Vue from 'vue'
import VueSwal from 'vue-swal'
import Toasted from 'vue-toasted'

Vue.use(Toasted)
Vue.use(VueSwal)

class Item {
  constructor (id, img, job_title, description, salary, salary_currency, registered_at) {
    this.id = id
    this.img = img
    this.job_title = job_title
    this.description = description
    this.salary = salary
    this.salary_currency = salary_currency
    this.registered_at = registered_at
  }
}

storiesOf('ComponentApplyFormSecondStep', module)
  .add('Fully Working', () => {
    return {
      components: { ComponentApplyFormSecondStep },
      template: `<company-apply-form-second-step />`,
      data: () => ({ local_test_item })
    }
  })
