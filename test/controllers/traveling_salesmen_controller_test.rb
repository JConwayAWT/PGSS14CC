require 'test_helper'

class TravelingSalesmenControllerTest < ActionController::TestCase
  setup do
    @traveling_salesman = traveling_salesmen(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:traveling_salesmen)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create traveling_salesman" do
    assert_difference('TravelingSalesman.count') do
      post :create, traveling_salesman: {  }
    end

    assert_redirected_to traveling_salesman_path(assigns(:traveling_salesman))
  end

  test "should show traveling_salesman" do
    get :show, id: @traveling_salesman
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @traveling_salesman
    assert_response :success
  end

  test "should update traveling_salesman" do
    patch :update, id: @traveling_salesman, traveling_salesman: {  }
    assert_redirected_to traveling_salesman_path(assigns(:traveling_salesman))
  end

  test "should destroy traveling_salesman" do
    assert_difference('TravelingSalesman.count', -1) do
      delete :destroy, id: @traveling_salesman
    end

    assert_redirected_to traveling_salesmen_path
  end
end
