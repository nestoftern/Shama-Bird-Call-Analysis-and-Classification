import urllib.request, json
import sys
import os


savePath = "../TERN/Bird Call Analysis/data/xeno-canto-dataset/"


def save_json(searchTerms, birdName, country):
    numPages = 1
    page = 1
    path = savePath + birdName.replace(':', '') + "/" + country
    if not os.path.exists(path):
        print("Creating subdirectory " + path + " for downloaded files...")
        os.makedirs(path)
        # downloads a json file for every page found in a query
    while page < numPages + 1:
        print("Loading page " + str(page) + "...")
        url = 'https://www.xeno-canto.org/api/2/recordings?query={0}&page={1}'.format(searchTerms.replace(' ', '%20'),page)
        print(url)
        jsonPage = urllib.request.urlopen(url)
        jsondata = json.loads(jsonPage.read().decode('utf-8'))
        filename = path + "/jsondata_p" + str(page) + ".json"
        with open(filename, 'w') as outfile:
            json.dump(jsondata, outfile)
        numPages = jsondata['numPages']
        page = page + 1
    print("Found ", numPages, " pages in total.")
    # return number of files in json
    print("Saved json for ", (numPages - 1) * 500 + len(jsondata['recordings']), " files")
    return path


''' Reads the json and return the list of values for selected json part
    i.e. "id" - ID number, "type": type of the bird sound such as call 
    or song for all Xeno Canto files found with the given search terms.'''

def read_data(searchTerm, path):
    data = []
    numPages = 1
    page = 1
    # read all pages and save results in a list
    while page < numPages + 1:
        with open(path + "/jsondata_p" + str(page) + ".json", 'r') as jsonfile:
            jsondata = jsonfile.read()
        jsondata = json.loads(jsondata)
        numPages = jsondata['numPages']
        # find "recordings" in a json and save a list with a search term
        for k in range(len(jsondata['recordings'])):
            data.append(jsondata["recordings"][k][searchTerm])
        page = page + 1
    return data




'''Downloads all sound files found with the search terms into 
   xeno-canto directory into catalogue named after the search term 
   filename have two parts: the name of the bird in latin and ID number'''

def download(searchTerms, birdName, country):
    path = save_json(searchTerms, birdName, country)
    # get filenames: recording ID and bird name in latin from json
    filenamesID = read_data('id', path)
    filenamesCountry = read_data('cnt', path)
    # get website recording http download address from json
    fileaddress = read_data('file', path)
    numfiles = len(filenamesID)
    print("A total of ", numfiles, " files will be downloaded")
    for i in range(0, numfiles):
        print("Saving file ", i + 1, "/", numfiles,
              path + birdName.replace(':', '') + filenamesID[
                  i] + ".mp3")
        urllib.request.urlretrieve("http:" + fileaddress[i],
                                   path + "/" + birdName + filenamesID[i] + ".mp3")
        

country = 'India' #country name
bird = 'Cyornis tickelliae' #bird name

download(bird + ' cnt:' + country + ' type:song', bird.replace(' ', ''), country)
download(bird + ' type:song', bird.replace(' ', ''), 'country')