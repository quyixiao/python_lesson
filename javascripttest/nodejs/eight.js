var obj = {
    'a' : 10,
    'b' : 20 
}



for (x in obj){
//for (x of obj){ 对象不能用of 
    console.log(x,obj[x])
}

// for in 循环返回的是索引或者key ,需要间接访问到值
// 数组返回正返回的是索引，C风格for循环可能操作方便一点的，
// 注意for of 不能迭代对象，原因是of后面的是一个迭代器
// 
function sum(arr){
    for (let x in arr){
        console.log(x,typeof(x),arr[x])
    }
    for(let x of arr){
        console.log(x,typeof(x))
    }
    for (let x = 0; x<arr.length;x ++){
        console.log(x,typeof(x),arr[x])
    }
}

sum([1,3,5])
// js 语法
// 函数
// function 函数名（参数列表）{
//    函数体
//}


function a (x){
    return x 
}

console.log(a)




