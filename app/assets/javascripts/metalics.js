$(document).ready(function(){
  $("#submit_data").click(function(){
    $.ajax({
      url: '/pose_metalic_problem',
      type: 'POST',
      data: {data: {"atoms": [{"x": 1, "y": 2, "z": 3, "symbol": "Pt"}], algorithm: "Alg A"}},
    })
    .done(function(data) {
      console.log(data.statusMessage);
    })
    .fail(function() {
      console.log("Failed =(");
    })
    .always(function() {
      console.log("complete");
    });
    
  });
});