import { storiesOf } from '@storybook/vue'
import { action } from '@storybook/addon-actions'
import CompanyImageComponentLeadingButton from './CompanyImageComponentLeadingButton'

class Item {
  constructor (id, img, title) {
    this.id = id
    this.title = title
  }
}

export const local_test_item = [
  new Item(
    '0',
    'Managing Director'
  )
]

export const methods = {
  onItemClick: action('onItemClick')
}

storiesOf('CompanyImageComponentLeadingButton', module)
  .add('Fully Working', () => {
    return {
      components: { CompanyImageComponentLeadingButton },
      template: `<company-image-component-leading-button :testObject="local_test_item"/>`,
      data: () => ({ local_test_item }),
      methods
    }
  })
