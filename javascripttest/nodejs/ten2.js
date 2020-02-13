// map arr = [1,2,3,4,5] => [2,3,4,5]
// 这就是非常常见的传递一个函数的功能，2-3-4-5 
const map = function (arr,fn){ // 就地修改，原数组每一个元素被改变，return new array 
    newarr = [] ;
    for(i in arr){
        newarr[i] = fn(arr[i]);
    }
    return newarr;
}

const map3 = (arr,fn) =>{ // 就地修改，原数组每一个元素被改变，return new array 
    newarr = [] ;
    for(i in arr){
        newarr[i] = fn(arr[i]);
    }
    return newarr;
}

function *add2(arr,fn) {  
    for (x in arr){
        yield fn(x) 
    }
}

console.log(map([1,2,3,4],function(x){
    return x + 1 ;
}));

// 下面就是数学公式一样，拿着箭头函数
// 箭头函数
// 箭头函数就是匿名的函数，它是一种更加精简的格式,箭头函数就匿名函数，就像一个数学公式一样的，
// 当只有一个形参的时候就可以省略掉，参数列表保留，如果是零个参数就保留
// 箭头的右边是一定要有大括号的，什么时候可以省略掉大括号，省略大括号。
console.log(1,map([1,2,3,4],x => x + 1));
console.log(2,map3([1,2,3,4],(x) => x + 10));
console.log(3,map3([1,2,3,4],(x) => {return x + 10}));
console.log((() => console.log('abc'))());// 这里打印的是一个函数的定义，这个是一个函数的定义，还是一个函数的调用，
// 如果遇到生成器的时候，千万不要忘记了，概念一定要清楚，根本不知道是怎样的，如果写出来的代码，
// 我们在做map 函数的时候，能省略就省略，不要
// 箭头函数，它是一种更加精简的格式，
// 以下的三行等价
// 箭头函数
// 如果一个函数没有，python 通过比较
// 大家还是要，箭头函数一定要掌握好的
// 


