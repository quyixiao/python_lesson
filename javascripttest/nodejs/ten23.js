let myPromise = new Promise(
    function (resolve,reject){
        var x = 1 + 1 ;
        resolve('ok');
        setTimeout(()=>resolve('ok'),5000);
        console.log('-------------------------');
       /// reject('Not ok');

    }
);
console.log(myPromise);
myPromise.then(
    value => {
        console.log('successed',value);
        return Promise.reject('wrong');
    },
    reason => console.log('failed',reson)
).then(
    value => console.log('successed1',value),
    reason => {
        console.log('failed1',reason)
        return Promise.reject('exceptionxxxxxxxx  ' );
    }
).catch(
    reson => console.log('exception' ,reson)
);
console.log('=================================');
// executor 是一个带有resolve 和reject 两个参数的函数
// executor 函数在Promise构造函数执行的同时执行，被传递的resolve和reject函数（executor 函数Promise构造函数返回新建对象）
// 前被调用
// executor内部通常会执行一些异步操作，一旦完成，可以调用
// 

