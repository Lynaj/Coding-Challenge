import { storiesOf } from '@storybook/vue'
import { action } from '@storybook/addon-actions'
import ComponentApplyFormFirstStep from './ComponentApplyFormFirstStep'
import Vue from 'vue'
import VueSwal from 'vue-swal'

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

export const local_test_item = new Item(
  '0',
  'https://semantic-ui.com/images/wireframe/square-image.png',
  'Managing Director',
  'Lorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsum',
  3500,
  '$',
  '2018-02-01'
)

storiesOf('ComponentApplyFormFirstStep', module)
  .add('Fully Working', () => {
    return {
      components: { ComponentApplyFormFirstStep },
      template: `<company-apply-form-first-step :tableObject="local_test_item" />`,
      data: () => ({ local_test_item })
    }
  })
