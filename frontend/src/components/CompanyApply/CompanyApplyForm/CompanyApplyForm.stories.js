import { storiesOf } from '@storybook/vue'
import { action } from '@storybook/addon-actions'
import CompanyApplyForm from './CompanyApplyForm'
import Vue from 'vue'
import VueSwal from 'vue-swal'

Vue.use(VueSwal)

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

export const local_test_item = new JobOffer(
  2,
  'EXTENDED Development Manager (Uganda/Africa)',
  'As a Systems Engineer you will be responsible for:<br>',
  4500,
  '$',
  false,
  false,
  0.0000,
  [
    {
      'id': 1,
      'question': 'jak sie nazywasz'
    },
    {
      'id': 2,
      'question': 'ile masz lat'
    }
  ],
  {
    name: 'Full Time'
  },
  [
    {
      'category': 'tech jobs'
    }
  ],
  [
    {
      'skill': 'Solidity'
    }
  ],
  {
    location: 'Barcelona'
  },
  'Featured',
  '2019-02-21T14:50:49.359570Z'
)

var screeningQuestions = []

storiesOf('CompanyApplyForm', module)
  .add('Fully Working', () => {
    return {
      components: { CompanyApplyForm },
      template: `<company-apply-form :formObject="local_test_item" :screeningQuestions="screeningQuestions"/>`,
      data: () => ({ local_test_item, screeningQuestions })
    }
  })
