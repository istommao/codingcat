<template>
  <div id="app">
      <div class="container" id="container">
          <div class="sideMenu">
              <div class="siteName">CodingCat</div>
              <div class="menu">
                <ul>
                  <li v-for="menu in navmenus"><router-link :to="menu.to"><i :class="menu.icon" aria-hidden="true"></i>  {{ menu.name }}</router-link></li>
                </ul>
              </div>
          </div>
          <div class="mainWrapper">
              <div class="topBar">

                <div class="topMenu">
                  <el-menu :router="true" default-active="1" class="el-top-menu" mode="horizontal">
                    <el-menu-item index="/">首页</el-menu-item>
                    <el-menu-item index="/about">关于</el-menu-item>
                  </el-menu>
                </div>

                <div class="searchBox">

                </div>
              </div>
              <div class="main">
                <div class="mainContent">
                  <router-view class="view"></router-view>
                </div>
              </div>
          </div>
      </div>
  </div>

</template>

<script>
  export default {
    data() {
      return {
        navmenus: [
          {'name': '个人博客', 'icon': 'fa fa-file-o', 'to': '/blogs'},
          {'name': '资讯站点', 'icon': 'fa fa-book', 'to': '/infos'}
        ]
      }
    }
  };
</script>
