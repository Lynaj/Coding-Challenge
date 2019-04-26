import { mount } from '@vue/test-utils'
import Vue from 'vue'
import CompanyMainPanelComponent from '../../../src/components/CompanyMainPanelComponent/CompanyMainPanelComponent/CompanyMainPanelComponent'
import SuiVue from "semantic-ui-vue";
import Notifications from 'vue-notification'

Vue.use(SuiVue);
Vue.use(Notifications);


describe('CompanyMainPanelComponent.vue', () => {
  it('contains basic div class', () => {
    const wrapper = mount(CompanyMainPanelComponent);
    expect(wrapper.html()).toContain('ui vertical segments');
  });
});

