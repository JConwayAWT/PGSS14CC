class AddParametersToTravelingSalesmen < ActiveRecord::Migration
  def change
  	change_table :traveling_salesmen do |t|
  		t.text :problem_parameters
   	end
  end
end
