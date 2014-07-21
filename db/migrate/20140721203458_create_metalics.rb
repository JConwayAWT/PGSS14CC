class CreateMetalics < ActiveRecord::Migration
  def self.up
  	create_table :metalics do |t|
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
	drop_table :metalics
  end
end
