class AddAlgorithmToTspDatabase < ActiveRecord::Migration
  def self.up
  	change_table :traveling_salesmen do |t|
      t.text :algorithm
    end
  end

  def self.down
  end
end
