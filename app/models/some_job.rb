class SomeJob
  include SuckerPunch::Job

  def perform
    sleep 10
    ActiveRecord::Base.connection_pool.with_connection do
      u = User.first
      u.first_name = Kernel.rand().to_s
      u.save!
    end
  end
end