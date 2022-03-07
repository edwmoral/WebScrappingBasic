from webScrapper import getHTML, findByClass,findByTittle,output

URL = "https://realpython.github.io/fake-jobs/"
contentHTML = getHTML(URL)

jobType = input('Do you want Python jobs or all jobs?').lower()

if ("p" in jobType):
    jobList = findByTittle("Python", contentHTML)

else:
    jobList = findByClass("card-content", contentHTML)


output(jobList)