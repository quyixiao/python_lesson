const obj={
    a :100,
    b:200,
    c:300,
};

//console.log(...obj);//TypeError: undefined is not a function
let {a,b,c} = obj;//100 200 300
//let[a,b,c] = obj;//TypeError: obj is not iterable, 这个对象是不可以迭代的
console.log(a,b,c);//通过下面的方式就可以解构了
//var {x,y,z} = obj;//变量名一定和对象中的名称是一样的
//let {c:x,b:y,a:z} = obj;//300 200 100 使用别名
//let {c:x,b:y,a:z,d} = obj;//300 200 100 undefined
let {c:x,b:y,a:z,d:D=1000} = obj;// 使用这种打印方式 console.log(x,y,z,D); //300 200 100 1000
console.log(x,y,z,D);
//console.log(x,y,z);//undefined undefined undefined







