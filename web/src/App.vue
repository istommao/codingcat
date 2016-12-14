<template>
  <div id="app">
    <div class="topNav" id="topNav">
      <div class="topbarHead">
        编程猫
      </div>
    </div>
    <div class="container" id="container">
      <div class="aside" id="sidebar">

        <div class="menu">
          <ul>
            <li><router-link to="/icon">Icon 图标</router-link></li>
            <li><router-link to="/button">Button 按钮</router-link></li>
            <li><router-link to="/radio">Radio 单选框</router-link></li>
            <li><router-link to="/checkbox">Checkbox 多选框</router-link></li>
            <li><router-link to="/select">Select 选择器</router-link></li>
            <li><router-link to="/switch">Switch 开关</router-link></li>
            <li><router-link to="/date">DatePicker 日期选择器</router-link></li>
            <li><router-link to="/upload">Upload 上传</router-link></li>
            <li><router-link to="/form">Form 表单</router-link></li>
            <li><router-link to="/card">Card 卡片</router-link></li>
          </ul>
        </div>

      </div>
      <div class="main">
        <router-view class="view"></router-view>
      </div>
    </div>
  </div>
</template>

<script>

</script>

<style>
body {
  font-family: Helvetica, sans-serif;
}

</style>
