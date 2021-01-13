#sorting the list  of hackathons alphabetically and sorting by the dates
from datetime import datetime

hackathons =[
    {'Title':'Set up a personal GitHub Page', 'Date': '2021-01-11'},
    {'Title':'Build a Starter Pack','Date':'2021-01-11'},
    {'Title':'Build and Deploy a Full Stack Web App with AWS', 'Date':'2021-01-11' },
    {'Title':'Build a Tic-Tac-Toe Game','Date':'2021-01-12'},
    {'Title':'Redesign your Favorite Website','Date':'2021-01-12'},
    {'Title':'Automate a Daily Task', 'Date':'2021-01-12'},
    {'Title':'Write a code to sort a list','Date':'2021-01-13'},
    {'Title':'Design an Outfit for Ellie','Date':'2021-01-14'},
    {'Title':'Build a project that uses a dataset','Date':'2021-01-15'},
    {'Title':'Connect Two APIs Together','Date':'2021-01-16'},
]

#function to get hackathons information
def get_title(hackathon):
    return hackathon.get('Title')

def get_dates(hackathon):
    return hackathon.get('Date')

#sorting by title alphabetically
hackathons.sort(key=get_title)
print('\n')
print("Sorting Hackathons Alphabetically")
print('\n')
print (hackathons, end='\n\n')

#sorting by dates
hackathons.sort(key= lambda x:datetime.strptime(x['Date'], '%Y-%m-%d'))
print('\n')
print("Sorting Hackathons according to dates")
print('\n')
print (str(hackathons), end='\n\n')

