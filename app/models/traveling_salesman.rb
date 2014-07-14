class TravelingSalesman < ActiveRecord::Base
	def pose_problem
		my_id = self.id

	    python_output = `python lib/python/tsp/TravelingSalesmanCanvas.py #{ENV["RAILS_ENV"]} #{my_id}`

	    #returnData = {statusMessage: "Processed", pythonOutput: python_output, algorithm: params[:algorithm]}
	end
end
