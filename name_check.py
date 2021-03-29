from requests import get

"""
    Services - URL links for more services
    Data was taking from namechk.com
"""
services = [
    [
        'github.com/{}',
        'github'
    ], [
        'api.github.com/users/{}/events/public',
        'github'
    ], [
        'api.github.com/users/{}',
        'github'
    ], [
        'facebook.com/{}',
        'facebook'
    ], [
        'twitter.com/{}',
        'twitter'
    ], [
        'twitch.com/{}',
        'twitch'
    ], [
        'reddit.com/user/{}',
        'reddit'
    ], [
        'producthunt.com/@{}',
        'producthunt'
    ], [
        'steamcommunity.com/id/{}',
        'steam'
    ], [
        'myspace.com/{}',
        'myspace'
    ], [
        'deviantart.com/{}',
        'deviantart'
    ], [
        'last.fm/user/{}',
        'last'
    ], [
        'slideshare.net/{}',
        'slideshare'
    ], [
        'vk.com/{}',
        'vk'
    ], [
        'roblox.com/users/profile?username={}',
        'roblox'
    ], [
        'skyscanner.com/trip/user/{}',
        'skyscanner'
    ], [
        'pastebin.com/u/{}',
        'pastebin'
    ], [
        'en.wikipedia.org/w/api.php?action=query&format=json&list=allusers&auprefix={}&aulimit=10',
        'wikipedia'
    ], [
        'codementor.io/{}',
        'codementor'
    ], [
        'news.ycombinator.com/user?id={}',
        'ycombinator'
    ], [
        '500px.com/{}',
        '500px'
    ], [
        'open.spotify.com/user/{}',
        'spotify'
    ], [
        'scribd.com/{}',
        'scribd'
    ], [
        'wattpad.com/user/{}',
        'wattpad'
    ], [
        'badoo.com/en/profile/{}',
        'badoo'
    ], [
        'mixcloud.com/{}',
        'mixcloud'
    ], [
        'telegram.me/{}',
        'telegram'
    ], [
        't.me/{}',
        'telegram'
    ],
]


class NameCheck:
    def __init__(self, services):
        self.services = services

    def getUrl(self, uri, username):
        return ('https://{}'.format(uri)).format(username)

    def request(self, url):
        res = get(url)
        text = res.text.lower()
        return res.status_code // 100 == 2 and text.find('not found') == -1 and text.find('error') == -1 and text.find('не найдена') == -1 and text.find('no such user.') == -1


    def search(self, username):
        index = 0
        for uri, service in self.services:
            if self.request(self.getUrl(uri, username)):
                print('[+] Username found on: {}'.format(service))
                print('[+] Profile url: {}'.format(self.getUrl(uri, username)))
                print('-'*75)
                index += 1
        if index:
            print('[+] All profile are found [+]')
        else:
            print('[+] No Such users with this username [+]')


print('[+] Find Profile by Username [+]')
username = input('[+] Enter username to search: ')
name_check = NameCheck(services)
name_check.search(username)
