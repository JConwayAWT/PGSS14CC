class AddSolverTimeout < ActiveRecord::Migration
   def self.up
  	change_table :traveling_salesmen do |t|
      t.integer :lastTick      
    end
  end
  def self.down	
	remove_column :lastTick	
  end
end
