require 'test_helper'

class MetalicsControllerTest < ActionController::TestCase
  setup do
    @metalic = metalics(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:metalics)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create metalic" do
    assert_difference('Metalic.count') do
      post :create, metalic: {  }
    end

    assert_redirected_to metalic_path(assigns(:metalic))
  end

  test "should show metalic" do
    get :show, id: @metalic
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @metalic
    assert_response :success
  end

  test "should update metalic" do
    patch :update, id: @metalic, metalic: {  }
    assert_redirected_to metalic_path(assigns(:metalic))
  end

  test "should destroy metalic" do
    assert_difference('Metalic.count', -1) do
      delete :destroy, id: @metalic
    end

    assert_redirected_to metalics_path
  end
end
