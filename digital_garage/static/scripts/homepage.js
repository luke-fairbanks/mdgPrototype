//USING THREE.JS TO INCLUDE 3D MODELS
import * as THREE from 'https://cdn.skypack.dev/pin/three@v0.137.5-HJEdoVYPhjkiJWkt6XIa/mode=imports/optimized/three.js';
//import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader'
//import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'
//import { GLTFLoader } from 'https://unpkg.com/three@0.120.1/jsm/loaders/GLTFLoader';

function main(){
    const canvas = document.querySelector("#landing-car");
    const renderer = new THREE.WebGLRenderer({canvas})

    //camera parameters
    const fov = 75;
    const aspect = 2; // the canvas default
    const near = 0.1;
    const far = 5;
    const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
    camera.position.z = 2;

    const scene = new THREE.Scene();

    //loading in our 3d model
    const loader = new GLTFLoader();
    loader.load('./assets/free_1972_datsun_240k_gt/scene.gltf', 
    function(gltf){
        scene.add(gltf.scene);
    },undefined, function(error){
        console.log(error);
    })

    renderer.render(scene, camera);

    const color = 0xFFFFFF;
    const intensity = 1;
    const light = new THREE.DirectionalLight(color,intensity)
    light.position.set(-1, 2, 4);
    scene.add(light);

    function render() {

        requestAnimationFrame(render);
    }
    requestAnimationFrame(render);
}

main();