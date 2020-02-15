# 项目依赖安装
# 将项目开发基本文件 react-mobx-starter-master-zip 解压缩，并用这个目录作为项目的目录
# 在项目根目录中，执行下面的代码，就会自动按照package.json的配置安装依赖模块
# npm install
# 或者
# npm i
# 安装完成之后，会生成一个目录，node_modules ，里面是安装的所有的依赖的模块
# 项目整体说明
# 项目目录结构
# .
# .babelrc
# .gitignore
# index.html
# jsconfig.json
# LICENSE
# .npmrc
# package.json
# README.md
# src
#       APP.js
#       AppState.js
#       index.html
#
#  start 指定启动的webpack的dev server 开发用WEB Server ，主要提供了2个功能，静态文件支持，自动刷新和热替换HMR
# HRM 可以在应用程序运行中替换，添加，删除模块，而无需重载页面，只把变化部分替换掉，不使用HMR 则自动刷新会导致这个页面刷新
#   --hot启动HMR
#   --inline 默认模式，使用HMR的时候建义开启inline模式，热替换时会消息显示在控制台
# build 使用webpack构建打包，对应 npm run build
# 项目依赖
# devDependencies 开发时依赖，不会打包到目标文件中，对应npm install xxx --save-dev ，例如babel 的一些依赖运行时，会打包
# 对应npm install xxx --save .
# 版本号指定
# 版本号，只安装的时候指定版本号
# 版本号， la
# latest ,安装最新版本
# babel转译，因为开发用了很多的ES6的语法，从6.x开始babel 拆分成很多的插件，需要引入什么
# babel-core 核心
# babel-loader webpack的loader，webpack是基于loader 的
# babel-preset-xxx预设的转换插件
# babel-plugin-transform-decorators-legacy 下面的的课程用到了装饰器，这个插件就是地图的装饰器用的
# css 样式相关的包括
# css-loader ,less,less-loader,style-loader
# react-hot-loader react 加载插件，希望心动保存后，直接在页面上直接反馈出来，不需要手动刷新
# source-map 文件打包，js会合并或者压纹，没法调试，用它来看js原文件是什么，source-map-loader也需要webpack的loader
# webpack 打包工具，2.4.1 发布于2017年4月，当前2.7.0 发布于2017年7月
# webpack-dev-server 启动一个开发的server
# 运行时依赖
# antd ant design 基于react实现，蚂蚁金服开源的react的UI库，做中后台管理非常方便
# axios 异步请求支持
# polyfill 解决浏览器api 不支持的问题，写好polyfill就让你的浏览器支持，帮你持平差异化
# react 开发的主构架
# react-dom 支持DOM
# react-router 支持路由
# react-router-dom DOM绑定路由
# mobox 状态管理库，透明化
# mobox-react,mobx-react-devtools-mox 和react 结合的模块
# babel 配置
# .babelrc babel 转译的配置文件
# {
#
# }
# webpack配置
# webpack.config.dev.js
# webpack.config.

# devtool:'source-map'
# 生成及如何生成source-map文件
# source-map 适合生成环境使用，会生成完成Sourcemap独立的文件
# 由于在Buillde中添加了引用注释，所在在开发工具知道如何找到Sourcemap
# entry 入口
# 描述入口，webpack会从入口开始，找出直接或者间接的模块和库，最后输出
# output 输出
# 告诉webpack输出bundles到哪里去，如何命名
# filename定义输出的bundle的名称
# path 输出目录的是__dirnam+'dist' ,名字叫做bundle.js
# publicPath 可以是绝对路径，或者相对路径，一般不会以/结尾，/assets/表示网站根目录下的assets目录下
# resolve解析
# 设置模块如何被解析
# module模块
# 如何处理不同的模块
# LESS
# CSS 的好处简单易学，但是坏处没有模块化，复用的概念，因为它不是语言
# LESS 是一门的预处理语言，扩展的CSS ,增加了变量，Mixin，函数等开发语言的特性，

# @color : #4D926F
# header{
# 可以使用解析器，将写好的LESS 解析成CSS,LESS 可以使用使用在浏览器端和服务器端
# node_modules/.bin/sessc test.less
# compress
# proxy:{
#  proxy 'api'{
#   target : 'http://127.0.0.1:8080' # port 启动端口 3000
# hot 启动HMR
#
# }
# }
# 将网页的所有的内容映射到一棵树型结构，浏览器提供了对DOM的支持，用户可是用脚本调用，DOM API 来动态的修改DOM结点
# 从而达到修改网页的目的，这种修改浏览器中完成，浏览器会根据DOM改变绘改变的DOM结点部分
# 修改DOM 重新渲染代价太高，前端框为了提高效率，尽量的减少DOM的重绘，提出了VirtualDOM ，所有的修改都是现在Virtual DOM
# 中完成，通过比较算法，找到浏览器DOM 之间的差异，使用这个操作DOM ,浏览器只需要渲染这部分变化就行了
# 支持JSX 语法
# JSX 是一种JAvaScript 和XML混写的语法，是JavaScript 的展
# 支持JSX语法
# JXS 是一种JAvaScript 语法
# content 字段问题
# 博客选取什么字段类型
# 多大合适
# 博文中的图片如何处理
# 适合的其它的字段放在同一张表吗？
# 思考
# 博文一般很长，不可能只有几百个字符，需要大文本字段，MySql 中选择Text类型，而不是char 或者varchar 类型
# 大小
# content 文章内容，博文内容可能很长，一般来说不会小于256个字
# 大小
# text 类型是65535 个字符，也不太够用，选择longtext 是有2^32 -1 个字符长度，应该说足够使用了
# 图片存储
# 博文就像Html 一样，图片是通过路径信息将图片嵌入内容中的，所以保存内容还是字符串
# 注意：这里的SQL脚本本次不要用来生成表，使用ORM工具来创建表，用来检查实体类构建是否正确
# 用户完成有功能有
# 登录，注册，登出
# 博客，
# 用户发文，文章列表，访问详情
# 注意，Pycharm 社区版本按照上面的步骤创建项目，创建新的虚拟环境的项目打开后，解释器的路径指向不对，但是虚拟环境已经创建好了
# 可以删除项目，重新建立，选择已经存在的解释器里面虚拟环境即可
# 本次Django开发后台，下面就开始Django 之旅





















