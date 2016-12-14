<template>
  <div class="mainContent">
    <el-switch
      v-model="value1"
      on-text="开启"
      off-text="关闭">
    </el-switch>
    <el-switch
      v-model="value2"
      on-color="#13ce66"
      off-color="#ff4949">
    </el-switch>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        value1: true,
        value2: true
      }
    }
  };
</script>
