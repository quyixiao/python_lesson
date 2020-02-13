
const a = function (x,y,z){
    return x ,y ,z ; //逗号表达式会以最后一个表达式求值，
}

const b = function (x,y,z){
    return (x ,y ,z ,x=z); //逗号表达式会以最后一个表达式求值，最后一个值是我们想要的值，求y的值。
}

console.log(a(...[4,5,60,7])); // 6 
console.log(b(...[4,5,60,7])); // 6 ,open ssl 是一个开源机构
console.log(c=1,2,3,4);//TypeError: Assignment to constant variable.
console.log((c=1,2,3,4,5)) ; // 这里用到了逗号表达式
console.log((c=(1,2,3,4,5))) ; // 这里用到了逗号表达式
// 表达式的值
// 类C的语言，都有一个概念，表达式的值
// 赋值表达式的值，等号右边的值
// 逗号表达式的值，类C语言，都支持逗号表达式，逗号表达式的值，就是最后的一个表达式的值
// 





