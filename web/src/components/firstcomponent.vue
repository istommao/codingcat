<template>
  <div class="mainContent">
    <i class="el-icon-edit"></i>
    <i class="el-icon-share"></i>
    <i class="el-icon-delete"></i>
<el-button type="primary" icon="search">搜索</el-button>

<el-button>默认按钮</el-button>
<el-button type="primary">主要按钮</el-button>
<el-button type="text">文字按钮</el-button>

<el-button type="primary" icon="edit"></el-button>
<el-button type="primary" icon="share"></el-button>
<el-button type="primary" icon="delete"></el-button>
<el-button type="primary" icon="search">搜索</el-button>
<el-button type="primary">上传<i class="el-icon-upload el-icon--right"></i></el-button>


<el-radio class="radio" v-model="radio" label="1">备选项</el-radio>
 <el-radio class="radio" v-model="radio" label="2">备选项</el-radio>


 <el-checkbox-group v-model="checkList">
   <el-checkbox label="复选框 A"></el-checkbox>
   <el-checkbox label="复选框 B"></el-checkbox>
   <el-checkbox label="复选框 C"></el-checkbox>
   <el-checkbox label="禁用" disabled></el-checkbox>
   <el-checkbox label="选中且禁用" disabled></el-checkbox>
 </el-checkbox-group>


 <el-select v-model="value" placeholder="请选择">
   <el-option
     v-for="item in options"
     :label="item.label"
     :value="item.value">
   </el-option>
 </el-select>

  </div>
</template>

<script>
  export default {
    data () {
      return {
        radio: '1',
        checkList: ['选中且禁用','复选框 A'],
        options: [{
          value: '选项1',
          label: '黄金糕'
        }, {
          value: '选项2',
          label: '双皮奶'
        }, {
          value: '选项3',
          label: '蚵仔煎'
        }, {
          value: '选项4',
          label: '龙须面'
        }, {
          value: '选项5',
          label: '北京烤鸭'
        }],
        value: ''
      };
    }
  }
</script>
