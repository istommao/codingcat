//是否允许分片打包
//如果允许分片打包，入口文件只能有一个
var isAnsyc = false

//打包路径配置
var configDir = {
  enteryDir: [
      './src/main.js',
         ],
    //将打包结果输出到目标路径, 为空时，打包后文件输出到 assets 目录
   outputDir: '' //'/home/tzf/Documents/web/static/classic/purchase/'  //支持一个输出路径
}

//是否提取css为单独文件从
var extractCss = true

//跨域调试 host
var hostName = 'http://127.0.0.1:8005'

//version
var vtag = 1


module.exports = {
  configDir: configDir,
  extractCss: extractCss,
  isAnsyc: isAnsyc,
  hostName: hostName,
  vtag: vtag,
}
