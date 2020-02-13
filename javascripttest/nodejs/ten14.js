try{
    throw ()=>{};
    //throw new Error();
    //throw 1;
    //throw new Number(1000);
    //throw 'not ok';
    //throw [1,2,3];
    //throw {'a':1};
}catch(error){ //只能写一个异常，
    console.log(typeof(error));
    console.log(error.constructor.name);
}finally{
    console.log('================end==================')
}
//模块化
// ES6 ,js 没有出现的模块化系统
// js 主要在前端的浏览器中使用，js文件下载缓存的客户端，在浏览器中运行
// 比如简单的表单本地验证，漂浮一个广告
// 服务器使用ASP ,JS 等动态网页技术，将动态的生成数据嵌入一个HTML 模板中，里面夹杂着JS使用<script></script>标签，返回浏览器端
// 2005年后，随着Google大量使用ajax技术之后，可以异步请求服务器端数据，带来的前端交互的巨大变化，前端功能需要起来越多
// 代码也越来越多，随着js 文件的增多，灾难性的后果来了，由于习惯了随便写，js脚本就出现问题了
// 转译工具，转译就是一种语言转换成另一个语言的代码，当然也可以从高版本转译成低版本，的支持语句
// 由于js存在不同的版本，不同的浏览器兼容问题，如何解决对语法的支持问题
// 使用transpiler转译工具解决
// babel
// 预设
// 在项目
// 本次放到项目根目录中，内容如下
// registry=https://registry.npm.taobao.org 
// .npmrc 文件
// 可以放到npm的目录下的npmrc 文件中
// 可以入在用户家目录中
// 可以放到项目根目录中
// 开发依赖，不是布署依赖，这些东西是开发用的，而不是布署用的，所以，我们，我们经常使用这种东西，但是
// 但是，依赖，最后运行时依赖，
// 安装
// 项目根目录下执行
// npm install 
// 
// {
//     "name":"trans",
//     "version":"1.0.0"
//      "description": "",
//      "main":
//}

// 准备目录
// 项目根目录下建立

// {
//  "preset":["env"],
//
//}
// npm install --save-dev babel-core
// require("babel-core").transform("code");
// 安装依赖
// 准备js文件
// 准备js文件
// 
