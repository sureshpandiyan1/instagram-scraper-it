import datetime
import json
import re
import time

import requests
from folsid import FOLLOWING_ID, FOLLOWING_COUNTS
from followersid import followers_counts, target_insta_id

# WARN YOU BEFORE MESS THIS FILE !!!!!!!
# => DON'T change anything in this main.py file
# => DON'T remove a cookies, otherwise won't work
# => DON'T EDIT THIS FILE
# => DON'T PLAY WITH THIS CODE LIKE A KID, IT'S CAN HANG YOUR SYSTEM


# INTRO
print(
    'The Instagram-scrap-it can collect information related to the things like post date, images, etc.' + '\n' +
    'Its written code in python that will run faster without delay of the start trouble.' + '\n' +
    'Theres no need to use your login id & password to use Instagram-scarp-it.' + '\n \n' +
    'WELCOME TO Instagram-scrap-it'
)

timz = datetime.datetime.now()
print("Copyright (C) " + timz.strftime('%Y') + " Suresh Pandiyan")

print('')
print('Enter Your Session ID')
ses_get = input('')
mysession = ses_get
print('-------------------------------')

permanent_cookie = "sessionid={}".format(mysession)

myheaders = {
    "X-IG-App-ID": "936619743392459",
    "Cookie": permanent_cookie,
}


def ss_liveornots(dname, msg):
    with open(dname, 'w') as liveornot:
        print(msg, file=liveornot)


# noinspection PyBroadException
def live_ss():
    try:
        whoismsgm()
        ss_liveornots('Instagram-scarp-it-LIVE', 'Instagram-scarp-it - LIVE,good to go !! :D')
    except:
        ss_liveornots('Instagram-scarp-it=DEATH', 'Instagram-scarp-it - DEATH, '
                                                  '\n PLZ GET NEW session ID for make me live.:(')


live_ss()


def insta_svc():
    my_src = [
        'insta id', 'get complete data about the user',
        'search the users', 'profile information (yours)',
        'list all insta users',
        'random fake users list',
        'find similar hashtag', 'list of active story post (yours)',
        'recent inbox online users (yours)', 'list all followings', 'unread message (yours)',
        'get biography', 'analyze your post for growth',
        'get any reels / image with complete data ',
        'collect anyone followers list'
        'quit'
    ]
    runs = True
    while runs:
        for x, y in enumerate(my_src, start=1):
            print(x, y)
        mychc = int(input('choose your option => '))
        if mychc == 1:
            print('enter your username')
            myname = input('')
            getuserid(myname)
        if mychc == 2:
            print('enter your username => ')
            myname = input('')
            getinfo(myname)
            followedbywho(myname, getinfo(myname))
        if mychc == 3:
            k = input('')
            usermatch(k)
        if mychc == 4:
            print('Note - only avaliable if you login your insta id in your browser')
            get_profile_info()
        if mychc == 5:
            listallusers()
        if mychc == 6:
            listallfakeusers()
        if mychc == 7:
            similarhashtag()
        if mychc == 8:
            print('Note - only avaliable if you login your insta id in your browser')
            trays()
        if mychc == 9:
            whoismsgm()
        if mychc == 10:
            list_all_follwing()
        if mychc == 11:
            unseensmsg()
        if mychc == 12:
            biography()
        if mychc == 13:
            checkourcompetitor()
        if mychc == 14:
            downloadanyoneimage()
        if mychc == 15:
            collect_anyone_followers_list()
        if mychc == 16:
            runs = False


def getinfo(names):
    sample_url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={names}"
    sample = requests.get(sample_url, headers=myheaders)
    x = json.loads(sample.text)
    return x


def getuserid(names):
    sample_url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={names}"
    sample = requests.get(sample_url, headers=myheaders)
    x = json.loads(sample.text)
    print('your instagram id - ', x['data']['user']['id'])


def get_profile_info():
    myinfos = 'https://i.instagram.com/api/v1/accounts/edit/web_form_data/'
    infos = requests.get(myinfos, headers=myheaders)
    myinf = json.loads(infos.text)
    myname = myinf['form_data']['first_name']
    mymailid = myinf['form_data']['email']
    print('%s\n%s\n \n' % (myname, mymailid))


def followedbywho(user, y):
    with open(str(user) + '.txt', 'w', encoding="utf-8") as k:
        pp = json.dumps(y, indent=4)
        print(pp, file=k)


