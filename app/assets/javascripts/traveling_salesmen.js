var isDown=false;
var x1=0;
var y1=0;

// Draw a circle
$(document).ready(docReady);

function docReady(){

	var cords = [];
	var ACCESS_RADIUS=10;
	var removing=false;
	var displayedSolution;

	addPoint(100,300);
	addPoint(200,300);
	addPoint(200,400);
	addPoint(100,400);

	$("#traveling-salesman-submit").click(function(){

		var xvalues =[];
		var yvalues=[];

		$("#output").html("Processing...");

		for(var i=0;i<cords.length;i++){
			var cord = cords[i];
			xvalues[xvalues.length]=cord.x();	
			yvalues[yvalues.length]=cord.y();
		}
		var points = {x: xvalues, y: yvalues};

		$.ajax({
			url: '/pose_traveling_salesman_problem',
			type: 'POST',
			data: {points: points},
		})
		.done(function(data) {
			console.log("success");
			$("#output").html(data.pythonOutput);
			drawSolution(data.pythonOutput);
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

	function drawSolution(solutionText){
		solution=solutionText.split(",");
		p= solution[cords.length-1];

		displayedSolution = {
		  strokeStyle: '#000',
		  strokeWidth: 2,
		   strokeDash: [5],
  			strokeDashOffset: 0,
		  rounded: true,
		  closed: true
		};

		for(var i=0;i<cords.length;i++){
			displayedSolution['x'+(i+1)] = cords[solution[i]].x();
		  	displayedSolution['y'+(i+1)] = cords[solution[i]].y();			
		}
		$('canvas').drawLine(displayedSolution);
	}


	$("canvas").on('mousedown', function(e){
		var x=e.pageX - $('canvas').offset().left;
		var y=e.pageY - $('canvas').offset().top;

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

	$("canvas").on('mouseup', function(e){
		var x=e.pageX - $('canvas').offset().left;
		var y=e.pageY - $('canvas').offset().top;
		console.log("pressed",x,y);
		for(var i=0;i<cords.length;i++){
			var cord = cords[i];
			if(cord.getDist(x,y)<ACCESS_RADIUS){
				cord.layer.fillStyle="green"; 
			}
		}
	});




	function addPoint(x, y){
		var point = $("canvas").drawArc({	
		  fillStyle: "red",
		  draggable: true,
		  x: x, y: y,
		  radius: 5
		});
		var c = new Coordinate($('canvas').getLayer(-1));
		cords[cords.length]=c;
	}
}

function Coordinate(l){
	this.layer=l;
	this.x = function(){
		return this.layer.x;
	}
	this.y = function(){
		return this.layer.y;
	}
	this.getDist= function(px,py){
		return Math.sqrt(Math.pow(px-this.x(),2)+Math.pow(py-this.y(),2));
	}
}


