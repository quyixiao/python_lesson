x = 42;
var y = 43 ;
let z = 60 
myobj = new Number()
myobj.h = 4 ; //create property (can delete if declare impicaly)
console.log(delete x); //return true 
console.log(delete y ); //return false  cannot delete if declared with var 
console.log(delete z) ; //return false 
console.log(delete Math.PI) // 
console.log(delete myobj.h) // return true 
console.log('-----------------------------------------------------')


var trees = new Array('redwood','bay','cedar','oak','maple')
for (var i = 0 ;i < trees.length ;i ++){
    console.log(trees[i])
}
delete trees[3] // 数组中的元素被删除，但是空着的位置是undefined

console.log('***************************************')

for (var i = 0 ;i < trees.length ;i ++){
    console.log(trees[i])
}


var trees = new Array('redwood','bay','cedar','oak','maple') 

console.log(0 in trees) ; // return true 0 在数组的index 中
console.log(3 in trees) ;// return true ,3 在数组的对象中index 中
console.log(6 in trees) ;// return false ，6 不在数组的index 中
console.log('bay' in trees) ;// return false bay 不是属性，它是值
console.log('length' in trees );//return true ；length 它是对象的属性
console.log('------------------')

delete trees[3];
console.log(3 in trees) ;// return false 


for (var i = 0 ;i < trees.length ;i ++){
    console.log(trees[i])
}

console.log('------------------')
//let mycar = [
 //   color:"red",
  //  year:1998 
//];
//console.log('color' in mycar);
//console.log('model' in mycar);
// .[]
// () new 
// ! - + ++ -- typeof void delete 
// * / % 
// + - 
// << >> >>>
// < <= > >= in instanceof 
// == != === !==
// & 
// | 
// ^ 
// && 
// || 
// ?:
// = = -= *= /= %= <<= >>= >>>= &= ^= |=
// ,
// 逗号预算法优先级最低，比赋值语句还低
// 记不住，就使用括号
// 表达式
// 基本表达式
// 











