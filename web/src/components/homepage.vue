<template>
  <div>
    <el-row>
      <el-col :span="24"><div class="grid-content bg-purple-dark">
        <img style="width:100%;height:250px;" src="/dist/assets/images/banner.png">
      </div>
      </el-col>

    </el-row>

    <div class="siteList">
      <div class="siteItem" v-for="site in sites">

        <a :href="site.url" target="_blank">
         <img :src="site.image" :alt="site.title">
        </a>
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
      this.$http.get('http://127.0.0.1:8005/api/sites/', {}, {
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
