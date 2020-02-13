class Point {
    constructor(x,y){
        console.log('Point constructor +++++');
        this.x = x ;
        this.y = y ;
    }
    // 实现了接口的功能
    stringify(){
        console.log('--------Point------',this.x,this.y);
    }
}

const Serialization = Sup => class extends Sup{
    constructor(...args){//js 调用可变参数来解决
        super(...args); // js 存在参数解构
        console.log('Serilization constructor ---');
        this.xyz =()=>{
            console.log(' 我是xyz ');
        }
        if(typeof(this.stringify) !== 'function'){
            throw new ReferenceError('should defini stringify ');
        }
    }
}

class Point3D extends Serialization(Point){
    constructor(x,y,z){
        console.log('Point3D constructor +++++');
        super(x,y);
        this.z = z ;
    }
     // 实现了接口的功能
     stringify(){
        console.log('--------Point3D------',this.x,this.y,this.z);
    }
}

p1 =new Point(4,5);
p1.stringify();
console.log('-----------------------------------');
p3d = new Point3D(7,8,9);
p3d.stringify();
//尽量少的改变原有函数和类的定义，将新的代码注入进去的，使得程序更加的灵活，this 构造器，如何定义将
// 注意
// Serialization(Point) 这一步实际上是一个匿名的箭头函数调用，
// 异常
// 抛出异常
// try ... catch 语句捕获异常
// 











































