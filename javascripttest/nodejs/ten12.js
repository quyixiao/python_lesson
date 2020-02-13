class A{

}
console.log(A);

function A1(){ //其实类和方法是一个东西

}

const B = class {
    constructor(x){
        this.x = x;
    }
}
console.log(B);
b =new B(4);
console.log(b.x);

const C = class extends B {

}

c = new C(2000);
console.log(c.x);


// 定义一个函数，传递一个参数，返回一个匿名类，这个匿名类继承于这个传入的参数
const d = (Sup) => class extends Sup{

}

console.log(typeof(d)) ;// d 是什么类型？ function 类型，用一个函数来返回一个类的定义

cls = d(B);         //返回什么，类定义，构造器
e = new cls(3000);
console.log(e.x);

//f = new d(B)(3000);
f = new (d(B))(3000);
console.log(f.x);


