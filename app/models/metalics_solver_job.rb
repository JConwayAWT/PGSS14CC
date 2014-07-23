class MetalicsSolverJob
  include SuckerPunch::Job

  def perform(id)
    ActiveRecord::Base.connection_pool.with_connection do
      u = Metalics.find(id)
      u.pose_problem
    end
  end
end