var sphere_array = [];
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, 720 / 360, 0.1, 10000 );

var renderer = new THREE.WebGLRenderer();
$(document).ready(function(){
	renderer.setSize( 720, 360 );
	$("#metallics-canvas").html( renderer.domElement );
	/*
	var geometry = new THREE.SphereGeometry(1, 50, 50);
	var material = new THREE.MeshPhongMaterial( { color: 0x8B9C1E} );
	for (i = 0; i < 5; i ++){
		var sphere = new THREE.Mesh(geometry, material);
		sphere_array.push(sphere);
	}
	for (i = 0; i < sphere_array.length; i++)
	{
		sphere = sphere_array[i];
		sphere.position.x = 2.5 - .5 * i;
		sphere.position.y = 0;
		sphere.position.z = 0;
		scene.add(sphere);
	}
	*/
	// var geometry = new THREE.SphereGeometry(1.5, 50, 50);
	// var material = new THREE.MeshPhongMaterial( { color: 0xfdca00 } );
	// var sphere = new THREE.Mesh( geometry, material );
	// sphere.position.x = -1.5;
	// sphere.position.y = 0;
	// sphere.position.z = 0;
	// scene.add( sphere );

	// var sphere1 = new THREE.Mesh( geometry, material );
	// sphere1.position.x = 1.5;
	// sphere1.position.y = 0;
	// sphere1.position.z = 0;
	// scene.add( sphere1 );


	camera.position.z = 5;
	scene.add(camera);
	var pointLight = new THREE.PointLight( 0xFFFFFF );

	// set its position
	pointLight.position.x = 0;
	pointLight.position.y = 0;
	pointLight.position.z = 6;

	// add to the scene
	scene.add(pointLight);

	function render() {
	  requestAnimationFrame(render);
	  renderer.render(scene, camera);	  
	}
	render();
});

function loadSpheres(atoms){
	sphere_array=[];
  	var geometry = new THREE.SphereGeometry(1, 50, 50);
  	var material = new THREE.MeshPhongMaterial( { color: 0x8B9C1E} );
  	for(var i=0;i<atoms.length;i++){
	    console.log(atoms[i]);
	    var sphere = new THREE.Mesh(geometry, material);
	    sphere.position.x=atoms[i].x;
	    sphere.position.y=atoms[i].y;
	    sphere.position.z=atoms[i].z;
	    sphere_array.push(sphere);
	    scene.add(sphere);
	    console.log("add sphere "+i);
  	}
}