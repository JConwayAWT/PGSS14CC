var isDown=false;
var x1=0;
var y1=0;

// Draw a circle
$(document).ready(docReady);

function docReady(){

	$("#traveling-salesman-submit").click(function(){

		points = {x: 1, y: 2};

		$.ajax({
			url: '/pose_traveling_salesman_problem',
			type: 'POST',
			data: {points: points},
		})
		.done(function(data) {
			console.log("success");
			$("#output").html(data.pythonOutput);
		})
		.fail(function() {
			console.log("error");
		})
		.always(function() {
			console.log("complete");
		});
		
	});

	$("canvas").drawArc({	
	  fillStyle: "green",
	  draggable: true,
	  x: 100, y: 100,
	  radius: 50
	});

	$("canvas").on('mousedown', function(e){
	    if (isDown === false) {

	        isDown = true;

	        /*var pos = getMousePos(canvas, e);
	        x1 = pos.x;
	        y1 = pos.y;
	        */
	    }
	});
}

