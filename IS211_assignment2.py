#David vayman
#IS211_Assignment2

import urllib2
import csv
import datetime
import logging
import argparse

#url: https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv

def main():

    logging.basicConfig(file_name='error.log')

    def downloadData(url):
        
        response = urllib2.urlopen(url)
        return response
    
    def processData(data):

        file_input = csv.reader(data)

        dictionary = {}
        date_format = '%d/%m/%Y'

        for row in file_input:
            if row[0] == 'id':
                continue

            else:
                try:
                    row[2] = datetime.datetime.strptime(row[2], date_format)

                except ValueError:
                    line_number = int(row[0]) + 1
                    id = int(row[0])

                    logger = logging.getLogger('assignment2')
                    logger.error('Error processing line# {0} for ID {1}'.format(line_number, id))

                finally:
                    dictionary[int(row[0])] = (row[1], row[2])

        return dictionary
    

    def displayPerson(id,Data):
        
        try:
            response = 'Person #{id} is {name} with a birthday of {date}'

            print response.format(id=id, name=Data[id][0],
                                   date=str(Data[id][1]).split(' ')[0])

        except KeyError:
            print 'No user found with that id'

    
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="Enter Url of the csv file")
    args = parser.parse_args()

    if args.url:
        try:
            csvData = downloadData(args.url)

            Data = processData(csvData)

            x = "Enter the number for the ID #1-#100 Enter 0 to Exit!! "

            loopSwitch = True
            while loop_switch:
                loopSwitch = False

                try:
                    user = int(raw_input(x))

                except ValueError:
                    print 'Wrong input'
                    loopSwitch = True
                    continue       

                if user > 0:
                    displayPerson(user,Data)
                    loopSwitch = True
                else:
                    print "Thanks"

        except ValueError:

            print "url is not valid"

    else:

        print "Please enter a --url"

if __name__ == '__main__':
    main()
