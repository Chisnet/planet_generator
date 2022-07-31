import './style.css';

import * as THREE from 'three';
import * as uuid from 'uuid';
import Planet from './generator/Planet';


document.querySelector<HTMLDivElement>('#app')!.innerHTML = `
    <div id="container"></div>
`

const container = document.getElementById('container');

if (container) {
    const width = container.offsetWidth;
    const height = container.offsetHeight;

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(width, height);

    const cameraDistance = 65;
    const camera = new THREE.PerspectiveCamera(cameraDistance, width / height, 1, 200);
    camera.position.z = -cameraDistance;

    const scene = new THREE.Scene();
    scene.fog = new THREE.Fog(0x000000, cameraDistance * .4, cameraDistance * 1.2);

    const createScene = () => {
        const seed = uuid.v4();
        const planet = new Planet(seed);

        console.log(seed);
    };

    createScene();

    let lastTime = Date.now();

    const tick = () => {
        // const dt = Date.now() - lastTime;

        lastTime = Date.now();

        renderer.render(scene, camera);

        requestAnimationFrame(tick);
    }

    container.append(renderer.domElement);
    requestAnimationFrame(tick);
}
