from flask import Blueprint

GlobeMonitorAPI = Blueprint('GlobeMonitorAPI', __name__)

@GlobeMonitorAPI.route("/GlobeMonitor/api/")
def GlobeMonitorWelcome():
    return "You have hit the root URL for the Globe Monitor API."