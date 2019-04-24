import { storiesOf } from '@storybook/vue'
import { action } from '@storybook/addon-actions'
import CompanyInfoBox from './CompanyInfoBox'

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

storiesOf('CompanyInfoBox', module)
  .add('Fully Working', () => {
    return {
      components: { CompanyInfoBox },
      template: `<company-info-box :testObject="local_test_item"/>`,
      data: () => ({ local_test_item }),
      methods
    }
  })
