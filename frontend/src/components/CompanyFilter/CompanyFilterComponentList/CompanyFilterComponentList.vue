<template>
  <div>
    <div class="ui category search" style="margin-top: 2em">
      <div class="ui icon input" style="width: 100%;">

        <sui-input v-model.lazy="searchInput" style="width: 100%;" placeholder="Search job titles..." />

        <i class="search icon"></i>
      </div>
      <div class="results"></div>
    </div>

    <br>

    <div class="ui checked checkbox" style="justify-content: center;display: grid;margin-bottom: 3em;margin-top: 3em;">
      <input v-model="remoteJobs" checked="" type="checkbox">
      <label>Show only remote jobs</label>
    </div>

    <div data-v-115c3d82="">

      <div class="ui styled accordion ui vertical menu" exclusive="" styled="">

        <template v-for="(accordionItem, accordionItemIndex) in accordionItemsArray">

          <company-filter-component-box v-on:chosen-parameters="METHOD_filter_particular_parameters_beta_workig" :accordionItem="accordionItem" :innerIndex="accordionItemIndex" />

        </template>

      </div>

    </div>

  </div>
</template>

<script type="text/javascript">
import VueDataLoading from 'vue-data-loading'
import CompanyFilterComponentBox from '../CompanyFilterComponentBox/CompanyFilterComponentBox.vue'

import { store } from '../../../store/store'

var VueScrollTo = require('vue-scrollto')

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

export default {
  name: 'CompanyFilterComponentList',
  data () {
    return {
      searchInput: '',
      searchInputData: [],
      listContainingFilterParameters: {
        parent_id: [],
        class_id: []
      },
      remoteJobs: true,
      accordionItemsArray: [
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
        ),
        new AccordionItem(
          '1',
          'Categories',
          [
            new AccordionItemField('tech jobs'),
            new AccordionItemField('design jobs'),
            new AccordionItemField('business development jobs'),
            new AccordionItemField('sales jobs'),
            new AccordionItemField('marketing jobs'),
            new AccordionItemField('operations jobs'),
            new AccordionItemField('customer support jobs'),
            new AccordionItemField('analyst jobs'),
            new AccordionItemField('other jobs')
          ],
          new AccorditionItemFieldName(
            'offer_category',
            'category'
          )
        ),
        new AccordionItem(
          '2',
          'Locations',
          [
            new AccordionItemField('Austin'),
            new AccordionItemField('Bangalore'),
            new AccordionItemField('Barcelona'),
            new AccordionItemField('Berlin'),
            new AccordionItemField('Boston'),
            new AccordionItemField('Buenos Aires'),
            new AccordionItemField('Cyberjaya'),
            new AccordionItemField('Hong Kong'),
            new AccordionItemField('Hyderabad'),
            new AccordionItemField('Krakow'),
            new AccordionItemField('London'),
            new AccordionItemField('Los Angeles'),
            new AccordionItemField('Melbourne'),
            new AccordionItemField('Mountain View'),
            new AccordionItemField('New York'),
            new AccordionItemField('Oslo'),
            new AccordionItemField('Palo Alto'),
            new AccordionItemField('Pune'),
            new AccordionItemField('San Francisco'),
            new AccordionItemField('Singapore'),
            new AccordionItemField('Stockholm'),
            new AccordionItemField('Tallinn'),
            new AccordionItemField('Toronto'),
            new AccordionItemField('Vienna')
          ],
          new AccorditionItemFieldName(
            'offer_location',
            'location'
          )
        ),
        new AccordionItem(
          '3',
          'Skills',
          [
            new AccordionItemField("Smart contract"),
            new AccordionItemField("Solidity"),
            new AccordionItemField("Photoshop"),
            new AccordionItemField("Trading"),
            new AccordionItemField("Web3")
          ],
          new AccorditionItemFieldName(
            'offer_skill',
            'skill'
          )
        )
      ]
    }
  },
  props: {
  },
  components: {
    VueScrollTo,
    VueDataLoading,
    CompanyFilterComponentBox
  },
  methods: {
    METHOD_filter_particular_parameters_beta_workig (listOfParameters, index) {
      store.commit('MUTATE_CURRENTLY_VIEWED_JOB_OFFER', {});
      this.listContainingFilterParameters.parent_id[index] = listOfParameters;
      this.FILTER_jobs_list()
    },
    METHOD_search_placeholder (description) {
      return ('Search ' + description)
    },
    METHOD_class_id (index) {
      return this.listContainingFilterParameters.class_id[index]
    },
    METHOD_input_id (index, title) {
      return (title + index)
    },
    FILTER_jobs_list () {
      VueScrollTo.scrollTo('#top', 500);

      store.commit('MUTATE_isLoading_FILTERED_jobs_list', true);

      // Building up the filters
      var filter_array = [];

      // filtering input box
      if (this.searchInput.length > 0) {
        filter_array.push(
          {
            parameter: 'title',
            value: this.searchInput
          }
        )
      }

      /*
        Iterating through every single filter
        that has been inserted in the filter's array
      */
      var self = this;
      // console.log('this.accordionItemsArray: ' + JSON.stringify(this.accordionItemsArray));
      for (var filter_object in this.accordionItemsArray) {
        // console.log('filter_object' + JSON.stringify(this.accordionItemsArray[filter_object]));
        if(self.listContainingFilterParameters.parent_id[this.accordionItemsArray[filter_object].id] !== undefined
        && self.listContainingFilterParameters.parent_id[this.accordionItemsArray[filter_object].id].length > 0){
          filter_array.push(
            {
              parameter: this.accordionItemsArray[filter_object].description.toLowerCase(),
              value: self.listContainingFilterParameters.parent_id[this.accordionItemsArray[filter_object].id]
            }
          )
        }
      }





      /*
       Deleting old job offers
       We have to use true as a second parameter
       otherwise it will just concatenate
       old & new arraya
      */
      store.commit('MUTATE_JOBS_LIST', {
        localJobs_list: [],
        SHOULD_CREATE_A_NEW_PAGE: true}
      );

      /*
      Propagating filter array
      to make sure, that it will be used
      in the process of building the URL
      */

    }
  },
  computed: {
    self_store () {
      return store
    }
  },
  watch: {
    searchInput: function () {
      this.FILTER_jobs_list()
    },
    listContainingFilterParameters: function () {
      this.FILTER_jobs_list()
    },
    remoteJobs: function () {
      this.FILTER_jobs_list()
    }
  },
  created () {
    for (var i = this.accordionItemsArray.length - 1; i >= 0; i--) {
      this.listContainingFilterParameters.parent_id.push([]);
      this.listContainingFilterParameters.class_id.push(['content active'])
    }
  }
}

</script>
