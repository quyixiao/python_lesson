class Point{
    constructor(x,y){
        this.x = x ;
        this.y = y ;
        
    }
    static show(){
        console.log(2,this,this.x,this.y);
    }
}

point = new Point(4,6);
Point.show();
class Point3D extends Point{
    constructor(x,y,z){
        super(x,y);
        this.z = z;
    }
    static show(){
        super.show();
        console.log(4,this,this.x,this.y,this.z);
    }
}

point3d =new Point3D(4,5,6);
//console.log(point3d.show());
point3d.constructor.show();//通过构造器来访问到一个中的属性

Point3D.show();
console.log(point3d.constructor.show === Point3D.show);//表示相等

