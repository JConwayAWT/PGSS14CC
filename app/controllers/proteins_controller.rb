class ProteinsController < ApplicationController
  before_action :set_protein, only: [:show, :edit, :update, :destroy]

  # GET /proteins
  # GET /proteins.json
  def index
    @proteins = Protein.all
  end

  # GET /proteins/1
  # GET /proteins/1.json
  def show
  end

 def cancel
    t = Protein.find(params[:id])
    t.last_tick=0
    t.done=true
    t.save!
    render json: {} and return
  end
    
  def retreive_problem
    t = Protein.find(params[:id])

    returnData = {message: t.message,answer: t.answer,statusDone: t.statusdone,done: t.done}

    unless t.done
      t.last_tick=Time.now
      t.save!
    end


    render json: returnData and return
  end

  def pose_problem
    t = Protein.new
    t.problem_parameters = params[:points].to_json
    t.algorithm = params[:algorithm]
    t.statusdone = "Waiting in queue..."
    t.last_tick=Time.now
    t.done=false
    t.save!
    
    ProteinSolverJob.new.async.perform(t.id)

    returnData = {statusMessage: "Processed",databaseId: t.id}

    render json: returnData and return
  end

  # GET /proteins/new
  def new
    @protein = Protein.new
  end

  # GET /proteins/1/edit
  def edit
  end

  # POST /proteins
  # POST /proteins.json
  def create
    @protein = Protein.new(protein_params)

    respond_to do |format|
      if @protein.save
        format.html { redirect_to @protein, notice: 'Protein was successfully created.' }
        format.json { render :show, status: :created, location: @protein }
      else
        format.html { render :new }
        format.json { render json: @protein.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /proteins/1
  # PATCH/PUT /proteins/1.json
  def update
    respond_to do |format|
      if @protein.update(protein_params)
        format.html { redirect_to @protein, notice: 'Protein was successfully updated.' }
        format.json { render :show, status: :ok, location: @protein }
      else
        format.html { render :edit }
        format.json { render json: @protein.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /proteins/1
  # DELETE /proteins/1.json
  def destroy
    @protein.destroy
    respond_to do |format|
      format.html { redirect_to proteins_url, notice: 'Protein was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_protein
      @protein = Protein.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def protein_params
      params[:protein]
    end
end
