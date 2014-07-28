var processing=false;
var DB_ID=0;
var startTime=0;


$(document).ready(docReady);

function doneProcessing(){
	processing=false;
	DB_ID=0;
	$("#floatingProgressBar").fadeOut(500);
}


function docReady(){

	getSolutionProgress();

	animate();
	$("#cancel_solution").click(function(){
		cancelSolution();
	});

	$("#random_string").click(function(){
		randomString();
	});


}

function animate(){

	setTimeout(animate,50);

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

function randomString(){
	var n=0;
	var notNum=false;
	while(true){
		s=prompt("How many amino acids do you want to be added? \n\n"+(notNum?"You must enter a number!":""));
		if(s==null||s==""){
			break;
		}
		n=parseInt(s);
		if(s==n+""){
			var value="";
			for(var i=0;i<n;i++){
				value+=(Math.random()<.5?"H":"P");
			}
			$("#data").val(value);
			break;
		}
		notNum=true;
	}
}

function cancelSolution(){
	if(DB_ID>0){			
		$.ajax({
			url: '/cancel_protein_problem',
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

function getSolutionProgress(){		
	setTimeout(getSolutionProgress,1000);
	if(DB_ID>0){
		$.ajax({
			url: '/retreive_protein_problem',
			type: 'POST',
			data: {id: DB_ID},
		})
		.done(function(data) {
			console.log(data);
			console.log(data.answer);
			console.log(data.message);
			console.log(data.statusDone);
			console.log(data.done)
			if(data.answer!=null&&data.answer!=""){
				//answer
				//$("#output").html(data.answer);
				drawSampleProtein(JSON.parse(data.answer));
			}
			if(data.done){
				DB_ID=0;
				doneProcessing();
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


// chain = {"potentialEnergy": 342, "acids": [{"type": "H", "x": 10, "y": 20}, {"type":"P", "x": 15, "y": 25}, {"type:":"H", "x": 17, "y": 18}]}

function drawSampleProtein(chain){
//	chain = {"potentialEnergy": 342, "acids": [{"type": "H", "x": 100, "y": 200}, {"type":"P", "x": 150, "y": 250}, {"type":"H", "x": 170, "y": 180}, {"type": "H", "x": 100, "y": 123}]}
	
	var minimumX = 0;
	var minimumY = 0;
	var maximumX = 1;
	var maximumY = 1;
	var padding = 50;

	for (i = 0; i < chain.acids.length; i++)
    {
    	if (chain.acids[i]["x"] < minimumX) {
    		minimumX = chain.acids[i]["x"];
    	}
    }
    for (i = 0; i < chain.acids.length; i++)
    {
    	chain.acids[i]["x"] = chain.acids[i]["x"] - minimumX;
    }

    for (i = 0; i < chain.acids.length; i++)
    {
    	if (chain.acids[i]["y"] < minimumY) {
    		minimumY = chain.acids[i]["y"];
    	}
    }
	for (i = 0; i < chain.acids.length; i++)
    {
    	chain.acids[i]["y"] = chain.acids[i]["y"] - minimumY;
    }
	
	for (i = 0; i < chain.acids.length; i++)
    {
    	if (chain.acids[i]["x"] > maximumX) {
    		maximumX = chain.acids[i]["x"];
    	}
    }

    for (i = 0; i < chain.acids.length; i++)
    {
    	if (chain.acids[i]["y"] > maximumY) {
    		maximumY = chain.acids[i]["y"];
    	}
    }

    loadSpheres(chain.acids,maximumX,maximumY);

	var canvas = document.getElementById('protein-canvas');
    var context = canvas.getContext('2d');
	context.clearRect(0,0,canvas.width,canvas.height);
	//console.log(maximumX+" "+maximumY);
    //console.log( (canvas.width-padding*2)+" "+ (canvas.height-padding*2));

    $("#current-potential-energy").html(chain.potentialEnergy);

	context.beginPath();
   	context.moveTo(chain.acids[0]["x"], chain.acids[0]["y"]);   
    for (i = 0; i < chain.acids.length; i++)
    {
    	buildAminoAcid(chain,chain.acids[i]["type"], padding+chain.acids[i]["x"]* (canvas.width-padding*2)/maximumX, padding+chain.acids[i]["y"]* (canvas.height-padding*2)/maximumY);
    	if (i > 0) {
    		var previousPoint = i - 1;
    		var p = previousPoint;

    	   	drawPeptideBonds(padding+chain.acids[p]["x"] * (canvas.width-padding*2)/maximumX, padding+chain.acids[p]["y"] * (canvas.height-padding*2)/maximumY, padding+chain.acids[i]["x"]* (canvas.width-padding*2)/maximumX, padding+chain.acids[i]["y"] * (canvas.height-padding*2)/maximumY);
	    }
    	// context.lineTo(chain.acids[i]["x"], chain.acids[i]["y"]);
    	// context.lineWidth = 3
    	// context.strokeStyle = 'blue'
    	// context.stroke();
    }
}

function buildAminoAcid(chain,type, x, y) {
	var canvas = document.getElementById('protein-canvas');
    var context = canvas.getContext('2d');
	var centerX = x;
    var centerY = y;
    var radius = 10;


    if (chain.acids.length > 10){
     	radius = 5;
    }
    else if (chain.acids.length > 20){
     	radius = 2;
    }
    else if (chain.acids.length > 50){
    	radius = 1;
    }
    else if (chain.acids.length > 100){
    	radius = 0.5;
    }

    context.beginPath();
    context.arc(centerX, centerY, radius, 0, 2 * Math.PI, false);
    if (type == "H"||type=="h") {
    	context.fillStyle = '#ff0000';
    	context.fill();
    }
    else if (type == "P"||type=="p") {
    	context.fillStyle = '#00ff00';
    	context.fill();
    }
    // context.fillStyle = 'green';
    // context.fill();
    // context.lineWidth = 1;
    // context.strokeStyle = '#003300';
    context.stroke();
    }

function drawPeptideBonds(x1,y1,x2,y2) {
	console.log(x1,y1,x2,y2);
	var canvas = document.getElementById('protein-canvas');
    var context = canvas.getContext('2d');

    context.moveTo(x1,y1);
	context.lineTo(x2, y2);
    // context.lineWidth = 3
    // context.strokeStyle = 'blue'
    context.stroke();
}

function getSolution(){
	if(processing)return false;
	var xvalues =[];
	var yvalues=[];		
	processing=true;

	var data=$("#data").val();
	var algorithm=$("#algorithm").val();
	startTime= (new Date().getTime());
	$.ajax({
		url: '/pose_protein_problem',
		type: 'POST',
		data: {data: data, algorithm: algorithm},
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
	
	return false;
}
