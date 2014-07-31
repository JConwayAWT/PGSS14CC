$(document).ready(docReady);

function docReady(){
	var sayingOn=0;
	var sayings = [
					"Creating Algorithms for Traveling, Nanoparticles, and Interactive Proteins",
					"Purrfect TSP, protein folding, and multimetallic optimization solvers",
					"More fun than a dead mouse",
					"All the critics say: meow!",
					"Furst TSP, then the world",
					"We were twine to design better algorithms than brute force",
					"We'll get you the best pawsible solution",
					"We're feline pretty good about our solvers",
					"Do cats have tails? <br> Let's paws and think about it.<br>Do cats make trails?<br>Yeah, they follow the mouse.",
					"Use our solvers - don't wait nine lives waiting for brute force to run",
					"Our paths don't stray from the best",
					"Such cat, very algorithm",
					"Click on one of the tabbies to learn more",
					"Our results are guaranteed never to be catastrophic",
					"A tale of two cities<br>A tale of two kitties<br>A tail of two kitties",
					"We're the best in the category - no question",
					"Have you met our script kitties?",
					"We built our algorithms from scratch"];

	function newSaying(){
		sayingOn++;
		if(sayingOn>=sayings.length){
			sayingOn=0;
		}
		$("#statement").html(sayings[sayingOn]);
	}

	if(document.cookie=="loadedPage"){
		sayingOn=Math.floor(Math.random()*sayings.length);
		newSaying();
	}
	document.cookie="loadedPage";
	
	$('#statement').on('dragstart', function(event) { event.preventDefault(); });

	$("#statement").click(function(event){
		newSaying();
		event.preventDefault();
		return false;
	});
}