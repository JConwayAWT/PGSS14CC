class TspRemoveLineCrossings < ActiveRecord::Migration
  def self.up
  	change_table :traveling_salesmen do |t|
      t.boolean :remove_overlaps
    end
  end
  def self.down
	remove_column :traveling_salesmen, :remove_overlaps
  end
end
