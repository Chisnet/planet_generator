import Face from "./Face";
import Point from "./Point";
import Tile from "./Tile";

const GOLDEN_RADIO = 1.61803399;

class Planet {
    seed: string;
    radius: number;
    tiles: Tile[];

    constructor(seed: string) {
        this.seed = seed;

        this.radius = 20;

        const corners = [
            new Point(1000, GOLDEN_RADIO * 1000, 0),
            new Point(-1000, GOLDEN_RADIO * 1000, 0),
            new Point(1000, -GOLDEN_RADIO * 1000, 0),
            new Point(-1000, -GOLDEN_RADIO * 1000, 0),
            new Point(0, 1000, GOLDEN_RADIO * 1000),
            new Point(0, -1000, GOLDEN_RADIO * 1000),
            new Point(0, 1000, -GOLDEN_RADIO * 1000),
            new Point(0, -1000, -GOLDEN_RADIO * 1000),
            new Point(GOLDEN_RADIO * 1000, 0, 1000),
            new Point(-GOLDEN_RADIO * 1000, 0, 1000),
            new Point(GOLDEN_RADIO * 1000, 0, -1000),
            new Point(-GOLDEN_RADIO * 1000, 0, -1000)
        ];

        const points = [];

        for (const [index, corner] of corners.entries()) {
            points[index] = corner;
        }

        const faces = [
            new Face(corners[0], corners[1], corners[4], false),
            new Face(corners[1], corners[9], corners[4], false),
            new Face(corners[4], corners[9], corners[5], false),
            new Face(corners[5], corners[9], corners[3], false),
            new Face(corners[2], corners[3], corners[7], false),
            new Face(corners[3], corners[2], corners[5], false),
            new Face(corners[7], corners[10], corners[2], false),
            new Face(corners[0], corners[8], corners[10], false),
            new Face(corners[0], corners[4], corners[8], false),
            new Face(corners[8], corners[2], corners[10], false),
            new Face(corners[8], corners[4], corners[5], false),
            new Face(corners[8], corners[5], corners[2], false),
            new Face(corners[1], corners[0], corners[6], false),
            new Face(corners[11], corners[1], corners[6], false),
            new Face(corners[3], corners[9], corners[11], false),
            new Face(corners[6], corners[10], corners[7], false),
            new Face(corners[3], corners[11], corners[7], false),
            new Face(corners[11], corners[6], corners[7], false),
            new Face(corners[6], corners[0], corners[10], false),
            new Face(corners[9], corners[1], corners[11], false)
        ];

        this.tiles = [];

        for (var point of points) {
            var newTile = new Tile(point);
            this.tiles.push(newTile);
        }
    }

    toObj = () => {
        const vertices = [];
        const faces = [];

        for(const tile of this.tiles) {
            const face = [];

        }
    }
}

export default Planet;
