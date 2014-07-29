var x1=0;
var y1=0;
var jobs=0;
var processing=false;

// Draw a circle
$(document).ready(docReady);

$(window).bind('page:load', function(){
	docReady();
});

function addJob(){
	
	jobs++;
	$("#jobs").prepend("<div id=\"job"+jobs+"\" class=\"job\"></div>");
	$("#job"+jobs).append("<h1>Job "+(jobs)+"</h1>");
	$("#job"+jobs).append("<br>"+$("#algorithm").val());
	if($("#remove_overlaps").is(':checked')){
		$("#job"+jobs).append("<br>Remove Overlaps");
	}
	//$("#job"+jobs).append(" <div class=\"progress\"> <div id=\"progress"+jobs+"\" class=\"progress-bar progress-bar-striped active\"  role=\"progressbar\" aria-valuenow=\"45\" aria-valuemin=\"0\" aria-valuemax=\"100\" style=\"width: 100%\"> <span id=\"statusDone"+jobs+"\">Waiting in queue...</span></div></div>");
	$("#floatingProgressBar").fadeIn(500);
	$("#loading").fadeIn(500);
}

function doneProcessing(){
	processing=false;
	DB_ID=0;
	$("#progress").css("width",$("#floatingProgressBar").width());
	$("#floatingProgressBar").fadeOut(500);
	$("#loading").fadeOut(500);
}

