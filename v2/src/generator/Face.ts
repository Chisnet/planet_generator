import Point from "./Point";

class Face {
    point1: Point;
    point2: Point;
    point3: Point;

    constructor(x: Point, y: Point, z: Point, register: boolean=true) {
        this.point1 = x;
        this.point2 = y;
        this.point3 = z;

        if(register) {

        }
    }
}

export default Face;
