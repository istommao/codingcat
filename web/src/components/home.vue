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
        <router-link :to="{ path: '/detail/' + (site.uid || 'unknown') }">
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
      this.$http.get('http://115.29.189.159/api/sites/home/', {}, {
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
