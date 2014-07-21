class AddProteinInfo < ActiveRecord::Migration
  def self.up
  	change_table :proteins do |t|
      t.text :problem_parameters   
      t.text :algorithm
      t.text :answer
      t.text :message
      t.text :statusdone
      t.boolean :done
      t.integer :last_tick
    end
  end
  def self.down
	remove_column :protein, :problem_parameters
	remove_column :protein, :algorithm
	remove_column :protein, :answer
	remove_column :protein, :message
	remove_column :protein, :statusdone
	remove_column :protein, :done
	remove_column :protein, :last_tick
  end
end
