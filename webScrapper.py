import requests
from bs4 import BeautifulSoup
import json
import csv

def getHTML(_url):    
    # read website and return bs4.BeautifulSoup object
    page = requests.get(_url)
    content = BeautifulSoup(page.content, "html.parser")
    return content

def findByClass(_className, _contentHTML):
    #finds all divs with same class
    return _contentHTML.find_all(
        "div", 
        class_= lambda text: _className.lower() in text.lower()
        )
    return 

def findByTittle(requestedValue, _contentHTML):
    python_jobs = _contentHTML.find_all(
        "h2", string=lambda text: requestedValue.lower() in text.lower()
    )

    result = [
        h2_element.parent.parent.parent for h2_element in python_jobs
    ] 

    
    return result

def printJobs(_jobList):

    for job_element in _jobList["jobs"]:

        print(job_element["title_element"])
        print(job_element["company_element"])
        print(job_element["location_element"])
        print()

def output(_jobList):
    jobsDict = {"jobs":[]}
    count =0
    for job_element in _jobList:
        count += 1
        print(count)
        tempDict = {}
        tempDict["title_element"] = job_element.find("h2", class_="title").text.strip() 
        tempDict["company_element"] = job_element.find("h3", class_="company").text.strip()  
        tempDict["location_element"] = job_element.find("p", class_="location").text.strip()
        jobsDict["jobs"].append(tempDict)

    print(jobsDict)
    input()
    printJobs(jobsDict)
    createCSV(jobsDict)

def createCSV(_jobsDict):    
    print('started')
    job_data = _jobsDict['jobs']    

    # csv writter automatically adds new line character at the end leaving empty lines
    # newline parameter is used to resolve this
    with open('data_file.csv', 'w',newline='') as data_file:
        
        # create the csv writer object
        csv_writer = csv.writer(data_file)
        
        #write headers to csv        
        header = job_data[0].keys()
        csv_writer.writerow(header)   


        for job in job_data:
            # Writing data of CSV file
            csv_writer.writerow(job.values())
        
        data_file.close()