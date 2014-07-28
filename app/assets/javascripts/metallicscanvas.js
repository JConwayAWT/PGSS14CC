$(document).ready(function(){
  var scene = new THREE.Scene();
  var camera = new THREE.PerspectiveCamera( 75, 720 / 360, 0.1, 10000 );

	var renderer = new THREE.WebGLRenderer();
	renderer.setSize( 720, 360 );
	document.body.appendChild( renderer.domElement );
	var geometry = new THREE.SphereGeometry(1, 50, 50);
	var material = new THREE.MeshPhongMaterial( { color: 0x8B9C1E} );
	var sphere_array = []
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
	  sphere.rotation.x += 0.1;
	}
	render();
});