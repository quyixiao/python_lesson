const counter = function (){ // 前面有些人是定义了一些标识符号，后面的人是不允许改这些变量的，保护了这些函数
    let c = 0;
    return function(){
        return ++c ;
    }
}

function counter1(){
    let c = 0;
    return function(){
        return ++c ;
    }
}

mycount = counter();//函数,
for (i = 0 ;i < 10 ;i ++){
    console.log(mycount())
}