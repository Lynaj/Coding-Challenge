import { storiesOf } from '@storybook/vue'
import { action } from '@storybook/addon-actions'
import CompanyImageComponentImage from './CompanyImageComponentImage'
import StoryRouter from 'storybook-vue-router'
import Vue from 'vue'
import { store } from '../../../store/store'


var testImageObject = 'https://semantic-ui.com/images/wireframe/square-image.png'

storiesOf('CompanyImageComponentImage', module)
  .add('Fully Working', () => ({
      components: { CompanyImageComponentImage },
      template: `<company-image-component-image :imageObject="testImageObject" />`,
      data: () => ({ testImageObject })
    }
  )
)