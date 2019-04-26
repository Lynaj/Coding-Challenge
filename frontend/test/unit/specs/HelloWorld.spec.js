import Vue from 'vue'
import Company from '../../../src/components/Company/Company/Company'

describe('Company.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(Company);
    const vm = new Constructor().$mount();
    expect(vm.$el.querySelector('.hello h1').textContent)
      .toEqual('Welcome to Your Vue.js App')
  })
})
