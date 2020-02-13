function hello(){
    let a = 1 ;
    var b = 2 ;
    c = 3 
}
let d = 100;
if (1){
    let d = 4 ;
    var e = 5 ;
    f = 6 ;
    if (true ){
        console.log(d)
        console.log(e)
        console.log(f)
        console.log('-----------------')
        g = 10 ;
        var h = 11 ;
    }
}

//console.log(a) ;// 不可见
//console.log(b) ;// 不可见
//console.log(c) ; // 不可见
console.log(d);// 块作用域使用let ,外界是不可见的
console.log(e) ;// var块作用域是可见的
console.log(f) ; // 块作用域是隐式声明，是可见的
console.log(g);//
console.log(h);//



console.log('-----------------------------------')
if({}){
    console.log('true')
}

console.log('-----------------------------------')

let x = 5  ;
switch(x){
    case 0 :
        console.log('zero');
        break;
    case 1 :
        console.log('one');
        break;
    case 5:
    case 4 :
        console.log('four');
        break;
    default:
        console.log('other');
        break;
}

if(x == 4 || x == 5 ){
    console.log('four');
    console.log('other')
}


if(x == 0){
    console.log('zero')
}else if (x == 2 ){
    console.log('')
}else if (x == 3 ){
    console.log('3')
}else if (x==4){
    console.log(4)
}else {
    console.log('other')
}








