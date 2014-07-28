var sphere_array = [];
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, 720 / 360, 0.1, 10000 );
var content;
var renderer = new THREE.WebGLRenderer();
$(document).ready(function(){
	renderer.setSize( 720, 360 );
	$("input#slider-goes-here").slider();
	$("#canvas3d").html( renderer.domElement );
	camera.position.z = 25;
	
	$("input#slider-goes-here").on('slide', function() {
		camera.position.z = 50 - $("input#slider-goes-here").slider('getValue');
	});

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
    	//camera.rotateOnAxis((new THREE.Vector3(0, 1, 0)).normalize(), degInRad(100));
    	if (content!=null){
    		content.rotation.x+=.1;	
    		content.rotation.y+=.1;	
    	}
	}
	render();

});

function loadSpheres(acids){
	scene.remove(content);
	content =  new THREE.Object3D();
	sphere_array=[];
	var geometry = new THREE.SphereGeometry(.25, 50, 50);
	var material = new THREE.MeshPhongMaterial( { color: 0xBFA6A6} );

	var points = new THREE.Geometry();


  	for(var i=0;i<acids.length;i++){
	    console.log(acids[i]);
		var sphere = new THREE.Mesh(geometry, material) ;
		sphere.position.x=acids[i].x;
	    sphere.position.y=acids[i].y;
	    sphere.position.z=acids[i].z;
	    points.vertices.push( sphere.position );
	    
	    sphere_array.push(sphere);
	    content.add(sphere);
	    console.log("add sphere "+i+" "+acids[i].x+" "+acids[i].y+" "+acids[i].z);
  	}

  	var line = new THREE.Line( points, new THREE.LineBasicMaterial( { color: 0xffffff, opacity: 0.5 } ) );
	content.add( line);

	scene.add(content);
}

/*
$('camera').slider({
	formater: function(value){
		camera.position.x = value * 5;
		return 'Current Camera Position: ' + value;
	}
});
*/