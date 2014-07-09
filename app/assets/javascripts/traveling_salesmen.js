var isDown=false;
var x1=0;
var y1=0;

// Draw a circle
$(document).ready(docReady);

function docReady(){

	var canvas=document.getElementById("canvas");
	console.log(canvas);
	var context= canvas.getContext('2d');

	var cords = [];
	var ACCESS_RADIUS=10;
	var removing=false;
	var solution;

	var moving=-1;

	addPoint(100,300);
	addPoint(200,300);
	addPoint(200,400);
	addPoint(100,400);

	animate();

	function animate(){
		context.clearRect(0,0,canvas.width,canvas.height);
		for(var i=0;i<cords.length;i++){
			var cord = cords[i];
			cord.draw();
		}
		drawSolution();
		setTimeout(animate,50);
	}

	$("#traveling-salesman-submit").click(function(){

		var xvalues =[];
		var yvalues=[];

		$("#output").html("Processing...");

		for(var i=0;i<cords.length;i++){
			var cord = cords[i];
			xvalues[xvalues.length]=cord.x;	
			yvalues[yvalues.length]=cord.y;
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
			solution=data.pythonOutput.split(",");
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

	function drawSolution(){
		if(solution!=null){
			p= solution[cords.length-1];
			for(var i=0;i<cords.length;i++){
				context.beginPath();
		    	context.moveTo(cords[p].x, cords[p].y);
		    	context.lineTo(cords[solution[i]].x, cords[solution[i]].y);
		    	context.stroke();
		    	p=solution[i];
			}
		}
	}

	$("#canvas").on('mousemove', function(e){
		var x=e.pageX - $("#canvas").offset().left;
		var y=e.pageY - $("#canvas").offset().top;
		

		if(moving>=0){
			console.log(moving+" "+x+" "+y+" "+cords[moving]);
			cords[moving].setX(x);
			cords[moving].setY(y);
		}
	});



	$("#canvas").on('mousedown', function(e){
		var x=e.pageX - $("#canvas").offset().left;
		var y=e.pageY - $("#canvas").offset().top;

		solution=null;

		var accessed=false;

		for(var i=0;i<cords.length;i++){
			var cord = cords[i];
			if(cord.getDist(x,y)<ACCESS_RADIUS){
				if(removing){
					cords.splice(i,1);
					i--;	
				}else{
					cord.moving=true;
					moving=i;
				}
				accessed=true;
			}
		}

		if(!accessed&&!removing){
			moving=cords.length;
			addPoint(x,y).moving=true;

		}
	});

	$("#canvas").on('mouseup', function(e){
		var x=e.pageX - $("#canvas").offset().left;
		var y=e.pageY - $("#canvas").offset().top;
		
		solution=null;

		for(var i=0;i<cords.length;i++){
			var cord = cords[i];
			if(cord.getDist(x,y)<ACCESS_RADIUS){
				cord.moving=false;
				moving=-1;
			}
		}
	});




	function addPoint(x, y){
		var c = new Coordinate(x,y);
		cords[cords.length]=c;
		return c;
	}

function Coordinate(x,y){
	this.x=x;
	this.y=y;
	this.moving=false;
	this.setX = function (x){
		this.x=x;
		console.log(x);
	}
	this.setY = function (y){
		this.y=y;
	}
	this.getDist= function(px,py){
		return Math.sqrt(Math.pow(px-this.x,2)+Math.pow(py-this.y,2));
	}
	this.draw = function(){
		context.beginPath();
		context.arc(this.x, this.y, 5, 0, 2 * Math.PI, false);
		context.fillStyle = this.moving?'red':'green';
		context.fill();
		context.stroke();
	}
}



}
