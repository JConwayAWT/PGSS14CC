class TravelingSalesmenController < ApplicationController
  before_action :set_traveling_salesman, only: [:show, :edit, :update, :destroy]

  # GET /traveling_salesmen
  # GET /traveling_salesmen.json
  def index
     
  end

  # GET /traveling_salesmen/1
  # GET /traveling_salesmen/1.json
  def show
  end

  def cancel
    t = TravelingSalesman.find(params[:id])
    
    returnData = {message: t.message,answer: t.answer,statusDone: t.statusdone,done: t.done}

    render json: returnData and return

  def retreive_problem
    t = TravelingSalesman.find(params[:id])

    returnData = {message: t.message,answer: t.answer,statusDone: t.statusdone,done: t.done}

    render json: returnData and return
  end

  def pose_problem
    t = TravelingSalesman.new
    t.problem_parameters = params[:points].to_json
    t.algorithm = params[:algorithm]
    t.statusdone = "Waiting in queue..."
    t.lastTick=Time.now
    t.done=false
    t.save!
    
    SolverJob.new.async.perform(t.id)

    returnData = {statusMessage: "Processed",databaseId: t.id}

    render json: returnData and return
  end

  # GET /traveling_salesmen/new
  def new
    @traveling_salesman = TravelingSalesman.new
  end

  # GET /traveling_salesmen/1/edit
  def edit
  end

  # POST /traveling_salesmen
  # POST /traveling_salesmen.json
  def create
    @traveling_salesman = TravelingSalesman.new(traveling_salesman_params)

    respond_to do |format|
      if @traveling_salesman.save
        format.html { redirect_to @traveling_salesman, notice: 'Traveling salesman was successfully created.' }
        format.json { render :show, status: :created, location: @traveling_salesman }
      else
        format.html { render :new }
        format.json { render json: @traveling_salesman.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /traveling_salesmen/1
  # PATCH/PUT /traveling_salesmen/1.json
  def update
    respond_to do |format|
      if @traveling_salesman.update(traveling_salesman_params)
        format.html { redirect_to @traveling_salesman, notice: 'Traveling salesman was successfully updated.' }
        format.json { render :show, status: :ok, location: @traveling_salesman }
      else
        format.html { render :edit }
        format.json { render json: @traveling_salesman.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /traveling_salesmen/1
  # DELETE /traveling_salesmen/1.json
  def destroy
    @traveling_salesman.destroy
    respond_to do |format|
      format.html { redirect_to traveling_salesmen_url, notice: 'Traveling salesman was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_traveling_salesman
      @traveling_salesman = TravelingSalesman.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def traveling_salesman_params
      params[:traveling_salesman]
    end
end
