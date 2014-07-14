class AddProgressUpdates < ActiveRecord::Migration
  def self.up
  	change_table :traveling_salesmen do |t|
      t.text :answer
      t.text :message
      t.text :statusdone
    end
  end
  def self.down
	
	remove_column :traveling_salesmen, :answer
	remove_column :traveling_salesmen, :message
	remove_column :traveling_salesmen, :statusdone

  end
end
