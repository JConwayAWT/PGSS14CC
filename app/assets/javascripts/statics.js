$(document).ready(docReady);

function docReady(){
	var sayings = ["Purfect TSP, protein folding, and multimetallic optimization solvers",
					"More fun than a dead mouse",
					"All the critics say: meow!"];

	$("#statement").html(sayings[Math.floor(Math.random()*sayings.length)]);
}