require 'task'

class UsersController < ApplicationController
  def index
   x = `python lib/python/hello.py`
   @output = x
  end
end