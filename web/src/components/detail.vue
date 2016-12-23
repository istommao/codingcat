<template>
  <div class="siteItem">
    <a :href="site.url" target="_blank">
      <div class="imgDiv"><img :src="site.image" :alt="site.title"></div>

      <div class="siteTitle">
        {{ site.title }}
      </div>

      <div class="siteTags">
        <el-tag v-for="tag in site.tags" type="primary">{{ tag }}</el-tag>
      </div>
    </a>
  </div>
</template>

<script type="text/javascript">
  export default {
    data() {
      return {
        site: {}
      }
    },
    mounted: function() {
      var api = '/api/detail' + this.$route.path + '/';
      this.$http.get('http://127.0.0.1:8005' + api, {}, {
          headers: {},
          emulateJSON: true
      }).then(function(response) {
        this.site = response.data
      }, function(response) {
        console.log(response)
      });
    }
  }

</script>
