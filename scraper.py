from bs4 import BeautifulSoup
from urllib2 import urlopen
import pandas as pd


def get_stats(year):
    url = "http://www.basketball-reference.com/leagues/NBA_{}_advanced.html".format(year)
    content = urlopen(url).read()
    soup = BeautifulSoup(content, "lxml")

    fh = open('{}_season_advanced.csv'.format(year), 'w')

    head = soup.find('tr')
    td = head.find_all('th')
    line = ','.join([x.text for x in td])
    fh.write(line + "\n")

    rows = soup.find_all('tr', class_='full_table')

    for tr in rows:
        td = tr.find_all('td')
        line = ','.join([x.text for x in td])
        fh.write(line + "\n")

    rows = soup.find_all('tr', class_='italic_text partial_table')

    for tr in rows:
        td = tr.find_all('td')
        line = ','.join([x.text for x in td])
        fh.write(line + "\n")

    fh.close()


def get_ratios(year):
    section_url = "http://www.basketball-reference.com/leagues/NBA_{}.html#all_standings".format(year)
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
    rows = soup.find_all("tr", {"class": "full_table"})
    l = []
    for row in rows:
        cells = row.find_all("td")
        a = cells[0].a["href"][7:10]
        b = cells[3]
        l.append(a+','+str(float(b.find(text=True))*100))
        l.sort()
    return [x[4:] for x in l]


def get_scores(year):
    df = pd.read_csv('{}_season_advanced.csv'.format(year))
    df['Score'] = df['PER']*df['MP']
    fh = open('{}_Scores.csv'.format(year), 'w')
    fh.write('Tm,score' + '\n')
    grouped = df.groupby('Tm')
    for name, group in grouped:
        line = name
        x = 0
        for score in group.sort_values('MP', ascending=False)[:12]['Score']:
            x = x + score
        line += ','
        line += str(x)
        #print(line)
        fh.write(line + '\n')
    fh.close()
    df = pd.read_csv('{}_Scores.csv'.format(year))
    df = df[df['Tm'] != 'TOT']
    df['W/L'] = get_ratios(year)
    df.to_csv('{}_Scores.csv'.format(year))

year = range(1996, 2016)

for i in year:
    get_stats(i)
    get_scores(i)

#get_stats(2013)
#get_scores(2013)


