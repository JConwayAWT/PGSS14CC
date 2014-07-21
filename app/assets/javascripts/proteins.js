var processing=false;

$(document).ready(docReady);

function doneProcessing(){
	processing=false;
	DB_ID=0;
	$("#floatingProgressBar").fadeOut(500);
}

function docReady(){

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