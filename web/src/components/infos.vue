<template>
  <div>
    <div class="siteList">
      <div class="siteItem" v-for="site in sites">

        <router-link :to="{ path: '/infos/' + (site.uid || 'unknown') }">
          <div class="imgDiv"><img :src="site.image" :alt="site.title"></div>

          <div class="siteTitle">
            {{ site.title }}
          </div>

          <div class="siteTags">
            <el-tag v-for="tag in site.tags" type="primary">{{ tag }}</el-tag>
          </div>
        </router-link>

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
      this.$http.get('http://115.29.189.159/api/sites/infos/', {}, {
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
