$(document).ready(function(){
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

      if (parseInt(percentageOne) + parseInt(percentageTwo) + parseInt(percentageThree) != 100){
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
  definingString += e1 + parseInt(parseInt(nAtoms) * parseInt(p1)/100) + e2 + parseInt(parseInt(nAtoms) * parseInt(p2)/100);
  if (e3 != "None"){
    definingString += e3 + parseInt(parseInt(nAtoms) * parseInt(p3)/100);
  }

  pass_info = {data: {"definingString": definingString, "numberOfAtoms": numberOfAtoms}, algorithm: alg}
  console.log(pass_info);

  $.ajax({
      url: '/pose_metalic_problem',
      type: 'POST',
      data: pass_info,
    })
    .done(function(data) {
      startCheckingForUpdates(data.databaseId);
    })
    .fail(function() {
      console.log("Failed =(");
    })
    .always(function() {
      console.log("complete");
    });
}

function startCheckingForUpdates(databaseId){
  retreiveProblemInterval = setInterval(retreiveProteinProblem(databaseId), 3000);
}

function retreiveProteinProblem(id){
  $.ajax({
    url: '/retreive_metalic_problem',
    type: 'POST',
    data: {id: id},
  })
  .done(function(data) {
    provideDataToPage(data);
  })
  .fail(function() {
    alert("Something went wrong...");
  });
}

function provideDataToPage(data){
  answer = data.answer;
  $("#display-answer").show();
  $("#display-answer").text(answer);
}