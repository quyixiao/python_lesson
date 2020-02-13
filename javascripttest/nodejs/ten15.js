// 列表解构
var parts = ['shoulder','kness'];
var lyrics = ['head',...parts,'and','toes'];//使用解构 ,[ 'head', 'shoulder', 'kness', 'and', 'toes' ]
console.log(lyrics);

// 参数解构
function f(x,y,z){
    console.log(x+y+z);
}
var test = [1,2,3];
f(...test);


const arr = [100,200,300];
let [x,y,z] = arr;
console.log(1,x,y,z);

console.log('=============================================================')
