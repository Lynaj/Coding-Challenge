<template>

    <button v-on:click="METHOD_init_creation_of_an_offer" class="contact-button apply-button-table-view">Apply</button>
  
</template>




<style lang="scss">
  @import './CompanyApplyButton.css';
</style>

<script type="text/javascript">
  import { store } from '../../../store/store'
  import VueSwal from 'vue-swal'

  export default {
    name: 'CompanyApplyButton',
    props: {
      tableObject: {
        type: Object,
        default: () => ({
          image: '',
          job_title: '',
          description: ''
        })
      },
      mainDivId: ''
    },
    data() {
      return {
        windowWidth: window.innerWidth
      }
    },
    computed: {
    },
    components: {
      VueSwal
    },
    methods: {
      METHOD_init_creation_of_an_offer() {
         alert() {
          this.$swal('Hello word!')
        }
      }
    },
    mounted() {
      window.addEventListener('resize', () => {
        this.windowWidth = window.innerWidth
      })
    },
  }

</script>
