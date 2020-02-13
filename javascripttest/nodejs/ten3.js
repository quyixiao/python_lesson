function add1(x,y){
    ret = x + y ;
    console.log(ret );
    return ret ;
}

const add2 = function(x,y){
    ret = x + y ;
    console.log(ret );
    return ret ;
}

const add3 = (x,y)=>{
    ret = x + y ;
    console.log(ret );
    return ret ;
}

const add4 = (x=4,y) => x+y ;

const add5 = (...args)=>{
    //console.log(arguments) // 在箭头函数中不要使用 arguments 中 
    console.log(args)
    s = 0
    for(x of args){
        s += x
    }
    return s ; 
}

console.log(add4(4,5));
console.log(add4(4,5,6))
console.log(add4(x=4,y=5,z=6)) // 
console.log(add4(a=4,x=5,z=6)) // 表达式的值，关键字传参
console.log(add4(11)) // NaN
console.log(add4()) //NaN
console.log(add4([4,5])) // 4,5undefined 这个转换成字符串相加
console.log(add4(...[4,5,6]))
console.log(add4(4));//NaN 在各种语言中都是一样的 ,还是可以吗？尝试一下
// 上面的调用结果 
// 为什么？
// 1.js 并没有python 中的关键字传参
// 
console.log(1111111,add5(...[4,5,6]));
// 可变参数
// 

console.log('-------------------------------------')
const add6 = function(...args){
    console.log(1,arguments);
    console.log(args);
    console.log(typeof args);
    s = 0;
    for(x of args){
        s += x ;
    }
    return s ;
}

console.log(add6(...[4,5,6]))


(function (p1,...args){
    console.log(p1);
    console.log(args);
    console.log('-----------------')
    console.log(arguments)
    for (let x of arguments){
        console.log(x);
    }
})('abc',1,3,5);
// ES6 之前，arguments 是唯一的参数的实现
// ES6 开始，不推荐，建义使用可变参数，为了兼容而保留
// 注意，使用箭头函数，取到的arguments不是我们想要的东西了
// 
((x,...args) => {
    console.log(args) ;//数组
    console.log(x);
    console.log(arguments);
})(...[1,2,3,4,5]);
// 参数解构
// 和Python 类似，JS提供了参数解构，依然使用了...符号来解构
















