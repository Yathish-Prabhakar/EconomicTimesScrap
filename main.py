import requests
import csv
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://etmarketsapis.indiatimes.com/ET_Stats/gainers'
    parameters={'pagesize':25, 'exchange':'nse', 'sort':'intraday', 'sortby':'percentchange', 'sortorder':'desc',
                'duration':'1d', 'marketcap':'largecap,midcap'}
    et_response = requests.get(url=url, params=parameters)
    #print(str(et_response.json()))
    data_file = open('ETScrap.csv','w')
    csv_writer = csv.writer(data_file)
    csv_writer.writerow(et_response.json()['searchresult'][0].keys())
    for row in et_response.json()['searchresult']:
        csv_writer.writerow(row.values())
