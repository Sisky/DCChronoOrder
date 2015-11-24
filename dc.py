from lxml import html
import requests
import time
import operator

#Arrow Season 1
page = requests.get('http://www.imdb.com/title/tt2193021/episodes?season=1&ref_=tt_eps_sn_1')
tree = html.fromstring(page.content)

dates = tree.xpath('//div[@class="airdate"]/text()')
episode = tree.xpath('//meta[@itemprop="episodeNumber"]/@content')

for i in range(0, len(episode)):
    episode[i] = 'Arrow S1E' + episode[i]
    
for i in range(0, len(dates)):
    dates[i] = dates[i].strip(' \.\n\t')
    dates[i] = dates[i].replace('.','')
    dates[i] = time.strptime(dates[i], "%d %b %Y")
    
zipped = zip(episode, dates)
 
#Arrow Season 2
page = requests.get('http://www.imdb.com/title/tt2193021/episodes?season=2')
tree = html.fromstring(page.content)

dates = tree.xpath('//div[@class="airdate"]/text()')
episode = tree.xpath('//meta[@itemprop="episodeNumber"]/@content')

for i in range(0, len(episode)):
    episode[i] = 'Arrow S2E' + episode[i]
    
for i in range(0, len(dates)):
    dates[i] = dates[i].strip(' \.\n\t')
    dates[i] = dates[i].replace('.','')
    dates[i] = time.strptime(dates[i], "%d %b %Y")
    
zippeds2 = zip(episode, dates)
zipped = zipped + zippeds2

#Flash Season 1
page = requests.get('http://www.imdb.com/title/tt3107288/episodes?season=1&ref_=tt_eps_sn_1')
tree = html.fromstring(page.content)

dates = tree.xpath('//div[@class="airdate"]/text()')
episode = tree.xpath('//meta[@itemprop="episodeNumber"]/@content')

for i in range(0, len(episode)):
    episode[i] = 'Flash S1E' + episode[i]
    
for i in range(0, len(dates)):
    dates[i] = dates[i].strip(' \.\n\t')
    dates[i] = dates[i].replace('.','')
    dates[i] = time.strptime(dates[i], "%d %b %Y")
    
    
zippeds2 = zip(episode, dates)
zipped = zipped + zippeds2

#Flash S2
page = requests.get('http://www.imdb.com/title/tt3107288/episodes?season=2')
tree = html.fromstring(page.content)

dates = tree.xpath('//div[@class="airdate"]/text()')
episode = tree.xpath('//meta[@itemprop="episodeNumber"]/@content')

for i in range(0, len(episode)):
    episode[i] = 'Flash S2E' + episode[i]
    
for i in range(0, len(dates)):
    dates[i] = dates[i].strip(' \.\n\t')
    dates[i] = dates[i].replace('.','')
    if len(dates[i]) > 4:
        dates[i] = time.strptime(dates[i], "%d %b %Y")
    else:
    	dates[i] = time.strptime("31 Dec " + dates[i], "%d %b %Y")
    
    
zippeds2 = zip(episode, dates)
zipped = zipped + zippeds2

#Arrow 3
page = requests.get('http://www.imdb.com/title/tt2193021/episodes?season=3')
tree = html.fromstring(page.content)

dates = tree.xpath('//div[@class="airdate"]/text()')
episode = tree.xpath('//meta[@itemprop="episodeNumber"]/@content')

for i in range(0, len(episode)):
    episode[i] = 'Arrow S3E' + episode[i]
    
for i in range(0, len(dates)):
    dates[i] = dates[i].strip(' \.\n\t')
    dates[i] = dates[i].replace('.','')
    dates[i] = time.strptime(dates[i], "%d %b %Y")
    
    
zippeds2 = zip(episode, dates)
zipped = zipped + zippeds2

#Arrow 4
page = requests.get('http://www.imdb.com/title/tt2193021/episodes?season=4')
tree = html.fromstring(page.content)

dates = tree.xpath('//div[@class="airdate"]/text()')
episode = tree.xpath('//meta[@itemprop="episodeNumber"]/@content')

for i in range(0, len(episode)):
    episode[i] = 'Arrow S3E' + episode[i]
    
for i in range(0, len(dates)):
    dates[i] = dates[i].strip(' \.\n\t')
    dates[i] = dates[i].replace('.','')
    if len(dates[i]) > 4:
        dates[i] = time.strptime(dates[i], "%d %b %Y")
    else:
    	dates[i] = time.strptime("31 Dec " + dates[i], "%d %b %Y")
    
    
zippeds2 = zip(episode, dates)
zipped = zipped + zippeds2


zipped = sorted(zipped, key=operator.itemgetter(1))

final_list = [i[0] for i in zipped]

for k in final_list:
    print k
    
    
    
