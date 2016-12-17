<template>
  <div id="app">
      <div class="container" id="container">
          <div class="sideMenu">
              <div class="siteName">CodingCat</div>
              <div class="menu">
                <ul>
                  <li><router-link to="/">首页</router-link></li>
                  <li><router-link to="/blogs">个人博客</router-link></li>
                  <li><router-link to="/infos">资讯站点</router-link></li>

                  <!-- <li><router-link to="/icon">Icon 图标</router-link></li>
                  <li><router-link to="/button">Button 按钮</router-link></li>
                  <li><router-link to="/radio">Radio 单选框</router-link></li>
                  <li><router-link to="/checkbox">Checkbox 多选框</router-link></li>
                  <li><router-link to="/select">Select 选择器</router-link></li>
                  <li><router-link to="/switch">Switch 开关</router-link></li>
                  <li><router-link to="/date">DatePicker 日期选择器</router-link></li>
                  <li><router-link to="/upload">Upload 上传</router-link></li>
                  <li><router-link to="/form">Form 表单</router-link></li>
                  <li><router-link to="/card">Card 卡片</router-link></li>
                  <li><router-link to="/notice">Notification 通知</router-link></li> -->
                </ul>
              </div>
          </div>
          <div class="main">
              <div class="topBar"></div>
              <div class="mainContent">
                <router-view class="view"></router-view>
              </div>
          </div>
      </div>
  </div>

</template>

<script>

</script>
