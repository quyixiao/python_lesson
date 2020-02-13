

function * inc(){
    let i = 0;
    let j = 7;
    while(true ){
    yield i ++ ;
        if (!j--) return 100;
    }
}

let gen = inc();
for (let i = 0 ;i < 10;i ++){
    let x = gen.next();
    console.log(x.done ,x.value )
}


const sum = function _sum(n){
    if (n == 1 ) return n ;
    return n +_sum(n -1 );
}

console.log(sum(5)) // 1 + 2 + 3 + 4 + 5 





// 每次调用next() 方法返回了一个对象，这个对象包含了两个属性，value 和done ，value 属性表示本次yield 表达式的返回值
// done 属性为布尔类型，done是false 表示后续还有yield 语句执行，如果执行完成或者return 后，done 为true 
// 
// js 语法
// 语句块
// js使用大括号构成语句块
// ES6 之前语句块是没有作用域，从ES6开始支持块作用域，let 也只有在块作用域中
// 





