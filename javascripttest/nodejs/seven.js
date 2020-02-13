
// while 循环
// 先进入循环

let x = 10;
while(x --){
    console.log(x)
}
do{
    console.log(x)
}while(x ++ < 10)
// 
for(var i = 0 ;i < 10 ;i ++){
    line = '';
    for(var j = 1 ; j<=i ;j ++){
        line += `${j}*${i}=${i*j}` + ' '
    }
    console.log(line)
}

console.log('==================================')
for(var i = 0 ;i < 10 ;i ++){
    line = '';
    for(var j = 1 ; j<=i ;j ++){
        line += j + '*' +i + '=' + (i * j ) + ' '
    }
    console.log(line)
}
console.log('==================================')
var arr = ['a','b','c']

for (x in arr){
    console.log(x,arr[x])
}
console.log('==================================')
for (i = 0;i < arr.length ;i ++){
    console.log(arr[i])
}

var obj = {
    'a' : 10,
    'b' : 20 
}



for (x in obj){
    console.log(x,obj[x])
}

