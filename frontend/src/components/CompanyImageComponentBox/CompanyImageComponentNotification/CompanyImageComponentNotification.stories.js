import { storiesOf } from '@storybook/vue'
import { action } from '@storybook/addon-actions'
import CompanyImageComponentNotification from './CompanyImageComponentNotification'

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

storiesOf('CompanyImageComponentNotification', module)
  .add('Fully Working', () => {
    return {
      components: { CompanyImageComponentNotification },
      template: `<company-image-component-notification :testObject="local_test_item"/>`,
      data: () => ({ local_test_item }),
      methods
    }
  })
