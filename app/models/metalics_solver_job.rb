class MetalicsSolverJob
  include SuckerPunch::Job

  def perform(id)
    ActiveRecord::Base.connection_pool.with_connection do
      m = Metalics.find(id)
      m.pose_problem
    end
  end
end