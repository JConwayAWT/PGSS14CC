var sphere_array = [];
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, 720 / 360, 0.1, 10000 );

var renderer = new THREE.WebGLRenderer();
$(document).ready(function(){
	renderer.setSize( 720, 360 );
	$("input#slider-goes-here").slider();
	$("#metallics-canvas").html( renderer.domElement );
	camera.position.z = 25;
	
	$("input#slider-goes-here").on('slide', function() {
		camera.position.z = 50 - $("input#slider-goes-here").slider('getValue');
	});


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

	scene.add(camera);
	var pointLight = new THREE.PointLight( 0xFFFFFF );

	// set its position
	pointLight.position.x = 0;
	pointLight.position.y = 0;
	pointLight.position.z = 15;

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

  	for(var i=0;i<atoms.length;i++){
	    console.log(atoms[i]);
    	switch (atoms[i].symbol){
			case "Al":
			var sphere = new THREE.Mesh(geometry_Al, material_Al) ;
			break;
			case "Ni":
			var sphere = new THREE.Mesh(geometry_Ni, material_Ni);
			break;
			case "Cu":
			var sphere = new THREE.Mesh(geometry_Cu, material_Cu);
			break;
			case "Pd":
			var sphere = new THREE.Mesh(geometry_Pd, material_Pd);
			break;
			case "Ag":
			var sphere = new THREE.Mesh(geometry_Ag, material_Ag);
			break;
			case "Pt":
			var sphere = new THREE.Mesh(geometry_Pt, material_Pt);
			break; 
			case "Au":
			var sphere = new THREE.Mesh(geometry_Au, material_Au);
			break; 
		}
		sphere.position.x=atoms[i].x;
	    sphere.position.y=atoms[i].y;
	    sphere.position.z=atoms[i].z;
	    sphere_array.push(sphere);
	    scene.add(sphere);
	    console.log("add sphere "+i);
  	}
}

$('camera').slider({
	formater: function(value){
		camera.position.z = value * 5;
		return 'Current Camera Position: ' + value;
	}
});
