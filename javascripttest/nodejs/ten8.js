class Point{
    constructor(x,y){
        this.x = x ;
        this.y = y ;
        this.show = function(){    console.log(1,this,this.x,this.y);}
    }
    show(){
        console.log(2,this,this.x,this.y);
    }
}

point = new Point(4,6);
point.show();
class Point3D extends Point{
    constructor(x,y,z){
        super(x,y);
        this.z = z;
        this.show = () => {
            console.log(3,this,this.x,this.y,this.z);
        }
    }
    show(){
        super.show();
        console.log(4,this,this.x,this.y,this.z);
    }
}
// 当属性名和方法名相同的时候，先调用属性,属性优先调用
point3d =new Point3D(4,5,6);
point3d.show();
// ES6的Class
// 从ES6开发，新提供了class 关键字，使得创建对象更加简单，一个构造器用
// 优先使用了子类的属性
// 总结：
// 父类，子类使用了同一种方法，子类覆盖了父类
// 如果父类使用属性，子类使用方法，则使用父类的属性，如果父类使用方法，子类使用属性，则使用子类的方法，所以，一句话，优先使用属性
//                                                                                                                                           

