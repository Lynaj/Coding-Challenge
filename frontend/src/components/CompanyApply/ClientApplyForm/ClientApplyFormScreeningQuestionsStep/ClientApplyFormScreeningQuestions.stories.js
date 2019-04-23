import { storiesOf } from '@storybook/vue'
import { action } from '@storybook/addon-actions'
import ClientApplyFormScreeningQuestions from './ClientApplyFormScreeningQuestions'
import Vue from 'vue'
import VueSwal from 'vue-swal'
import { store } from '../../../../store/store'

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

var local_job = {
  'id': 2,
  'job_title': 'EXTENDED Development Manager (Uganda/Africa)',
  'description': 'As a Systems Engineer you will be responsible for:<br>' +
    'Designing and developing mission critical automation applications using different languages such as Python and Go, and event driven platforms such as Stackstorm<br>' +
    'Work with other Developers, Service Owners and Architects to ensure accurate requirement gathering and timely delivery of a high quality overall solution that meets business requirements<br>' +
    'Be adaptive. Be productive quickly in a new environment that is fast paced. Learn new processes and multiple technologies. “Roll up your sleeves” and do what needs to be done<br>' +
    'Produce clear and concise feedback to product engineering teams on API and SDK gaps or desired enhancements<br>' +
    'Produce documentation and provide handson training for product engineers on using the automation applications you’ve developed<br>' +
    'About The Team<br>' +
    'The IT DevOps team is responsible for developing critical automation applications and is also responsible for making Akamai IT the best customer of Akamai. We work closely with our Premium Support team and business units to be the true Customer 1 for all appropriate Akamai products and services. We are transforming IT at Akamai and turning the enterprise inside out!<br>' +
    'Qualifications<br>' +
    'Required Education and Experience<br>' +
    'Applicants must meet one of the following education and experience requirements:<br>' +
    'A Bachelor’s degree or equivalent experience<br>' +
    'Required Skills<br>' +
    'Experience with common languages such as Python and Go<br>' +
    'Experience with programming of Web based applications with backend databases<br>' +
    'Experience with REST based APIs<br>' +
    'Experience with Linux container technology such as Docker and Kubernetes<br>' +
    'Desired Skills<br>' +
    'Strong written and verbal communication<br>' +
    'Project experience in IT industry through internship<br>' +
    'Strong analytical and problem solving skills<br>',
  'salary': 4500,
  'salary_currency': '$',
  'remote': false,
  'equity': false,
  'equity_percentage': '0.0000',
  'offer_screening_questions': [
    {
      'id': 1,
      'question': 'jak sie nazywasz'
    },
    {
      'id': 2,
      'question': 'ile masz lat'
    }
  ],
  'offer_type': {
    'name': 'Full Time'
  },
  'offer_category': [
    {
      'category': 'tech jobs'
    }
  ],
  'offer_skill': [
    {
      'skill': 'Solidity'
    }
  ],
  'offer_location': {
    'location': 'Barcelona'
  },
  'offer_type_controller': 'Featured',
  'registered_at': '2019-02-21T14:50:49.359570Z'
}

storiesOf('ClientApplyFormScreeningQuestions', module)
  .add('Fully Working', () => {
    return {
      components: { ClientApplyFormScreeningQuestions },
      template: `<client-apply-form-screening-questions />`,
      data: () => ({ })
    }
  }
  )
