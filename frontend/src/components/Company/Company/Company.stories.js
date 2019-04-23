import { storiesOf } from '@storybook/vue'
import { action } from '@storybook/addon-actions'
import Company from './Company'
import VueFuse from 'vue-fuse'
import StoryRouter from 'storybook-vue-router'
import Vue from 'vue'
import { store } from '../../../store/store'
import iconNoExist from '../../../assets/icons/not-found.svg'
import CompanyInfoBox from '../../CompanyInfo/CompanyInfoBox/CompanyInfoBox.vue'
import CompanyMainPanelComponent from '../../CompanyMainPanelComponent/CompanyMainPanelComponent/CompanyMainPanelComponent.vue'
import CompanyMainPanelNewJobComponent from '../../CompanyMainPanelComponent/CompanyMainPanelNewJobComponent/CompanyMainPanelNewJobComponent.vue'

Vue.use(VueFuse)

class AccorditionItemFieldName {
  constructor (field, name) {
    this.field = field
    this.name = name
  }
}

export const methods = {
  onItemClick: action('onItemClick')
}

var filteredList = [
  {
    job_title: 'Business Development Manager (Uganda/Africa)',
    description: 'Lorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsum',
    salary: 0,
    salary_currency: 'US Dollars',
    remote: true,
    equity: false,
    equity_percentage: '0.0000',
    offer_screening_questions: [],
    offer_type: {
      name: 'Full Time'
    },
    offer_category: [
      {
        category: 'tech jobs'
      }
    ],
    offer_skill: [
      {
        skill: 'Solidity'
      }
    ],
    offer_location: {
      location: 'Barcelona'
    },
    registered_at: '2019-02-01',
    offer_type_controller: 'Featured'
  },
  {
    job_title: 'V1 Business Development Manager (Uganda/Africa)',
    description: 'Lorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsum',
    salary: 0,
    salary_currency: 'US Dollars',
    remote: true,
    equity: false,
    equity_percentage: '0.0000',
    offer_screening_questions: [],
    offer_type: {
      name: 'Part Time'
    },
    offer_category: [
      {
        category: 'tech jobs'
      }
    ],
    offer_skill: [
      {
        skill: 'Solidity'
      }
    ],
    offer_location: {
      location: 'Barcelona'
    },
    registered_at: '2019-02-01',
    offer_type_controller: 'Featured'
  },
  {
    job_title: 'V2 (Uganda/Africa)',
    description: 'Lorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsum',
    salary: 0,
    salary_currency: 'US Dollars',
    remote: true,
    equity: false,
    equity_percentage: '0.0000',
    offer_screening_questions: [],
    offer_type: {
      name: 'Intern'
    },
    offer_category: [
      {
        category: 'tech jobs'
      }
    ],
    offer_skill: [
      {
        skill: 'Solidity'
      }
    ],
    offer_location: {
      location: 'Barcelona'
    },
    registered_at: '2019-02-01',
    offer_type_controller: 'Featured'
  }
]

store.commit('MUTATE_JOBS_LIST', filteredList)
store.commit('MUTATE_NOT_FOUND_ICON', iconNoExist)

storiesOf('Company', module)
  .addDecorator(StoryRouter({}, {
    routes: [
      { path: '/', component: Company },
      { path: '/login', component: CompanyInfoBox },
      { path: '/new', component: CompanyMainPanelNewJobComponent },
      {
        path: '/menu',
        component: CompanyMainPanelComponent,
        children: [{
          path: '/offers',
          component: CompanyMainPanelComponent
        },
        {
          path: '/applications',
          components: CompanyMainPanelComponent
        }
        ]
      }
    ]}))
  .add('local', () => ({
    components: { },
    template: `
      <transition name="slide">
        <div>
          <router-view/>
        </div>
      </transition>`
  }))
