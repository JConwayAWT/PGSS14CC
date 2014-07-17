class AddSolverTimeout < ActiveRecord::Migration
   def self.up
  	change_table :traveling_salesmen do |t|
      t.integer :last_tick      
    end
  end
  def self.down	
	remove_column :traveling_salesmen, :last_tick	
  end
end
