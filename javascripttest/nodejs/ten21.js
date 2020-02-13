// 方法 push(...items) 尾部增加多个元素
// pop()            移除最后的元素
// 

let arr = [1,2,3,4,5];
console.log(arr);
console.log(arr.map(
    function(x){
        return x + 10;
    }
));
console.log(arr.map( x => x + 10 ));
console.log(arr);//原来的东西不进行修改
console.log(arr.filter(x=> x > 2 ));
console.log(arr.filter(x=> !(x % 2)));
console.log(arr.filter(x=> x % 2)); // 奇数
console.log('=============================================')
console.log(arr.forEach(
    function (x){
        console.log(x);
        // 通过网络传输，所以不一定需要返回值，这个是没有返回值的
    }
));

console.log('**********************************************')
console.log(arr.forEach( x => console.log(x) ));// 这种写法在jquery 中太多的实现了
newarr = [];
// forEach 不返回值，也不对现有的值进行修改
console.log(arr.forEach( x =>newarr.push( x*x) ));// 这种写法在jquery 中太多的实现了
console.log(newarr);







