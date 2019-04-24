
import { storiesOf } from '@storybook/vue'
import { action } from '@storybook/addon-actions'
import CompanyFilterComponentList from './CompanyFilterComponentList'
import VueFuse from 'vue-fuse'
import Vue from 'vue'
import { store } from '../../../store/store'
import VueStickto from 'vue-stickto'

Vue.use(VueStickto)
Vue.use(VueFuse)

class AccorditionItemFieldName {
  constructor (field, name) {
    this.field = field
    this.name = name
  }
}

class AccordionItemField {
  constructor (content) {
    this.content = content
  }
}

class AccordionItem {
  constructor (id, description, accordionItems, fieldDetails) {
    this.id = id
    this.description = description
    this.fieldDetails = fieldDetails
    this.accordionItems = accordionItems
  }
}

export const accordionItemsArray = [
  new AccordionItem(
    '0',
    'Types',
    [
      new AccordionItemField(
        'Full Time'
      ),
      new AccordionItemField(
        'Part Time'
      ),
      new AccordionItemField(
        'Intern'
      ),
      new AccordionItemField(
        'Contract'
      ),
      new AccordionItemField(
        'Other'
      )
    ],
    new AccorditionItemFieldName(
      'offer_type',
      'name'
    )
  )
]
export const methods = {
  onItemClick: action('onItemClick')
}

storiesOf('CompanyFilterComponentList', module)
  .add('Types Accordion Only', () => {
    return {
      components: { CompanyFilterComponentList },
      template: `<company-filter-component-list :accordionItemsArray="accordionItemsArray"/>`,
      data: () => ({ accordionItemsArray }),
      methods
    }
  }).add('Types Accordion Only Fully Filled', () => {
    return {
      components: { CompanyFilterComponentList },
      template: `<company-filter-component-list :accordionItemsArray="accordionItemsArrayFull"/>`,
      data: () => ({ accordionItemsArrayFull }),
      methods
    }
  })
