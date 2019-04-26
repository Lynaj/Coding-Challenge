import { mount } from '@vue/test-utils'
import Vue from 'vue'
import CompanyApply from '../../../src/components/CompanyApply/CompanyApplyForm/CompanyApplyForm'
import SuiVue from "semantic-ui-vue";
import Notifications from 'vue-notification'

Vue.use(SuiVue);
Vue.use(Notifications);


describe('CompanyApplyForm.vue', () => {

  it('renders the correct version of view', () => {
  const wrapper = mount(CompanyApply);
    expect(wrapper.html()).toContain('From Currency');
    expect(wrapper.html()).toContain('Recipient');
    expect(wrapper.html()).toContain('To Currency');
    expect(wrapper.html()).toContain('Transaction Value');
    expect(wrapper.html()).toContain('Transfer');
  });

  it('contains proper number of recipients', () => {
    const wrapper = mount(CompanyApplyForm({
      arrayOfRecipients: ["John"]
    }));
    expect(wrapper.html()).toContain('<span>John</span>');
  })

  it('contains proper number of currencies', () => {
    const wrapper = mount(CompanyApplyForm({
      arrayOfCurrencies: ["USD"]
    }));
    expect(wrapper.html()).toContain('<span>USD</span>');
  })

});

