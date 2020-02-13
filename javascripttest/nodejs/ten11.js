// 高阶对象，高价类，或称Mixin模式
// Mixin 模式，混合模式，这是一种不同的继承就可以复用的技术，主要是为了解决多重继承的问题，多继承的继承路径是个问题
// JS 是基于对象，类，和对象都是对象模板
// 混合Minxin，指的是将一个对象的全部或者部分拷贝到另一个对象上去，其实就是属性了
// 可以将多个类或者对象混合成一个类或者对象
// 继承实现
// 先看一个例子实现的例子
// 以上就是解决this问题，bind方法最常用
class Serialization{
    constructor(){
        console.log('Serilization constructor ---');
        if(typeof(this.stringify) !== 'function'){
            throw new ReferenceError('should defini stringify ');
        }
    }
}

class Point extends Serialization{
    constructor(x,y){
        console.log('Point constructor +++++');
        super();
        this.x = x ;
        this.y = y ;
    }
    // 实现了接口的功能
    stringify(){
        console.log('--------------');
    }

}




class Point3D extends Point{
    constructor(x,y,z){
        console.log('Point3D constructor +++++');
        super(x,y);
        this.z = z ;
    }
}


p1 =new Point(4,5);
console.log('-----------------------------------');
p3d = new Point3D(7,8,9);
p3d.stringify();
