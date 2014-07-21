class MetalicsController < ApplicationController
  before_action :set_metalic, only: [:show, :edit, :update, :destroy]

  # GET /metalics
  # GET /metalics.json
  def index
    @metalics = Metalic.all
  end

  # GET /metalics/1
  # GET /metalics/1.json
  def show
  end

  # GET /metalics/new
  def new
    @metalic = Metalic.new
  end

  # GET /metalics/1/edit
  def edit
  end

  # POST /metalics
  # POST /metalics.json
  def create
    @metalic = Metalic.new(metalic_params)

    respond_to do |format|
      if @metalic.save
        format.html { redirect_to @metalic, notice: 'Metalic was successfully created.' }
        format.json { render :show, status: :created, location: @metalic }
      else
        format.html { render :new }
        format.json { render json: @metalic.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /metalics/1
  # PATCH/PUT /metalics/1.json
  def update
    respond_to do |format|
      if @metalic.update(metalic_params)
        format.html { redirect_to @metalic, notice: 'Metalic was successfully updated.' }
        format.json { render :show, status: :ok, location: @metalic }
      else
        format.html { render :edit }
        format.json { render json: @metalic.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /metalics/1
  # DELETE /metalics/1.json
  def destroy
    @metalic.destroy
    respond_to do |format|
      format.html { redirect_to metalics_url, notice: 'Metalic was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_metalic
      @metalic = Metalic.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def metalic_params
      params[:metalic]
    end
end
