import axios from 'axios'
import MockAdapter from 'axios-mock-adapter'
import { action } from '@storybook/addon-actions'
import { storiesOf } from '@storybook/vue'
import Vue from 'vue'
import Vuex from 'vuex'
import CompanyMainPanelTableWithJobOffers from './CompanyMainPanelTableWithJobOffers.vue'
import SuiVue from 'semantic-ui-vue'

Vue.use(Vuex)
Vue.use(Vuex)
Vue.use(SuiVue)

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

class JobOffer {
  constructor (company_id, image, offerId, job_title, description, salary, salary_currency, remote, equity, equity_percentage, offer_screening_questions, offer_type, offer_category, offer_skill, offer_location, offer_type_controller, registered_at, company_name) {
    this.company_id = company_id
    this.image = image
    this.offerId = offerId
    this.job_title = job_title
    this.description = description
    this.salary = salary
    this.salary_currency = salary_currency
    this.remote = remote
    this.equity = equity
    this.equity_percentage = equity_percentage
    this.offer_screening_questions = offer_screening_questions
    this.offer_type = offer_type
    this.offer_category = offer_category
    this.offer_skill = offer_skill
    this.offer_location = offer_location
    this.offer_type_controller = offer_type_controller
    this.registered_at = registered_at
    this.company_name = company_name
  }
}

export const local_test_item = new Item(
  '0',
  'https://semantic-ui.com/images/wireframe/square-image.png',
  '1',
  'Managing Director',
  'Lorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsum',
  3500,
  '$',
  false,
  false,
  0,
  [],
  {},
  [],
  [],
  [],
  'Featured',
  '2018-02-01',
  'BizShake',
  'BizShake'
)

storiesOf('CompanyMainPanelTableWithJobOffers', module)
  .add('Fully Working', () => {
    return {
      components: { CompanyMainPanelTableWithJobOffers },
      template: '<company-main-panel-table-with-job-offers  />',
      data: () => ({ local_test_item })
    }
  })
