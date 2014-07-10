class CreateTravelingSalesmen < ActiveRecord::Migration
  def change
    create_table :traveling_salesmen do |t|

      t.timestamps
    end
  end
end
