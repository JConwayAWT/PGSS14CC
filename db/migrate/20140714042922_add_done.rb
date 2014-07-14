class AddDone < ActiveRecord::Migration
  def self.up
  	change_table :traveling_salesmen do |t|
      t.boolean :done      
    end
  end
  def self.down
	
	remove_column :done, :answer	

  end
end
