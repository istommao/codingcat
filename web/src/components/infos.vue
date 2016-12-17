<template>
  <div>
    <div class="siteList">
      <div class="siteItem" v-for="site in sites">

        <a :href="site.url" target="_blank">
         <img :src="site.image" :alt="site.title">
        </a>
        <div class="siteTitle">
          {{ site.title }}
        </div>
      </div>
    </div>
  </div>
</template>

<script type="text/javascript">
  export default {
    data() {
      return {
        sites: []
      }
    },
    mounted: function() {
      this.$http.get('http://127.0.0.1:8005/api/sites/infos/', {}, {
          headers: {},
          emulateJSON: true
      }).then(function(response) {
        this.sites = response.data.results
      }, function(response) {
        console.log(response)
      });
    }
  }

</script>
