export default function a() {
    console.log('test.a()');
  }

export default class {
    constructor(x){
        this.x = x ;
        console.log(x)
    }
    show(){
        console.log(this.x);
    }
}

  export function b(){
      console.log('test1.b()');
  }

  export let c = 100;
  export var d = 200;
  export const e = 300;

  export {b,c,d};


