get_ipython().system(u'pip install pint')
# Configure Jupyter so figures appear in the notebook
get_ipython().magic(u'matplotlib inline')

# Configure Jupyter to display the assigned value after an assignment
get_ipython().magic(u"config InteractiveShell.ast_node_interactivity='last_expr_or_assign'")

# import functions from the modsim library
from modsim import *

# set the random number generator
np.random.seed(7)

"""Start a new Cell Here"""

bikeshare = State(Brooklyn=10, Manhattan=2, Co2Subway=0, ride=0)

def bike_to_Manhattan(state):
    """Move one bike from Brooklyn to Manhattan.

    state: bikeshare State object
    """
    if state.Brooklyn == 0:
        return
    state.Brooklyn -= 1
    state.Manhattan += 1


def bike_to_Brooklyn(state):
    """Move one bike from Manhatten to Brooklyn.

    state: bikeshare State object
    """
    if state.Manhattan == 0:
        return
    state.Manhattan -= 1
    state.Brooklyn += 1


def step(state, p1, p2):
    if flip(p1):
        bike_to_Manhattan(state)
        state.ride += 1

    if flip(p2):
        bike_to_Brooklyn(state)
        state.ride += 1


def Co2Saved(state):
    # We will use the data collected in the bikeshare model to calculate how much Co2 Emmissions were saved
    """An average commute by passenger vehicle causes the emission of over 4,000 pounds of CO2 per year
       An average commute of the same distance via subway is responsible for just 820 pounds of CO2 per year

       A walking or bicycling commute generates zero CO2 emissions.

       Source: https://www.transalt.org/sites/default/files/news/reports/2008/Rolling_Carbon.pdf """

    TrainRiders = state.ride

    # Subways in New York run almost every day
    # To figure out how much CO2 emmissions a single Subway ride causes we will
    # Assume a subway train runs at least once a day everyday for a year
    # So that gives us 820/365 which is approximately 3 pounds of CO2 emmisions per ride

    state.Co2Subway = str(TrainRiders * 3) + " lbs of CO2 emissions saved"



"""Start a new Cell Here"""

for m in range(365):
    for i in range(200):
        step(bikeshare, .5, .5)
        Co2Saved(bikeshare)

bikeshare
