// 有一个数组const arr=[1,2,3,4,5],要求出元素的平方值是偶数且大于10 

const s = Math.sqrt(10);

console.log(s);

arr=[1,2,3,4,5,6,7,8,9,10,11,12]

b = arr.filter(x => !(x%2) && x > s );

console.log(b);

c = arr.map(x=>{
    if(!(x%2) && (y = x * x ) > 10 ){
        return y ;
    }
});

console.log(c);

let newarr = []
arr.forEach(x => {
    if (x > s && !(x%2)){
        newarr.push(x*x);
    }
});

console.log(newarr);
// 对象的操作

// Object 的静态方法
// 

