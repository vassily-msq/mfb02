import
def list_posts(qs):
    a = '---------------------'
    print(a)
    for post in qs:
        print("Created on: "+ post.date_created)
        print("Published on: "+ post.date_published)
        print("Title: "+ post.title)
        print(post.text)
        print(a)

def pr(post):
    '''assumes: Post on the input'''
    auth = post.author
    dcr = post.date_created
    dpub = post.date_published
    ttle = post.title
    txt = post.text
    print(auth)
