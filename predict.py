import requests
import argparse
import logging
from operator import itemgetter
import os

def predict_file(file_name, column_no, correct_type):
    url = "http://127.0.0.1:8081/labelling?column=%d" % column_no
    # url = "http://127.0.0.1:8082/labelling?column=%d" % column_no
    files = {'csv': open(file_name, 'r')}
    response = requests.post(url, files=files)
    #print response.text
    prop_scores = response.json()["labelling"]["property"]["avg"]  # because avg is used in the paper to classify csv
    prop_scores = sorted(prop_scores, key=itemgetter(1), reverse=True)
    print "\n\nfile name: %s column no: %d type: %s" % (file_name.split('/')[-1], column_no, correct_type)
    print "------------------------------"
    for ps in prop_scores:
        print ps


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="csv file")
    parser.add_argument("-c", "--column", help="column number")
    args = parser.parse_args()
    level = logging.INFO
    logging.basicConfig(level=level, format='%(asctime)s %(levelname)s %(message)s')
    if not args.file:
        logging.error("Specify a csv file: -f file.csv")
        return None
    if not args.column.isdigit():
        logging.error("Column must be an integer")
        return None
    return {"file_name": args.file, "column_no": int(args.column)}


# def main():
#     kwargs = parse_args()
#     if kwargs:
#         predict_file(**kwargs)

def main():
    # base_dir = "/Users/aalobaid/workspaces/Pyworkspace/tada/tadacode/explore/clean_input"
    base_dir = "/Users/aalobaid/workspaces/Pyworkspace/tada/tadacode/explore/clean_input_for_seb_test"

    files_cols = [
        ('badmintonplayers.csv', 2, 'height'),
        ('badmintonplayers.csv', 3, 'weight'),
        ('basketballplayers.csv', 2, 'height'),
        ('basketballplayers.csv', 3, 'weight'),
        ('boxers.csv', 2, 'height'),
        ('boxers.csv', 3, 'weight'),
        ('cyclists.csv', 2, 'height'),
        ('cyclists.csv', 3, 'weight'),
        ('golfplayers3.csv', 0, 'height'),
        ('golfplayers3.csv', 1, 'weight'),
        ('gymnasts.csv', 2, 'height'),
        ('gymnasts.csv', 3, 'weight'),
        ('handballplayers.csv', 2, 'height'),
        ('handballplayers.csv', 3, 'weight'),
        ('Olympic Games.csv', 1, 'year'),
        ('Olympic Games.csv', 5, 'athletes'),
        ('rower.csv', 2, 'height'),
        ('rower.csv', 3, 'weight'),
        ('soccerplayers4.csv', 7, 'height'),
        ('soccerplayers4.csv', 8, 'weight'),
        ('stadiums2.csv', 4, 'capacity'),
        ('swimmers.csv', 2, 'height'),
        ('swimmers.csv', 3, 'weight'),
        ('tennisplayers.csv', 2, 'height'),
        ('tennisplayers.csv', 3, 'weight'),
        ('volleyballplayers.csv', 2, 'height'),
        ('volleyballplayers.csv', 3, 'weight'),
        ('wrestlers.csv', 2, 'height'),
        ('wrestlers.csv', 3, 'weight'),
    ]
    for fc in files_cols:
        predict_file(os.path.join(base_dir,fc[0]), fc[1], [fc[2]])

    #predict_file('/Users/aalobaid/workspaces/Pyworkspace/tada/tadacode/explore/clean_input/badmintonplayers.csv', 2, 'test')
    #predict_file('testfile/stadiums.csv', 2, 'test')

if __name__ == "__main__":
    main()
