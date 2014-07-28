var sphere_array = [];
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, 720 / 360, 0.1, 10000 );

var renderer = new THREE.WebGLRenderer();
$(document).ready(function(){
	renderer.setSize( 720, 360 );
	$("#metallics-canvas").html( renderer.domElement );


	var geometry_Al = new THREE.SphereGeometry(1.25, 50, 50);
	var geometry_Ni = new THREE.SphereGeometry(1.35, 50, 50);
	var geometry_Cu = new THREE.SphereGeometry(1.35, 50, 50);
	var geometry_Pd = new THREE.SphereGeometry(1.4, 50, 50);
	var geometry_Ag = new THREE.SphereGeometry(1.6, 50, 50);
	var geometry_Pt = new THREE.SphereGeometry(1.35, 50, 50);
	var geometry_Au = new THREE.SphereGeometry(1.35, 50, 50);

	var material_Al = new THREE.MeshPhongMaterial( { color: 0xBFA6A6} );
	var material_Ni = new THREE.MeshPhongMaterial( { color: 0x50D050} );
	var material_Cu = new THREE.MeshPhongMaterial( { color: 0xC88033} );
	var material_Pd = new THREE.MeshPhongMaterial( { color: 0x006985} );
	var material_Ag = new THREE.MeshPhongMaterial( { color: 0xC0C0C0} );
	var material_Pt = new THREE.MeshPhongMaterial( { color: 0xD0D0E0} );
	var material_Au = new THREE.MeshPhongMaterial( { color: 0xDAA520} );

	var atom_array = []
	// for (i = 0; i < input_array.length; i ++){
	// 	switch (**future input**){
	// 		Case 0: var sphere = new THREE.Mesh(geometry_Al, material_Al)) ;
	// 		break;
	// 		Case 1: var sphere = new THREE.Mesh(geometry_Ni, material_Ni);
	// 		break;
	// 		Case 2: var sphere = new THREE.Mesh(geometry_Cu, material_Cu);
	// 		break;
	// 		Case 3: var sphere = new THREE.Mesh(geometry_Pd, material_Pd);
	// 		break;
	// 		Case 4: var sphere = new THREE.Mesh(geometry_Ag, material_Ag);
	// 		break;
	// 		Case 5: var sphere = new THREE.Mesh(geometry_Pt, material_Pt);
	// 		break; 
	// 		Case 6: var sphere = new THREE.Mesh(geometry_Au, material_Au);
	// 		break; 
	// 	}

	// }
	// for (i = 0; i < sphere_array.length; i++)
	// {
	// 	sphere = sphere_array[i];
	// 	sphere.position.x = 2.5 - .5 * i;
	// 	sphere.position.y = 0;
	// 	sphere.position.z = 0;
	// 	scene.add(sphere);
	// }

	// var geometry = new THREE.SphereGeometry(1.5, 50, 50);
	// var material = new THREE.MeshPhongMaterial( { color: 0xfdca00 } );

	/*
	var sphere = new THREE.Mesh( geometry_Al, material_Al);
	sphere.position.x = -6;
	sphere.position.y = 0;
	sphere.position.z = 0;
	scene.add( sphere );

	var sphere1 = new THREE.Mesh( geometry_Cu, material_Cu );
	sphere1.position.x = -4;
	sphere1.position.y = 0;
	sphere1.position.z = 0;
	scene.add( sphere1 );

	var sphere2 = new THREE.Mesh( geometry_Ni, material_Ni);
	sphere2.position.x = -2;
	sphere2.position.y = 0;
	sphere2.position.z = 0;
	scene.add( sphere2 );

	var sphere3 = new THREE.Mesh( geometry_Pd, material_Pd);
	sphere3.position.x = 0;
	sphere3.position.y = 0;
	sphere3.position.z = 0;
	scene.add( sphere3 );

	var sphere4 = new THREE.Mesh( geometry_Ag, material_Ag);
	sphere4.position.x = 2;
	sphere4.position.y = 0;
	sphere4.position.z = 0;
	scene.add( sphere4 );

	var sphere5 = new THREE.Mesh( geometry_Pt, material_Pt);
	sphere5.position.x = 4;
	sphere5.position.y = 0;
	sphere5.position.z = 0;
	scene.add( sphere5 );

	var sphere6 = new THREE.Mesh( geometry_Au, material_Au);
	sphere6.position.x = 6;
	sphere6.position.y = 0;
	sphere6.position.z = 0;
	scene.add( sphere6 );

	*/

	camera.position.z = 20;


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
