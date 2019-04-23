
<template>

</template>

<style lang="scss">
  @import './CompanyImageComponentSmallButton.css';
</style>

<script type="text/javascript">

import { store } from '../../../store/store'

export default {
  name: 'CompanyImageComponentSmallButton',
  props: {
    testArray: {
      type: Array(),
      default: () => []
    },
    testObject: {
      type: Object,
      default: () => ({
        id: ''
      })
    }
  },
  components: {

  },

  methods: {
    Test: function () {

    }
  },
  mounted () {
    this.Test()
  }
}

</script>