# noinspection PyBroadException
def usermatch(k):
    usersearch = k
    find_username = f"https://www.instagram.com/web/search/topsearch/?context=blended&query={usersearch}&rank_token=0" \
                    f".17061633125971365&include_reel=true "
    bs = requests.get(find_username, headers=myheaders)
    ps = json.loads(bs.text)
    # noinspection PyUnusedLocal
    try:
        for m in range(0, 1000):
            name = ps['users'][m]['user']['username']
            profile_pic = ps['users'][m]['user']['profile_pic_url']
            badge = '✔ - verified badge' if ps['users'][m]['user']['is_verified'] else 'not verified badge'
            url_suggest = 'https://www.instagram.com/{}'.format(str(name))
            print('user_: %s\nprofile_pic: %s\nbadge: %s \n' % (url_suggest, profile_pic, badge))
    except Exception as error:
        pass


# noinspection PyBroadException,PyUnusedLocal
def listallusers():
    start = 2000000000
    end = 91000000000
    for m in range(start, end):
        maxuser = 'https://i.instagram.com/api/v1/users/{}/info/'.format(m)
        muser = requests.get(maxuser, headers=myheaders)
        myinf = json.loads(muser.text)
        try:
            print(myinf['user']['username'])
        except Exception as KeyError:
            pass


# noinspection PyBroadException,PyUnusedLocal
def listallfakeusers():
    start = 2000000000
    end = 91000000000
    for m in range(start, end):
        maxuser = 'https://i.instagram.com/api/v1/users/{}/info/'.format(m)
        muser = requests.get(maxuser, headers=myheaders)
        myinf = json.loads(muser.text)
        try:
            if myinf['user']['follower_count'] == 0 and myinf['user']['media_count'] == 0:
                print('https://www.instagram.com/' + myinf['user']['username'])
        except Exception as KeyError:
            pass


# noinspection PyBroadException,PyUnusedLocal
def findusers(usernames):
    start = 2000000000
    end = 91000000000
    for m in range(start, end):
        maxuser = 'https://i.instagram.com/api/v1/users/{}/info/'.format(m)
        muser = requests.get(maxuser, headers=myheaders)
        myinf = json.loads(muser.text)
        try:
            if myinf['user']['full_name'] == usernames or \
                    myinf['user']['username'] == usernames or \
                    myinf['user']['profile_pic_url'] == usernames:
                print(myinf['user'])
        except Exception as KeyError:
            pass


def similarhashtag():
    print('enter your hashtag below :')
    usersearch = input('')
    usersearch = re.sub('#', '%23', usersearch)
    print('wait, few seconds... \n')
    find_username = f"https://i.instagram.com/api/v1/web/search/topsearch/?context=blended" \
                    f"&query={usersearch}&rank_token=0.2712077074231197&include_reel=true "
    bs = requests.get(find_username, headers=myheaders)
    ps = json.loads(bs.text)
    myhash = []
    totalhashtags = len(ps['hashtags']) - 1
    for m in range(0, totalhashtags + 1):
        hashname = ps['hashtags'][m]['hashtag']['name']
        mediaposts = ps['hashtags'][m]['hashtag']['search_result_subtitle']
        print('#%s %s' % (hashname.ljust(20), mediaposts))
        myhash.append('#' + hashname)
    print('-' * 60)
    myques = input('are you want to use this in your post for hashtag - y or n ? ')
    if myques == 'y':
        time.sleep(5)
        print('just wait, let me do it for you in single line \n')
        time.sleep(2)
        d = ','.join(myhash)
        d = re.sub(',', ' ', d)
        print(d)
    else:
        pass


def trays():
    tray = 'https://i.instagram.com/api/v1/feed/reels_tray/'
    bs = requests.get(tray, headers=myheaders)
    ps = json.loads(bs.text)
    traynumber = len(ps['tray'])
    print('here list of active story post - users now \n')
    u = datetime.datetime.now()
    print(u.strftime("%c"))
    print('%s %s' % ('user'.ljust(30), 'Spost'))
    print('--' * 30)

    for x in range(0, traynumber):
        theusern = ps['tray'][x]['user']['username']
        mediacount = ps['tray'][x]['media_count']
        print('%s %s ' % (theusern.ljust(30), mediacount))


def timestamps(mytime):
    thattime = str(mytime)
    timestamp = int(thattime[0:10])
    datetimez = time.strftime('%A, %Y-%m-%d %H:%M:%S', time.localtime(timestamp))
    return datetimez


