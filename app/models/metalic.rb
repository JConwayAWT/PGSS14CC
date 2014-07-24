class Metalic < ActiveRecord::Base
	def pose_problem
		my_id = self.id

	    python_output = `python lib/python/multimetallics/MetalicsCanvas.py #{ENV["RAILS_ENV"]} #{my_id}`
	end
end
