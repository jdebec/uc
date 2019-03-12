import feedparser

rss_urls = {
        'nyt_home_page': 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
        'nyt_world':'http://rss.nytimes.com/services/xml/rss/nyt/World.xml',
        'reddit/python':'http://www.reddit.com/r/python/.rss',
        'lefigaro_world':'http://www.lefigaro.fr/rss/figaro_international.xml',
        }


d = feedparser.parse(rss_urls['nyt_home_page'])

#get some feed info
print ('rss title', d['feed']['title'])

#print struc of one entry:
print(d['entries'][1])

#loop on all entries and display values
for entry in d['entries']:
    fields = list(entry.keys())

    if 'tags' in fields:
        tags = [tag['term'] for
                tag in entry['tags']]
    else:
        tags = []
    if 'media_content' in fields:
        print(entry['media_content'])
        pics = [media['url'] for
                media in entry['media_content'] if
                media['medium'] == 'image']
    else:
        pics = []
    print('-'*5, entry['title'], '-'*5)
    print(entry['summary'])
    print('by: ', entry['author'])
    print('tags: ', ', '.join(tags))
    print('pics: ', '\n'.join(pics))
    print('date: ', entry['published'])
    print('*'*10)
