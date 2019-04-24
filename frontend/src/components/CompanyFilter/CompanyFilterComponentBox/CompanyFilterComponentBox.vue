
<template>
  <div class="Expander">
    <div class="Expander__trigger"
      @click="open=!open"
      :class="open?'active':'beforeBorder'">
        <div :class="COMPUTED_title_header_class">
          <i class="dropdown icon"></i> {{ accordionItem.description }}
        </div>
    </div>

    <transition :name="animation">
        <div class="Expander__body" v-show="open">
            <slot>

               <sui-input style="justify-content: center;display: grid;" v-model.lazy="searchInputData" :placeholder="METHOD_search_placeholder(accordionItem.description)" />

                <div class="content active" >
                  <form class="ui form">

                      <div class="field" v-for="(accordionItemField, accorditionIndex) in filteredListOfAccordionItems">
                        <div class="ui checkbox">

                          <input v-on:change="METHOD_choose_parameters" v-model="listContainingFilterParameters" :id="METHOD_input_id(accorditionIndex, accordionItemField.content)" :value="accordionItemField.content" type="checkbox">
                          <label>{{ accordionItemField.content }}</label>
                        </div>

                      </div>

                  </form>
                </div>

          </slot>
        </div>

    </transition>
  </div>
</template>

<style lang="scss">
  @import './CompanyFilterComponentBox.css';
</style>

<script type="text/javascript">
import { store } from '../../../store/store'
export default {
  name: 'CompanyFilterComponentBox',
  methods: {
    METHOD_search_placeholder (description) {
      return ('Search ' + description)
    },
    METHOD_choose_parameters () {
      this.$emit('chosen-parameters', this.listContainingFilterParameters, this.innerIndex)
    },
    METHOD_input_id (index, title) {
      return (title + index)
    }
  },
  computed: {
    COMPUTED_title_header_class () {
      if (this.open == true) {
        return 'title header active'
      } else {
        return 'title header'
      }
    }
  },
  props: {
    innerIndex: 0,
    filteredListOfAccordionItems: [],
    accordionItem: {
      type: Object,
      default: () => ({
        description: '',
        accordionItems: []
      })
    },
    animation: {
      type: String,
      default: 'rightToLeft'
    }
  },
  data () {
    return {
      open: false,
      listContainingFilterParameters: [],
      searchInputData: ''
    }
  },
  created () {
    this.filteredListOfAccordionItems = this.accordionItem.accordionItems
  },
  watch: {
    searchInputData: function () {
      if (this.searchInputData.length > 0) {
        this.filteredListOfAccordionItems = this.accordionItem.accordionItems.filter(
          item => {
            return (item.content.toLowerCase().includes(this.searchInputData.toLowerCase()))
          }
        )
      } else {
        this.filteredListOfAccordionItems = this.accordionItem.accordionItems
      }
    }
  }
}

</script>
