class TravelingSalesman < ActiveRecord::Base
	def pose_problem
		my_id = self.id
		puts my_id
	    python_output = `python lib/python/tsp/TravelingSalesmanCanvas.py #{ENV["RAILS_ENV"]} #{my_id}`
	    puts "RAN"
	    puts python_output
	    puts "OUT"
	    #returnData = {statusMessage: "Processed", pythonOutput: python_output, algorithm: params[:algorithm]}
	end
end
