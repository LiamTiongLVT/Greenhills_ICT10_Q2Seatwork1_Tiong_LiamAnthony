# Student Club Member Checker
from pyscript import display, document


def ICT_club(e):
    document.getElementById('meta').innerHTML = ' '
    candidatename = document.getElementById('candidate_name').value
    candidate_members = ['Emily', 'Lily', 'Jeodore', 'Arlie', 'Bemmie', 'Martsono' 'Cassally'] # I spent an uneccesary amount of time thinking about these names....
    candidate_checker = candidatename in candidate_members

    display_message = ('Sorry, your name is not on the list.', f'congratulations {candidatename}, you are now part of the ICT club.')

    display(display_message[candidate_checker], target='meta')
