var DB_ID=0;
var processing=false;
$(document).ready(function(){
  startCheckingForUpdates();
  doneProcessing();
  animate();

  $("#cancel_solution").click(cancelSolution);

  $("#submit_data").click(function(){

    elementOne = $("#element-1").val();
    elementTwo = $("#element-2").val();
    elementThree = $("#element-3").val();
    percentageOne = $("#percentage-1").val();
    percentageTwo = $("#percentage-2").val();
    percentageThree = $("#percentage-3").val();
    algorithm = $("#algorithm").val();
    numberOfAtoms = $("#number-of-atoms").val();

    validateParametersForSubmission(elementOne, elementTwo, elementThree, percentageOne, percentageTwo, percentageThree, algorithm, numberOfAtoms)

  });
  
});

function cancelSolution(){
  if(DB_ID>0){      
    $.ajax({
      url: '/cancel_metalic_problem',
      type: 'POST',
      data: {id: DB_ID},
    })
    .done(function(data) {
      //console.log("success");
      
      //console.log("DB_ID "+DB_ID);
    })
    .fail(function() {
      //console.log("error");
      
    })
    .always(function() {
      //console.log("complete");
    });
  }
  
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

function doneProcessing(){
  processing=false;
  DB_ID=0;

  $("#progbar").fadeOut(500);
  $("#loading").fadeOut(500);
}

function validateParametersForSubmission(elementOne, elementTwo, elementThree, percentageOne, percentageTwo, percentageThree, algorithm, numberOfAtoms){
  if (elementOne == "None" || percentageOne == undefined){
    alert("Please choose a primary element and specify its percentage");
  }
  else if (elementTwo == "None" || percentageTwo == undefined){
    alert("Please choose a second element and specify its percentage.");
  }
  else if (elementThree != "None" && percentageThree == undefined){
    alert("Please specify a percentage for your third element");
  }
  else if (numberOfAtoms == ""){
    alert("Please specify a number of atoms.");
  }
  else{
    if (elementThree == "None"){
      percentageThree = "0";
    }

    if (parseFloat(percentageOne) + parseFloat(percentageTwo) + parseFloat(percentageThree) != 100){
      alert("Please ensure that your percentages add to 100");
    }
    else{
      performAjaxRequest(elementOne, elementTwo, elementThree, percentageOne, percentageTwo, percentageThree, algorithm, numberOfAtoms);
    }
  }
}



function performAjaxRequest(e1, e2, e3, p1, p2, p3, alg, nAtoms){  
  definingString = ""
  numberOfAtoms = parseInt(numberOfAtoms)

  n1 = parseInt(parseInt(nAtoms)*(p1/100));
  n2 = parseInt(parseInt(nAtoms)*(p2/100));
  
  if (e3 != "None"){
    n3 = parseInt(parseInt(nAtoms)*(p3/100));
  }
  else{
    n3 = 0;
  }

  while (n1 + n2 + n3 != numberOfAtoms){
    n1 += 1;
  }

  definingString += e1 + n1 + e2 + n2;
  if (e3 != "None"){
    definingString += e3 + n3;
  }

  pass_info = {data: {"definingString": definingString, "numberOfAtoms": numberOfAtoms}, algorithm: alg}

  $("#progress").css("width",$("#progbar").width());
  $("#loading").css("opacity",1);
  console.log(pass_info);
  $.ajax({
      url: '/pose_metalic_problem',
      type: 'POST',
      data: pass_info,
    })
    .done(function(data) {
      DB_ID=data.databaseId;
      processing=true;
      $("#progbar").fadeIn(500);
      $("#loading").fadeIn(500);
    })
    .fail(function() {
      //alert("The AJAX request to pose the problem has raised an error.");
    });
}

function startCheckingForUpdates(){  
  setTimeout(startCheckingForUpdates,1000);
  if(processing && DB_ID>0){
    $.ajax({
      url: '/retreive_metalic_problem',
      type: 'POST',
      data: {id: DB_ID},
    })
    .done(function(data) {
      provideDataToPage(data);
      $("#statusDone").html(data.statusDone);
      $("#progress").css("width",parseFloat(data.statusDone.substring(0,data.statusDone.indexOf('%')))/100*$("#progbar").width());
      $("#loading").css("opacity",1-parseFloat(data.statusDone.substring(0,data.statusDone.indexOf('%')))/100);
      if(data.done){
        DB_ID=0;
        doneProcessing();
      }
    })
    .fail(function() {
      //alert("The AJAX request to retreive the problem has raised an error");
    });  
  }
}



function provideDataToPage(data){
  answer = data.answer;
  if(answer!=null){
    answer = jQuery.parseJSON( answer );
    if(answer.potentialEnergy!=null){
      $("#potentialEnergy").html("Potential energy: "+Math.floor(answer.potentialEnergy*100)/100);
    }
    atoms = answer.atoms;
    loadSpheres(atoms);
  }
}
