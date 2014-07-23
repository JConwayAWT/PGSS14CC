$(document).ready(docReady);

function docReady(){
	var sayings = [
					"Creating Algorithms for Traveling, Nanoparticles, and Interactive Proteins",
					"Purrfect TSP, protein folding, and multimetallic optimization solvers",
					"More fun than a dead mouse",
					"All the critics say: meow!",
					"Furst TSP, then the world",
					"We were twined to design better algorithms than brute force",
					"We'll get you the best pawsible solution",
					"We're feline pretty good about our solvers",
					"Do cats have tails? <br> Lets paws and think about it.<br>Do cats make trails?<br>Yeah, they follow the mouse.",
					"Use our solvers - don't wait nine lives waiting for brute force to run",
					"Our paths don't stray from the best",
					"Such cat, very algorithm",
					"Click on one of the tabbies to learn more",
					"Our results are guaranteed to never be catastrophic"];

	function newSaying(){
		$("#statement").html(sayings[Math.floor(Math.random()*sayings.length)]);
	}

	newSaying();

	$("#statement").click(newSaying);
}
