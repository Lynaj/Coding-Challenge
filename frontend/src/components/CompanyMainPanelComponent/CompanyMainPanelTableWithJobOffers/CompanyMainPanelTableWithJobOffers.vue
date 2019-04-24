<template>
  <div>
    <table class="ui celled padded table">
      <thead class="">
      <tr class="">
        <th class="single line" style="text-align: center;">{{ tableObject.title }}</th>
      </tr>
      </thead>
      <tbody>

      <transition name="fade">

        <template v-if="loading">

          <circle-loader class="spinner-class" loading="loading" color="black" size=135 sizeUnit="px"/>

        </template>

        <template v-else>

          <template v-if="">


          </template>

          <template v-else>
            <tr class="">
                <div class="formatted-wrong-item-icon"></div>
                <div style="font-size: 2em; text-align: center;padding-top: 2em;padding-bottom: 3em;">
                  {{ tableObject.emptyDataListMessage }}
                </div>
            </tr>
          </template>


        </template>

      </transition>
      </tbody>
    </table>
  </div>

</template>

<style lang="scss">
  @import './CompanyMainPanelTableWithJobOffers.css';
</style>

<script type="text/javascript">
  import {CircleLoader} from '@saeris/vue-spinners'
  import VueRouter from 'vue-router'


  import {store} from '../../../store/store'

  export default {
    name: 'CompanyMainPanelTableWithJobOffers',
    props: {
      imageUrl: ''
    },
    components: {
      CircleLoader,
      VueRouter
    },
    data() {
      return {
        tableObject: {
          title: 'Transactions',
          loading: true,
          emptyDataListMessage: 'You have not created any transactions yet.'
        },
        buttonObject: {
          title: 'Delete'
        },
        buttonShowExtraButton: {
          title: 'More'
        }
      }
    },
    computed: {
      self_store() {
        return store
      }
    },
    created() {
      this.METHOD_fetchUserDataFromTheDatabase();
      console.log('wywoalem fetchowanie user data')
    },
    methods: {
      METHOD_invokeShowMore(data) {
        // Setting up concrete job offer
        store.commit('MUTATE_currently_viewed_job_offer_owner_view', data);
        // Changing view of the current page ( mutating router
        this.$router.push({
          name: 'job_applicants_linked_to_particular_job_offer',
          params: {job_offer_title: data.job_title.trim()}
        });
      },
      METHOD_computed_mainDivId(localIndex) {
        return localIndex + 'p13p123'
      },
      METHOD_invokeDeleteFunction(data) {
        this.tableObject.loading = true
        var self = this
        store.dispatch('deleteJobOffer', data.offerId).then(() => {
          self.METHOD_fetchUserDataFromTheDatabase()
          self.tableObject.loading = false
        }).catch(error => {
          this.$swal('Soemthing went wrong!').then(() => {
            self.tableObject.loading = false;
          });
        })
      },
      METHOD_fetchUserDataFromTheDatabase: function () {
        var self = this
        self.tableObject.loading = true


        store.dispatch('fetchJobOffersLinkedToTheUser', ).then(() => {
          self.tableObject.loading = false
        }).catch(error => {
          console.log(error.response)
          self.tableObject.loading = false
        })
      }
    }
  }

</script>
+
