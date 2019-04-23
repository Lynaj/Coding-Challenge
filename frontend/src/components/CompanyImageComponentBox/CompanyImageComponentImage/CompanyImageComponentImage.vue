<template>
  <img :src="imageObject" class="ui image image-collapsed-company-version" >
</template>

<style lang="scss">
  @import './CompanyImageComponentImage.css';
</style>


<script type="text/javascript">
export default {
  name: 'CompanyImageComponentImage',
  props: {
    imageObject: ''
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
