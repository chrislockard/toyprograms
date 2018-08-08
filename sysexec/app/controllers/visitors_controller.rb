class VisitorsController < ApplicationController
  
  def new
    Rails.logger.debug "DEBUG: Entering new method"
    @command = Command.new
    flash[:notice] = "Executed command!"
    Rails.logger.debug "DEBUG: Command name is " + @command.name
    # render 'visitors/new', :layout => false
  end

end
