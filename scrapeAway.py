from selenium import webdriver

from miscData import NICKNAME

# create new chrome driver
driver = webdriver.Chrome()

year = 2010
tab = "overview"
tab_urls = {
    'overview':''
}

BASE_URL = "https://football.fantasysports.yahoo.com/league/{}/".format(NICKNAME)



# create login function
def login(driver):
    """
    function to login to yahoo using selenium
    :return:
    """

    driver.get(BASE_URL)

    # type in username
    username_box = driver.find_elements_by_name("username")

    # you must verify the login


def get_league_id():
    """
    each year the id of the league changes, if you request the base url you
    can use the links to determine the league id for that year
    :return:
    """
    pass

login(driver)

# log into the site

# find the drop down with all prior years

# for each prior year:
    # Overview tab:
        # get all the teams
        # get the final standings
            # final points
            # roster moves
        # for each team get the points for each week
    # Final Rosters tab:
        # Collect players and their stats
    # Draft results tab:
        # Collect draft results
    # Setting:
        # collect each settings and create a json file to store values
    # Transactions:
        # Collect each transaction
    # commishnote Note
        # Collect

# "https://football.fantasysports.yahoo.com/archive/nfl/2008/669862" = overview table

# "https://football.fantasysports.yahoo.com/archive/nfl/2008/669862/teams" = managers tab

# https://football.fantasysports.yahoo.com/archive/nfl/2008/669862/teams = rosters

# draftresults = draft results

# settings = settings

# transactions = transactions

# commishnote = comissioners note
