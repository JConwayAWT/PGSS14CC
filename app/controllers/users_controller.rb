require 'task'

class UsersController < ApplicationController
  def index
   x = `python lib/python/hello.py #{ENV["RAILS_ENV"]}`
   @output = x
  end
end