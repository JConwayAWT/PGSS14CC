$(document).ready(docReady);

function docReady(){
	var sayings = ["Purrfect TSP, protein folding, and multimetallic optimization solvers",
					"More fun than a dead mouse",
					"All the critics say: meow!",
					"Furst TSP, then the world",
					"We were twined to solve problems"];

	$("#statement").html(sayings[Math.floor(Math.random()*sayings.length)]);
	animate();
	function animate(){
		setTimeout(animate,50);
	}
}
