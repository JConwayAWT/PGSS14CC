var isDown=false;
var x1=0;
var y1=0;

// Draw a circle
$(document).ready(docReady);

function docReady(){

	var cords = [];
	var ACCESS_RADIUS=10;
	var removing=false;

	$("#traveling-salesman-submit").click(function(){

		var xvalues =[5,4];
		var yvalues=[3,3];
		var points = {x: xvalues, y: yvalues};

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

	$(document).keydown(function(event) {
		if(event.which==65){
			removing=true;
		}
	});

	$(document).keyup(function(event) {
		if(event.which==65){
			removing=false;
		}
	});

	$("canvas").on('mousedown', function(e){
		var x=e.pageX - $('canvas').offset().left;
		var y=e.pageY - $('canvas').offset().top;
		console.log("pressed",x,y);
	
		var accessed=false;

		for(var i=0;i<cords.length;i++){
			var cord = cords[i];
			if(cord.getDist(x,y)<ACCESS_RADIUS){
				cord.layer.fillStyle="red";
				if(removing){
					cords.splice(i,1);
					$('canvas').removeLayer(cord.layer);
					i--;	
				}
				accessed=true;
			}
		}

		if(!accessed&&!removing){
			addPoint(x,y);
		}
	});

	function addPoint(x, y){
		var point = $("canvas").drawArc({	
		  fillStyle: "green",
		  draggable: true,
		  x: x, y: y,
		  radius: 5
		});
		var c = new Coordinate(x,y,$('canvas').getLayer(-1));
		cords[cords.length]=c;
	}
}

function Coordinate(x, y,l){
	this.x=x;
	this.y=y;
	this.layer=l;
	this.getDist= function(px,py){
		return Math.sqrt(Math.pow(px-x,2)+Math.pow(py-y,2));
	}
}


