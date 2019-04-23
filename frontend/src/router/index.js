import Vue from 'vue'
import Router from 'vue-router'
import Company from '@/components/Company/Company/Company.vue'
import CompanyInfoBox from '@/components/CompanyInfo/CompanyInfoBox/CompanyInfoBox.vue'
import CompanyMainPanelComponent from '@/components/CompanyMainPanelComponent/CompanyMainPanelComponent/CompanyMainPanelComponent.vue'
import CompanyDetailedView from '@/components/CompanyDetailedView/CompanyDetailedView.vue'

Vue.use(Router);


let router = new Router({
  routes: [
    { 
      path: '/login', 
      name: 'login', 
      component: CompanyInfoBox,
      meta: { 
          guest: true
      } 
    },
    {
      path: '/menu',
      name: 'menu',
      component: CompanyMainPanelComponent,
      meta: { 
          requiresAuth: true
      },
      children: [{
        path: 'offers',
        name: 'offers',
        component: CompanyMainPanelComponent,
        meta: { 
            requiresAuth: true
        }
      },
      {
        path: '/applications/:job_offer_title',
        name: 'job_applicants_linked_to_particular_job_offer',
        component: CompanyMainPanelComponent,
        meta: { 
            requiresAuth: true
        }
      }, {
        path: 'create',
        name: 'jobcreator',
        component: CompanyMainPanelComponent,
        meta: {
            requiresAuth: true
        }
      }, {
        path: 'information',
        name: 'menuinformation',
        component: CompanyMainPanelComponent,
        meta: {
            requiresAuth: true
        }
      }
      ]
    },
    { 
      path: '/company/:company_name', 
      name: 'company_detailed', 
      component: CompanyDetailedView,
      meta: { 
          guest: true
      }
    },
    { 
      path: '/', 
      name: 'main', 
      component: Company,
      meta: { 
          guest: true
      }
    }
  ]
});

router.beforeEach((to, from, next) => {

    if(to.matched.some(record => record.meta.requiresAuth)) {
        if (localStorage.getItem('jwt') == null) {
            next({
                path: '/'
            })
        } else {
          next()
        }
    }else {
        next()
    }
  });

export default router
