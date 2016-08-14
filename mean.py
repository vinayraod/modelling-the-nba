import math
import pandas as pd
import glob


def average(s): return sum(s) * 1.0 / len(s)


def sd(s):
    avg = average(s)
    variance = map(lambda x: (x - avg)**2, s)
    standard_deviation = math.sqrt(average(variance))
    return standard_deviation

dict = {}
for file_name in glob.glob('*.csv'):
    print(file_name)
    try:
        df = pd.read_csv(file_name)
        df.fillna("", inplace=True)
        for i, row in df.iterrows():
            if row['points'] != "":
                away = row['a1'], row['a2'], row['a3'], row['a4'], row['a5']
                home = row['h1'], row['h2'], row['h3'], row['h4'], row['h5']
                if dict.has_key(home) == False:
                    dict[home] = {}
                h_dict = dict[home]
                #
                if h_dict.has_key('scores'):
                    h_dict['scores'].append(int(row['points']))
                else:
                    h_dict['scores'] = [int(row['points'])]
                #
                if h_dict.has_key('points'):
                    h_dict['points'] += int(row['points'])
                else:
                    h_dict['points'] = int(row['points'])
                #
                if h_dict.has_key('team') == False:
                    h_dict['team'] = file_name[12:15]
                #
                ##########################
                if dict.has_key(away) == False:
                    dict[away] = {}
                h_dict = dict[away]
                #
                if h_dict.has_key('scores'):
                    h_dict['scores'].append(int(row['points']))
                else:
                    h_dict['scores'] = [int(row['points'])]
                #
                if h_dict.has_key('points'):
                    h_dict['points'] += int(row['points'])
                else:
                    h_dict['points'] = int(row['points'])
                #
                if h_dict.has_key('team') == False:
                    h_dict['team'] = file_name[9:12]
                #
    except KeyError:
        continue

for unit, values in dict.iteritems():
    values['mean'] = average(values['scores'])
    values['sd'] = sd(values['scores'])

counter = 0
with open('sample.csv', 'wb') as f:
    for unit, values in dict.iteritems():
        counter += 1
        line = str(counter) + '\t'
        line += str(unit) + '\t'
        line += str(values['team']) + '\t'
        line += str(values['points']) + '\t'
        line += str(values['mean']) + '\t'
        line += str(values['sd']) + '\n'
        f.write(line)
