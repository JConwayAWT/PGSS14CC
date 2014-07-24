var processing=false;

$(document).ready(docReady);

function doneProcessing(){
	processing=false;
	DB_ID=0;
	$("#floatingProgressBar").fadeOut(500);
}

function docReady(){

	drawSampleProtein();

	var DB_ID=0;

	var startTime=0;

	$("#submit_data").click(function(){
		getSolution();
	});

	$("#cancel_solution").click(function(){
		cancelSolution();
	});

	getSolutionProgress();

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
	function getSolution(){
		if(processing)return;
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
					$("#output").html(data.answer);
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
}

// chain = {"potentialEnergy": 342, "acids": [{"type": "H", "x": 10, "y": 20}, {"type":"P", "x": 15, "y": 25}, {"type:":"H", "x": 17, "y": 18}]}

function drawSampleProtein(){
	chain = {"potentialEnergy": 342, "acids": [{"type": "H", "x": 100, "y": 200}, {"type":"P", "x": 150, "y": 250}, {"type":"H", "x": 170, "y": 180}, {"type": "H", "x": 100, "y": 123}]}

	var canvas = document.getElementById('protein-canvas');
    var context = canvas.getContext('2d');
	
	context.beginPath();
   	context.moveTo(chain.acids[0]["x"], chain.acids[0]["y"]);   
    for (i = 0; i < chain.acids.length; i++)
    {
    	buildAminoAcid(chain.acids[i]["type"], chain.acids[i]["x"], chain.acids[i]["y"]);
    	if (i > 0) {
    		var previousPoint = i - 1
    		var p = previousPoint
    	   	drawPeptideBonds(chain.acids[p]["x"], chain.acids[p]["y"], chain.acids[i]["x"], chain.acids[i]["y"])
	    }
    	// context.lineTo(chain.acids[i]["x"], chain.acids[i]["y"]);
    	// context.lineWidth = 3
    	// context.strokeStyle = 'blue'
    	// context.stroke();
    }
}

function buildAminoAcid(type, x, y) {
	var canvas = document.getElementById('protein-canvas');
    var context = canvas.getContext('2d');
	var centerX = x;
    var centerY = y;
    var radius = 10;

    context.beginPath();
    context.arc(centerX, centerY, radius, 0, 2 * Math.PI, false);
    if (type == "H") {
    	context.fillStyle = '#ff0000';
    	context.fill();
    }
    else if (type == "P") {
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
	var canvas = document.getElementById('protein-canvas');
    var context = canvas.getContext('2d');

    context.moveTo(x1,y1);
	context.lineTo(x2, y2);
    // context.lineWidth = 3
    // context.strokeStyle = 'blue'
    context.stroke();
}