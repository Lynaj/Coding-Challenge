<template>

    <table style="margin: auto !important;padding-top: 3em;">
      <tbody class="ui vertical labeled menu">
        <tr>
          <th>Balance</th>
          <th>Currency</th>
        </tr>
        <tr v-for="balance in self_store.getters['user/GET_BALANCES']" class="ui celled padded table">
          <th>{{ balance.value }}</th>
          <th>{{ balance.currency }}</th>
        </tr>
      </tbody>
    </table>

</template>

<style lang="scss">
  @import './CompanyMainBalanceTable.css';
</style>

<script type="text/javascript">

import { store } from '../../../store/store'

export default {
  name: 'CompanyMainBalanceTable',
  computed: {
    self_store() {
      return store
    }
  },
  mounted () {
    var self = this;

    // setInterval(function(){
    store.dispatch('user/fetchUserBalances').then(() => {
    }).catch((e) => {
    });
    // }, 1000);


    window.addEventListener('resize', () => {
      this.windowWidth = window.innerWidth;
      console.log(this.isMobile)
    })
  },

}

</script>
