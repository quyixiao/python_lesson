// 函数的变量的作用域 
function test(){
    a = 100;//全局变量，严格定义是这个是不可以用的
    var b = 200;
    let c = 300;
}
// 先要运行test函数
test();
console.log(a);
if(true){
    b = 1 ;
    c = 10;
}
console.log(b);//不可见 ,ReferenceError: b is not defined
console.log(c);//不可见 ,ReferenceError: c is not defined
// function 是函数的定义，是一个独立作用域，其中定义的变量在函数外不可见
// 