function docReady(){
	var canvas=document.getElementById("canvas");
	//console.log(canvas);
	var context= canvas.getContext('2d');
	context.font="14px Georgia";

	var cords = [];
	var ACCESS_RADIUS=10;
	var removing=false;
	var solution;

	var DB_ID=0;

	var startTime=0;
	var totalDist=0;

	var moving=-1;

	animate();
	getSolutionProgress();
	doneProcessing();

	var dragging=null;
	var dragY=0;
	var dragX=0;
	
	addRandomCoordinates(10);

	$(".handle").mousedown(function(e) {
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

			if(dispY<70)dispY=70;
			var bottomY=$(window).height()-dragging.parent().height();
			if(dispY>bottomY)dispY=bottomY;

			var rightX=$(window).width()-dragging.parent().width();
			if(dispX>rightX)dispX=rightX;
			if(dispX<0)dispX=0;
			
			dragging.parent().css('top',dispY);
			dragging.parent().css('left',dispX);
		}
	});
	

	function addRandomCoordinates(numCords){
		solution="";
		for(var i=0;i<numCords;i++){
			var c = new Coordinate(500+Math.random()*500,60+Math.random()*500,cords.length);
			cords[cords.length]=c;
		}
	}

	function animate(){

		setTimeout(animate,50);

		context.canvas.width=innerWidth-20;
		context.canvas.height=innerHeight-20;

		$("#jobs").height(innerHeight-250);

		context.clearRect(0,0,canvas.width,canvas.height);
		for(var i=0;i<cords.length;i++){
			var cord = cords[i];
			cord.draw();
		}
		drawSolution();
		
		//canvas.width=window.innerWidth-200;
		$("#submit_data").prop('disabled', processing);
		$("#cancel_solution").prop('disabled', !processing);
		$("#remove_all_datapoints").prop('disabled', processing);
		$("#add_random_points").prop('disabled', processing);


		if(processing){
			$("#submit_data").hide();
			$("#cancel_solution").show();
		}else{
			$("#submit_data").show();
			$("#cancel_solution").hide();
		}
	}

	$("#submit_data").click(getSolution);
	$("#cancel_solution").click(cancelSolution);
	$("#remove_all_datapoints").click(removeData);
	$("#add_random_points").click(addRandPoints);

	function removeData(){
		if(processing)return;
		if(confirm("Erase all points?")){
			cords=[];
		}
	}

	function addRandPoints(){
		if(processing)return;
		var n=0;
		var notNum=false;
		while(true){
			s=prompt("How many points do you want to be added? \n\n"+(notNum?"You must enter a number!":""));
			if(s==null||s==""){
				break;
			}
			n=parseInt(s);
			if(s==n+""){
				addRandomCoordinates(n);
				break;
			}
			notNum=true;
		}
	}

	function cancelSolution(){
		if(DB_ID>0){			
			$.ajax({
				url: '/cancel_traveling_salesman_problem',
				type: 'POST',
				data: {id: DB_ID},
			})
			.done(function(data) {
				//console.log("success");
				
				//console.log("DB_ID "+DB_ID);
			})
			.fail(function() {
				//console.log("error");
				doneProcessing();
			})
			.always(function() {
				//console.log("complete");
			});
		}
		
	}
	function getSolution(){
		if(processing)return;
		if(cords.length==0){
			alert("You must add some points!");
			return;
		}
		var xvalues =[];
		var yvalues=[];

		//$("#output").html("Waiting in queue...");
		processing=true;

		addJob();

		for(var i=0;i<cords.length;i++){
			var cord = cords[i];
			xvalues[xvalues.length]=cord.x;	
			yvalues[yvalues.length]=cord.y;
		}
		var points = {x: xvalues, y: yvalues};
		var algorithm=$("#algorithm").val();
		var remove_overlaps=$("#remove_overlaps").is(':checked')?"y":"n";

		startTime= (new Date().getTime());
		$.ajax({
			url: '/pose_traveling_salesman_problem',
			type: 'POST',
			data: {points: points, algorithm: algorithm,remove_overlaps: remove_overlaps},
		})
		.done(function(data) {
			//console.log("success");
			DB_ID=data.databaseId;
			//console.log("DB_ID "+DB_ID);
		})
		.fail(function() {
			//console.log("error");
			doneProcessing();
		})
		.always(function() {
			//console.log("complete");
		});
		
	}
	function getSolutionProgress(){		
		setTimeout(getSolutionProgress,1000);
		if(DB_ID>0){
			$.ajax({
				url: '/retreive_traveling_salesman_problem',
				type: 'POST',
				data: {id: DB_ID},
			})
			.done(function(data) {
				console.log(data);
				console.log(data.answer);
				console.log(data.message);
				console.log(data.statusDone);
				console.log(data.done)
				$("#statusDone").html(data.statusDone);
				$("#progress").css("width",parseFloat(data.statusDone.substring(0,data.statusDone.indexOf('%')))/100*$("#floatingProgressBar").width());
				console.log(data.answer);
				if(data.answer!=null&&data.answer!=""){
					//$("#output").html(data.answer);
					if(data.answer.indexOf("ERROR:")==-1){//No error
						var ansStart=data.answer.lastIndexOf(';')+1;
						var ans=data.answer.substring(ansStart)
						solution=ans.split(",");
					}
				}
				if(data.done){
					DB_ID=0;
					doneProcessing();
					$("#job"+jobs).append("<br>Points: "+cords.length);
					$("#job"+jobs).append("<br>Time (s): "+Math.floor((((new Date().getTime())-startTime)/1000)*10)/10);
					calculateTotalDist();
					$("#job"+jobs).append("<br>Total Distance (px): "+Math.floor(totalDist));
				}
			})
			.fail(function() {
				//console.log("error");
			})
			.always(function() {
				//console.log("complete");
			});		
		}
	}

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
	function calculateTotalDist(){
		totalDist=0;
		p= solution[cords.length-1];
		for(var i=0;i<cords.length;i++){
		   	totalDist+=cords[p].getDistCord(cords[solution[i]]);
		   	p=solution[i];	
		}
	}
	function drawSolution(){
		try{
			totalDist=0;
			if(solution!=null){
				p= solution[cords.length-1];
				for(var i=0;i<cords.length;i++){
					context.beginPath();
			    	context.moveTo(cords[p].x, cords[p].y);
			    	context.lineTo(cords[solution[i]].x, cords[solution[i]].y);
			    	context.stroke();
			    	p=solution[i];
			    	totalDist+=cords[p].getDistCord(cords[solution[i]]);
				}
			}
		}catch(err){
			console.log("Draw error "+err);
		}
	}

	$("#canvas").on('mousemove', function(e){
		if(!processing){
			var x=e.pageX - $("#canvas").offset().left;
			var y=e.pageY - $("#canvas").offset().top;
			

			if(moving>=0){
				//console.log(moving+" "+x+" "+y+" "+cords[moving]);
				cords[moving].setX(x);
				cords[moving].setY(y);
			}
		}
	});



	$("#canvas").on('mousedown', function(e){
		if(!processing){
			var x=e.pageX - $("#canvas").offset().left;
			var y=e.pageY - $("#canvas").offset().top;

			solution=null;

			var accessed=false;

			for(var i=0;i<cords.length;i++){
				var cord = cords[i];
				if(cord.getDist(x,y)<ACCESS_RADIUS){
					if(removing){
						cords.splice(i,1);
						for(var j=i;j<cords.length;j++){
							cords[j].i=j;
						}
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
		}
	});

	$("#canvas").on('mouseup', function(e){
		if(!processing){
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
		}
	});




	function addPoint(x, y){
		var c = new Coordinate(x,y,cords.length);
		cords[cords.length]=c;
		return c;
	}

	function Coordinate(x,y,i){
		this.x=x;
		this.y=y;
		this.i=i;
		this.moving=false;
		this.setX = function (x){
			this.x=x;
			//console.log(x);
		}
		this.setY = function (y){
			this.y=y;
		}
		this.getDist= function(px,py){
			return Math.sqrt(Math.pow(px-this.x,2)+Math.pow(py-this.y,2));
		}
		this.getDistCord = function(c){
			return this.getDist(c.x,c.y);
		}
		this.draw = function(){
			var radius=5;
			context.beginPath();
			context.arc(this.x, this.y, radius, 0, 2 * Math.PI, false);
			context.fillStyle = this.moving?'red':'green';
			context.fill();
			context.stroke();
			context.fillStyle='black';
			context.fillText(this.i,this.x+radius,this.y+radius/2); 
		}
	}



}