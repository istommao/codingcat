'use strict'

let path = require('path')
let fs = require('fs')
let webpack = require('webpack')
let ExtractTextPlugin = require('extract-text-webpack-plugin')
let CleanWebpackPlugin = require('clean-webpack-plugin')
let precss = require('precss')
let autoprefixer = require('autoprefixer')
let configDir = require('./package.config').configDir
let extractCss = require('./package.config').extractCss
let isAnsyc = require('./package.config').isAnsyc
let hostName = require('./package.config').hostName
let vtag = require('./package.config').vtag
if(!configDir.outputDir) {
  configDir.outputDir = path.join(__dirname, 'dist')
}

let staticPath = '/dist/'

let isProduction  = process.env.NODE_ENV === 'development' ? false : true

let enteryFiles = function() {
  let enteryObj = {}
  if(configDir.enteryDir.length === 0 || configDir.enteryDir === undefined) {
    console.log('[webpack]', 'entry path need to configurated ')
    return
  } else {

    if(isAnsyc && configDir.enteryDir.length > 1) {
      throw ('[error]: only one entry file need when use code splitting!!')
    }

    configDir.enteryDir.map((item, index) => {
      fs.stat(item, function(err, state) {
        if(err) {
          throw ( 'path' + item + 'is not a correct path!')
        }
      })
      //打包文件
      let filePath = /[a-zA-Z0-9_-]+\/[a-zA-Z0-9_-]+\.js/.exec(item)[0].replace(/\.js/, '')  //filePath配置时把最后的 ‘/’去掉，否则在hot reload情况下，会出现文件无法找到情况
      console.log('filePath: ', filePath)
      if(isAnsyc) {
        filePath = filePath.split('/')
        configDir.outputDir = path.join(configDir.outputDir, filePath[0])
        enteryObj[filePath[1]] = [item]
      } else {
        enteryObj[filePath] = [item]
      }

    })
  }
  return enteryObj
}

let plugins = [
  new webpack.optimize.OccurenceOrderPlugin(),
  new webpack.NoErrorsPlugin(),
  // new webpack.optimize.CommonsChunkPlugin('common/common.js'),
  new ExtractTextPlugin( '[name].css?[hash]-[chunkhash]-[contenthash]-[name]', {
      disable: !extractCss,
      allChunks: true
    }),
  new webpack.DefinePlugin({
    'process.env': {
      'NODE_ENV': JSON.stringify(isProduction ? 'production' : 'development'),
      'HOST_NAME': JSON.stringify(isProduction ? '' : hostName)
    }
  }),
]

if(isProduction) {
  console.log('current env is production!')

  plugins.push(
    new webpack.optimize.UglifyJsPlugin({
      test: /(\.jsx|\.js)$/,
      compress: {
        warnings: false
      }
    })
  )
  plugins.push(
    new CleanWebpackPlugin(['dist/src'])
  )
} else {
  console.log('current env is development!')
}

module.exports = {
  devtool: isProduction ? null : 'source-map',
  entry: enteryFiles(),
  output: {
    path: configDir.outputDir,
    filename: '[name].bundle.js',
    publicPath: staticPath
  },
  plugins: plugins,
  module: {
    loaders: [{
      test: /\.js$/,
      loader: 'babel-loader',
      exclude: /node_modules/,
      include: __dirname
    }, {
      test: /\.vue$/,
      loader: 'vue-loader',
      exclude: /node_modules/,
      include: __dirname,
    }, {
      test: /\.css$/,
      loader: ExtractTextPlugin.extract('style-loader', 'css-loader!postcss-loader?sourceMap=inline'),
      include: __dirname,
    }, {
      test: /\.(jpe?g|png|gif|svg)$/i,
      loader: 'url-loader?limit=5000&name=[path][name].[ext]'
    }, {
        test: /\.(eot|woff|woff2|ttf)([\?]?.*)$/,
        loader: 'file-loader'
    }, { test: /\.(woff|woff2)$/, loader:"url?prefix=font/&limit=5000" },
    { test: /\.ttf(\?v=\d+\.\d+\.\d+)?$/,    loader: "url?limit=10000&mimetype=application/octet-stream" },
    { test: /\.eot(\?v=\d+\.\d+\.\d+)?$/,    loader: "file" },
    { test: /\.svg/, loader : 'file?prefix=font/' }
    ]
  },
  postcss: function () {
    return [precss, autoprefixer];
  }
}
