require 'task'

class UsersController < ApplicationController
  def index
   x = `python lib/python/hello.py #{ENV["RAILS_ENV"]}`
   @output = x
  end

  def change_first_name
    SomeJob.new.async.perform
    @my_name = "Jeff"
  end
end