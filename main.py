import manganelo
from datetime import datetime
import json

userlist = []
with open('data/checkdate.txt', 'r') as file:
    checkdate = datetime.strptime(file.read(), "%Y-%m-%d %H:%M:%S")
    file.close()
with open('data/userlist.txt', 'r') as file:
    userlist = json.load(file)

def get_date():
    return checkdate.strftime("%m-%d-%Y %H:%M:%S")

def search(input):
    results = manganelo.get_search_results(input)
    matches = []
    for r in results:
        #print(r.title)
        tmp = []
        tmp.append(r.title)
        matches.append(tmp)
        #r.download_icon("./images/" + r.title + ".png")
    return matches

def exists(input):
    results = manganelo.get_search_results(input[0])
    if len(results) == 0:
        print("Nothing exists containing your search")
        return False
    else:
        return True

def add_to_list(input):
    if input not in userlist:
        userlist.append(input)
        with open('data/userlist.txt', 'w') as file:
            json.dump(userlist, file)

def remove_from_list(input):
    if input in userlist:
        userlist.remove(input)
        with open('data/userlist.txt', 'w') as file:
            json.dump(userlist, file)

def check_new():
    global checkdate
    op = []
    for item in userlist:
        results = manganelo.get_search_results(item)
        for r in results:
            chaps = r.chapter_list
            if r.title.lower() == item.lower():
                for c in chaps:
                    if c.uploaded > checkdate:
                        tmp = [r.title, c.chapter, c.uploaded, c.url]
                        op.append(tmp)
                        #print(f"{c.chapter} of {r.title} is new {c.url}")
    checkdate = datetime.today()
    with open('data/checkdate.txt', 'w') as file:
        file.write(checkdate.strftime("%Y-%m-%d %H:%M:%S"))
        file.close()
    return op

def get_list():
    tmp = []
    for i in userlist:
        e = []
        e.append(i)
        tmp.append(e)
    return tmp