import { shallowMount } from '@vue/test-utils'
import Company from '@/components/Company/Company.vue'

describe('Company.vue', () => {
  it('toggles msg passed to Message when button is clicked', () => {
    const wrapper = shallowMount(Company)
    const button = wrapper.find('#toggle-message')
    button.trigger('click')
    const MessageComponent = wrapper.find(Message)
    expect(MessageComponent.props()).toEqual({msg: 'message'})
    button.trigger('click')
    expect(MessageComponent.props()).toEqual({msg: 'toggled message'})
  })
})