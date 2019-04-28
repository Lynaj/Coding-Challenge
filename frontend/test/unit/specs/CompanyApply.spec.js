import {mount} from '@vue/test-utils'
import Vue from 'vue'
import CompanyApply from '../../../src/components/CompanyApply/CompanyApplyForm/CompanyApplyForm'
import SuiVue from "semantic-ui-vue";

Vue.use(SuiVue);


describe('CompanyApplyForm.vue', () => {

  it('renders the correct version of view', () => {
    const wrapper = mount(CompanyApply);
    expect(wrapper.html()).toContain('From Currency');
    expect(wrapper.html()).toContain('Recipient');
    expect(wrapper.html()).toContain('To Currency');
    expect(wrapper.html()).toContain('Transaction Value');
    expect(wrapper.html()).toContain('Transfer');
  });

  it('creation of a transaction without necessary data', () => {
    const wrapper = mount(CompanyApply);

    const button = wrapper.find('#transferspan');
    button.trigger('click');

  });
  //
  it('contains proper number of currencies', () => {
    const wrapper = mount(CompanyApply), testCurrency = "USD", testEmailAddress = "johny@test.tt",
      testTransactionValue = 123;
    // Setting up proper array objects
    wrapper.setData({arrayOfCurrencies: [testCurrency], arrayOfRecipients: [testEmailAddress]})
    // Filling form data
    wrapper.setData({
        form: {
          recipient: testEmailAddress,
          fromCurrency: testCurrency,
          toCurrency: testCurrency,
          value: testTransactionValue,
          loading: false
        }
      }
    )
    wrapper.setData({arrayOfCurrencies: ["USD"], arrayOfRecipients: ['john@aw.da']})

    expect(wrapper.html()).toContain('<span>' + testCurrency + '</span>');

    const button = wrapper.find('#transferspan');
    button.trigger('click');


  })

});

