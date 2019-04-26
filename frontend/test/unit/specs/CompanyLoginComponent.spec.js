import { mount } from '@vue/test-utils'
import Vue from 'vue'
import CompanyLoginComponentfrom from '../../../src/components/CompanyLoginComponent/CompanyLoginComponent/CompanyLoginComponent'
import SuiVue from "semantic-ui-vue";
import Notifications from 'vue-notification'

Vue.use(SuiVue);
Vue.use(Notifications);


describe('CompanyLoginComponent.vue', () => {
  it('renders the correct login view', () => {
    const wrapper = mount(CompanyLoginComponentfrom);
    expect(wrapper.html()).toContain('<input type="text" placeholder="E-mail" class="input ui-input-box-div ui-input-box-div-text" style="width: 80%;">');
  });
});

