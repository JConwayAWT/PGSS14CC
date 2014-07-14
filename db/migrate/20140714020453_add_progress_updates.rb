class AddProgressUpdates < ActiveRecord::Migration
  def self.up
  	change_table :traveling_salesmen do |t|
      t.text :answer
      t.text :message
      t.text :statusDone
    end
  end
end
