const add = function(x,y){
    return x + y ;
};

function add1(x,y){
    return x + y ;
}

console.log(add(4,6));

const sub = function fn(x,y) { 
    return x - y ;
 };

 console.log(sub(3,1));

 const sum = function _sum(n){
     if (n == 1 ) return 1;
     return n + _sum(n -1 );
 }
 console.log(sum(5)) ;//
 // 高阶函数
 const counter = (function *(){
    count = 0;
    while(true){
        yield count ++;
    }
})();

for(let i = 0 ;i < 10;i++){
    console.log(counter.next());
}









