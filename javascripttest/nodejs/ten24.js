function runAsync(){
    return new Promise(function(resolve,reject){
        setTimeout(() => {
            console.log('do something')
            resolve('ok')
        }, 3000);
    });
}
// 调用
runAsync().then(value =>{
    console.log(value);
    return Promise.reject(value + '*');
}).catch(reason => {
    console.log(reason);
    return Promise.resolve(reason + '*');
}).then(value => {
    console.log('测试');
});



