var metadata = {
    title:'Scratcpad',
    translations:[
        {
            locale:'de',
            localization_tags:[100,200],
            last_edit:'2014-04-14T08:43:37',
            url:'/de/decs/Tools/Scratchpad',
            title:'JavaScript-Umgebug',
        }
    ],
    url:'/en-US/doc/Tolls/Scratcpad'
};

//let {title:entitle,url:enurl,translations:[{locale,localization_tags:[x,y],last_edit,url,title}]} = metadata;
//let { translations:[{title}]} = metadata;//JavaScript-Umgebug
//let { translations:[{localization_tags:[x,y]}]} = metadata;//JavaScript-Umgebug 100 200
//console.log(x,y);
//console.log(url);
//console.log(translations);
// 
//console.log(Object.keys(metadata));
//console.log(Object.values(metadata));
//console.log(Object.assign({},metadata));// 这个是深拷贝
obj =  Object.assign({},metadata,{localization_tags:[1,2,3],url:'magedu.com'});//使用source 进行拷贝
console.log(obj);// 
// Promise 
// 概念
// promise对象对于一个异步操作的最终完成（包括成功和失败），及结果值的表示
// 简单的来说，就是处理异步请求
// 之所以叫做Promise,就是我承诺，如果成功则怎么处理，失败则怎样处理
// 





