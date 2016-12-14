<template>
  <div class="mainContent">
    <div v-loading="siteLoadding">
      <div v-for="site in sites" class="text item">
        {{site.url}}
      </div>
    </div>

    <el-switch
      v-model="value1"
      on-text="开"
      off-text="关">
    </el-switch>
    <el-switch
      v-model="value2"
      on-color="#13ce66"
      off-color="#ff4949">
    </el-switch>
  </div>
</template >

<script>
export default {
  data() {
    return {
      sites: [],
      value1: true,
      value2: true,
      siteLoadding: true
    }
  },
  mounted: function() {
    this.$http.get('http://127.0.0.1:8005/sites/', {}, {
      headers: {},
      emulateJSON: true
    }).then(function(response) {
      this.sites = response.data.results;
      this.siteLoadding = false;
    }, function(response) {
      console.log(response)
    });
  }
}
</script>
