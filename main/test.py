def get_url_view(): #change name
    hostname = 'http://www.nfl.com'
    player_name = 'travelle wharton'
    player_type = 'historical'
    content = (hostname + '/players/search?category=name&filter={}&playerType={}'.format(player_name, player_type))
    print(content)
    # souper = BeautifulSoup(content, 'html.parser')
    # player_url = hostname + (souper.find(id='result').a.attrs['href'])
    # content = requests.get(player_url)
    # souper = BeautifulSoup(content.text, 'html.parser')
    # player_bio = str(souper.find(id='player-profile-wrapper'))
    # player_stats = str(souper.find(id='player-stats-wrapper'))

get_url_view()
