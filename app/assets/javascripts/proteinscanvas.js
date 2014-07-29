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
//    		content.rotation.x+=.01;	
    		//content.rotation.y+=.01
    		//content.rotation.y+=.1;	
    	}
	}
	render();


	var dragging=null;
	var dragY=0;
	var dragX=0;

	$("#canvas3d").mousedown(function(e) {
		dragging=$(this);
		dragY=e.pageY;
		dragX=e.pageX;
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

function loadSpheres(acids,maximumX,maximumY){
	scene.remove(content);
	if(content==null){
		content =  new THREE.Object3D();
	}else{
		oldcontent = content;
		content =  new THREE.Object3D();
		content.rotation.x = oldcontent.rotation.x;
		content.rotation.y = oldcontent.rotation.y;
	}
	var geometry = new THREE.SphereGeometry(.25, 50, 50);
	var red = new THREE.MeshPhongMaterial( { color: 0xff0000} );
	var green = new THREE.MeshPhongMaterial( { color: 0x00ff00} );
	var white = new THREE.MeshPhongMaterial( { color: 0xffffff} );

	var points = new THREE.Geometry();

  	for(var i=0;i<acids.length;i++){	    
  		color = white;
	    if(acids[i].type=="H"||acids[i].type=="h"){color=red;}
	    if(acids[i].type=="P"|acids[i].type=="p"){color=green;}

	    if(isNaN(acids[i].z)){
	    	acids[i].z=0;
	    }

		var sphere = new THREE.Mesh(geometry, color) ;
		sphere.position.x=acids[i].x-maximumX/2;
	    sphere.position.y=acids[i].y-maximumY/2;
	    sphere.position.z=acids[i].z;

	    points.vertices.push( sphere.position );
	    content.add(sphere);	    
  	}

  	var line = new THREE.Line( points, new THREE.LineBasicMaterial( { color: 0xffffff, opacity: 0.5 } ) );
	content.add( line);

	scene.add(content);
}