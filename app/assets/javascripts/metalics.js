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
      alert("The AJAX request to pose the problem has raised an error.");
    });
}

function startCheckingForUpdates(databaseId){
  retreiveProblemInterval = setInterval(function(){
    $.ajax({
      url: '/retreive_metalic_problem',
      type: 'POST',
      data: {id: databaseId},
    })
    .done(function(data) {
      provideDataToPage(data);
    })
    .fail(function() {
      alert("The AJAX request to retreive the problem has raised an error");
    });
  }, 3000);
}

function provideDataToPage(data){
  answer = data.answer;
  $("#display-answer").show();
  $("#answer-goes-here").text(answer);
}


function webGLStart() {
      from: 'ids',
  PhiloGL('lesson01-canvas', {
    program: {
      vs: 'shader-vs',
      fs: 'shader-fs'
    },
    onError: function() {
      alert("An error ocurred while loading the application");
    },
    onLoad: function(app) {
      var gl = app.gl,
          canvas = app.canvas,
          program = app.program,
          camera = app.camera;
 
      gl.viewport(0, 0, canvas.width, canvas.height);
      gl.clearColor(0, 0, 0, 1);
      gl.clearDepth(1);
      gl.enable(gl.DEPTH_TEST);
      gl.depthFunc(gl.LEQUAL);
 
      program.setBuffers({
        'triangle': {
          attribute: 'aVertexPosition',
          value: new Float32Array([0, 1, 0, -1, -1, 0, 1, -1, 0]),
          size: 3
        },
        
        'square': {
          attribute: 'aVertexPosition',
          value: new Float32Array([1, 1, 0, -1, 1, 0, 1, -1, 0, -1, -1, 0]),
          size: 3
        }
      });
      
      gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
      camera.view.id();
      //Draw Triangle
      camera.view.$translate(-1.5, 0, -7);
      program.setUniform('uMVMatrix', camera.view);
      program.setUniform('uPMatrix', camera.projection);
      program.setBuffer('triangle');
      gl.drawArrays(gl.TRIANGLES, 0, 3);
      
      //Draw Square
      camera.view.$translate(3, 0, 0);
      program.setUniform('uMVMatrix', camera.view);
      program.setUniform('uPMatrix', camera.projection);
      program.setBuffer('square');
      gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
    }
  });  
}