def whoismsgm():
    useronline = 'https://i.instagram.com/api/v1/direct_v2/inbox/?persistentBadging' \
                 '=true&folder=&limit=100&thread_message_limit=100'
    rd = requests.get(useronline, headers=myheaders)
    ds = json.loads(rd.text)
    njk = len(ds['inbox']['threads'])
    print('list of whoismsgm3 \n')
    for h in range(0, njk):
        onlineornot = ds['inbox']['threads'][h]['users'][0]['is_private']
        usernn = ds['inbox']['threads'][h]['users'][0]['username']
        ons = 'online' if onlineornot else 'offline'
        print('%s %s' % (usernn, ons))


def unseensmsg():
    useronline = 'https://i.instagram.com/api/v1/direct_v2/inbox/?persistentBadging' \
                 '=true&folder=&limit=100&thread_message_limit=100'
    rd = requests.get(useronline, headers=myheaders)
    ds = json.loads(rd.text)
    print('list of new message TODAY \n')
    newmessagetoday = ds['inbox']['unseen_count']
    print('new messages- %s' % newmessagetoday)



def list_all_follwing():
    if FOLLOWING_ID and FOLLOWING_COUNTS != '':
        main_followers_list = f"https://i.instagram.com/api/v1/friend" \
                              f"ships/{FOLLOWING_ID}/following/?count={FOLLOWING_COUNTS}&max_id=0 "
        fol_ll = requests.get(str(main_followers_list), headers=myheaders)
        how_many = json.loads(fol_ll.text)
        spt_how = str(how_many).split(',')
        usernamess = []
        for x in spt_how:
            if 'username' in x:
                usernamess.append(x)
                with open('followers_list.txt', 'w') as k:
                    for lX in usernamess:
                        (first, second) = lX.split(':')
                        print('%s' % second, file=k)
            if 'pk' in x:
                yg = str(x).split(':')
                matchy = re.findall(r'[0-9]+', str(yg))
                if len(matchy) < 2:
                    for xx in matchy:
                        print(xx)
    else:
        print(' - kindly navigate to folsid.py')
        print(' - enter your following insta id and counts \n')
    print('NOTE:')
    print('if you not enter anythings in folsid.py, you dont get followers list details in a text documents')
    print('')


def biography():
    print('enter the username to get bio')
    usersss = input('')
    sample_url = "https://i.instagram.com/api/v1/users/web_profile_info/?username={}".format(usersss)
    sample = requests.get(sample_url, headers=myheaders)
    gh = json.loads(sample.text)
    names = gh['data']['user']['username']
    bios = gh['data']['user']['biography']
    print('%s %s \n' % (names, bios))


def checkourcompetitor():
    ask_medianumber = str(input(''))
    media_url = f"https://i.instagram.com/api/v1/media/{ask_medianumber}/info/"
    media_check = requests.get(media_url, headers=myheaders)
    tk = json.loads(media_check.text)
    print('your post complete analysis details when your post get high likes:')
    timez = tk['items'][0]['device_timestamp']
    likes = tk['items'][0]['like_count']
    # captions = tk['items'][0]['caption']['text']
    mytime = timestamps(timez)
    with open('analysisthepost.txt', 'w+') as k:
        k.writelines('%s | likes -  %s' % (mytime, likes))


def downloadanyoneimage():
    print('type the media no')
    media_no = str(input(''))
    for x in media_no:
        media_url = f"https://i.instagram.com/api/v1/media/{x}/info/"
        media_check = requests.get(media_url, headers=myheaders)
        tk = json.loads(media_check.text)
        print(tk)

def collect_anyone_followers_list():
    users = []
    cnt_mx = followers_counts / 12
    (zx,y) = str(cnt_mx).split('.')
    print('this process is very slow if you have large amount of followers...')
    print('just open followers_list.txt,it will collect followers')
    for y in range(0,12):
        for x in range(0,int(zx)):
            maxs = 12 * x
            follows = f'https://i.instagram.com/api/v1/friendships/{target_insta_id}/followers' \
                      f'/?count=12&max_id={maxs}&search_surface=follow_list_page'
            kkk = requests.get(follows,headers=myheaders)
            opo = json.loads(kkk.text)
            po = opo['users'][y]['username']
            users.append(po)
            with open('followers_list.txt','w') as lxf:
                for yh in users:
                    print('%s' % yh,file=lxf)

insta_svc()

# ----------------- End -------------
