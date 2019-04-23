import axios from 'axios'
import MockAdapter from 'axios-mock-adapter'
import { action } from '@storybook/addon-actions'
import { storiesOf } from '@storybook/vue'
import Vue from 'vue'
import Vuex from 'vuex'
import { store } from '../../../store/store'
import CompanyMainMenuBoxComponent from './CompanyMainMenuBoxComponent.vue'
import SuiVue from 'semantic-ui-vue'

Vue.use(Vuex)
Vue.use(Vuex)
Vue.use(SuiVue)
Vue.use(Router)

var menuItems = [
  {
    'id': 0,
    'class': 'gamepad icon',
    'title': 'My Job Offers',
    'path': store.getters.GET_LINKS_OBJECT.job_offers
  },
  {
    'id': 1,
    'class': 'video camera icon',
    'title': 'Applications',
    'path': store.getters.GET_LINKS_OBJECT.job_applications
  }
]

var methods = {
  onTestAction: action('onTestAction')
}

export default new Router({
  routes: [
    { path: '/login', name: 'login', component: CompanyInfoBox },
    { path: '/new', name: 'new', component: CompanyMainPanelNewJobComponent },
    {
      path: '/menu',
      name: 'menu',
      component: CompanyMainPanelComponent,
      children: [{
        path: '/offers',
        name: 'offers',
        component: CompanyMainPanelComponent
      },
      {
        path: '/applications',
        name: 'applications',
        components: CompanyMainPanelComponent
      }
      ]
    },
    { path: '/company/:company_name', name: 'company_detailed', component: CompanyDetailedView },
    { path: '/', name: 'main', component: Company }
  ]
})

storiesOf('CompanyMainMenuBoxComponent', module)
  .add('Fully Working', () => {
    return {
      components: { CompanyMainMenuBoxComponent },
      template: '<company-main-menu-box-component @changedMenuItem="onTestAction" :menuItems="menuItems" />',
      data: () => ({
  	    menuItems }),
    		methods
    }
  }
  )
