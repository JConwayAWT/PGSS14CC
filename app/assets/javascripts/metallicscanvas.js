var sphere_array = [];
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, 720 / 360, 0.1, 10000 );
var content;
var renderer = new THREE.WebGLRenderer();
$(document).ready(function(){
	renderer.setSize( 720, 360 );
	$("input#slider-goes-here").slider();
	$("#metallics-canvas").html( renderer.domElement );
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

	}
	render();

	var dragging=null;
	var dragY=0;
	var dragX=0;

	$("#metallics-canvas").mousedown(function(e) {
		dragging=$(this);
		dragY=e.pageY-parseInt(dragging.parent().css('top'));
		dragX=e.pageX-parseInt(dragging.parent().css('left'));
	});


	$(window).mouseup(function(e) {
		dragging=null;
	});

	$(window).mousemove(function(e) {
		if(dragging!=null){
			var dispY=e.pageY-dragY;
			var dispX=e.pageX-dragX;
			dragY=e.pageY;
			dragX=e.pageX;
			if(!isNaN(dispY)){		
				content.rotation.x+=parseFloat(dispY)*.01;
				content.rotation.y+=parseFloat(dispX)*.01;
			}
		}
	});
});
function centerSpheres(){
	minX=999999;
	minY=999999;
	minZ=999999;
	maxX=-999999;
	maxY=-999999;
	maxZ=-999999;
	for(var i=0;i<atoms.length;i++){
		minX=Math.min(atoms[i].x,minX);
	    minY=Math.min(atoms[i].y,minY);
	    minZ=Math.min(atoms[i].z,minZ);

	    maxX=Math.max(atoms[i].x,maxX);
	    maxY=Math.max(atoms[i].y,maxY);
	    maxZ=Math.max(atoms[i].z,maxZ);
  	}
  	for(var i=0;i<atoms.length;i++){
		atoms[i].x-=minX+(maxX-minX)/2;
		atoms[i].y-=minY+(maxY-minY)/2;
		atoms[i].z-=minZ+(maxZ-minZ)/2;

  	}
}
function loadSpheres(atoms){
	centerSpheres();	
	scene.remove(content);
	if(content==null){
		content =  new THREE.Object3D();
	}else{
		oldcontent = content;
		content =  new THREE.Object3D();
		content.rotation.x = oldcontent.rotation.x;
		content.rotation.y = oldcontent.rotation.y;
	}
	var geometry_Al = new THREE.SphereGeometry(1.25, 50, 50);
	var geometry_Ni = new THREE.SphereGeometry(1.35, 50, 50);
	var geometry_Cu = new THREE.SphereGeometry(1.35, 50, 50);
	var geometry_Pd = new THREE.SphereGeometry(1.4, 50, 50);
	var geometry_Ag = new THREE.SphereGeometry(1.6, 50, 50);
	var geometry_Pt = new THREE.SphereGeometry(1.35, 50, 50);
	var geometry_Au = new THREE.SphereGeometry(1.35, 50, 50);

	var material_Al = new THREE.MeshPhongMaterial( { color: 0xDDE0EB} );
	var material_Ni = new THREE.MeshPhongMaterial( { color: 0x7FB598} );
	var material_Cu = new THREE.MeshPhongMaterial( { color: 0xC88033} );
	var material_Pd = new THREE.MeshPhongMaterial( { color: 0xAB8FB5} );
	var material_Ag = new THREE.MeshPhongMaterial( { color: 0x8694BD} );
	var material_Pt = new THREE.MeshPhongMaterial( { color: 0xABAD7B} );
	var material_Au = new THREE.MeshPhongMaterial( { color: 0xBDC23E} );

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
	    content.add(sphere);
	    console.log("add sphere "+i);
  	}
  	scene.add(content);
}

$('camera').slider({
	formater: function(value){
		camera.position.z = value * 5;
		return 'Current Camera Position: ' + value;
	}
});
