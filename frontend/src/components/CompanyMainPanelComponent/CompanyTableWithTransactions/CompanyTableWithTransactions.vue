<template>

  <div>

    <template v-for="item in self_store.getters['user/GET_TRANSACTIONS']">
      item.recipient{{ item.recipient }}
    </template>

    <table class="ui celled padded table">
      <tbody>

      <transition name="fade">

        <template v-if="tableObject.loading">

          <div style="margin: auto; display: box;">
            <circle-loader class="spinner-class" loading="loading" color="black" size=135 sizeUnit="px"/>
          </div>

        </template>
        <template v-else>

          <template v-if="numberOfTransactions > 0">

            <tr>
              <th>Recipient</th>
              <th>Sender</th>
              <th>From Currency</th>
              <th>To Currency</th>
              <th>Value</th>
              <th>Exchange Rate</th>
              <th>Created At</th>
              <th>Status</th>
            </tr>
            <template v-for="item in self_store.getters['user/GET_TRANSACTIONS']">
              <tr class="ui celled padded table">
              <th>
                {{ item.recipient }}
              </th>
              <th>
                {{ item.sender }}
              </th>
              <th>
                {{ item.fromc }}
              </th>
              <th>
                {{ item.toc }}
              </th>
              <th>
                {{ item.value }}
              </th>
              <th>
                {{ item.rate }}
              </th>
              <th>
                {{ item.created_at }}
              </th>
              <th>
                {{ item.status }}
              </th>
            </tr>
            </template>
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
  @import './CompanyTableWithTransactions.css';
</style>

<script type="text/javascript">

  import {store} from '../../../store/store'
  import {CircleLoader} from '@saeris/vue-spinners'

  export default {
    name: 'CompanyTableWithTransactions',
    computed: {
      self_store() {
        return store
      },
      numberOfTransactions() {
        var number = 0;
        try {
          number = store.getters['user/GET_TRANSACTIONS'].length;
        } catch (e) {
          number = 0;
        }
        return number;
      },
       COMPUTED_transactions() {
        return store.getters['user/GET_TRANSACTIONS'];
      }
    },
    components: {
      CircleLoader
    },
    data() {
      return {
        tableObject: {
          title: 'Transactions',
          loading: true,
          emptyDataListMessage: 'You have not created any transactions yet.'
        }
      }
    },
    mounted() {
      var self = this;

      store.dispatch('user/fetchUserTransactions').then(() => {
      }).catch((e) => {
      }).finally(() => {
        self.tableObject.loading = false;
      });


      window.addEventListener('resize', () => {
        this.windowWidth = window.innerWidth;
        console.log(this.isMobile)
      })
    },

  }

</script>
