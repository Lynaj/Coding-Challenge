<template>

    <table class="ui celled padded table" style="width: 100%;border: 1px solid;box-shadow: 2px azure !important;">

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
      <tr v-for="item in self_store.getters['user/GET_TRANSACTIONS']" class="ui celled padded table">
          <th>{{ item.recipient }}</th>
          <th>{{ item.sender }}</th>
          <th>{{ item.fromc }}</th>
          <th>{{ item.toc }}</th>
          <th>{{ item.value }}</th>
          <th>{{ item.rate }}</th>
          <th>{{ item.created_at }}</th>
          <th>{{ item.status }}</th>
      </tr>

  </table>


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
