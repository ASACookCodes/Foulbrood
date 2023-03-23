# Foulbrood

NOTE: 23/03/2022
IN A BIZARRE TWIST OF FATE, THE NIGHT OF 22/03/2022 THE WEBSITE https://www.nationalbeeunit.com UNDERWENT A COMPLETE OVERHAUL. It is not unliklely that the website overhaul is an ongoing process, meaning that I will be maintaining the code until I receive feedback every day to make sure it still works.

Foulbrood is a Python tool to visualise the spread of European Foulbrood disease in honeybees in the UK.

European Foulbrood data and recorded incidents are available on "BeeBase" (https://www.nationalbeeunit.com) a website that tracks reports of the disease. However, the interactive map is
not particularly useful and difficult to immediately see the affected regions. 

The data on BeeBase shows Ordnance Survey Grid Reference (10km squares) and how many incidents there are for that area.
Foulbrood is therefore designed to:
- scrape this data from the website by year for the last 5 years (note that there is no disease data for 2023 thus far). Good news for bees.
- parse it to obtain the OS References as a dataframe using Pandas
- convert these to latitude and longitudes
- write them to CSV files by year
- start a Python web server
- Upon the user loading one of the generated CSVs, will show a heat map of the affected areas for that year.

The tool will scrape data from BeeBase and will parse the data and write it to a CSV file. 

Note that this is not a web application, JavaScript is only being used to display the data using the Google maps API.
 

## Installation

IMPORTANT: Please make sure you have been given the "index.html" file which has been emailed to the recruiter separately, since this contains a Google Maps
API key which I will not push to the GIT repository, despite only accepting requests from "localhost:8000", for security reasons.
Since I am displaying the data the old-fashioned way, there is no easy way to mask the API key on the front-end.


Foulbrood uses some external libraries. Before installing, please make sure you are using the latest version of Python and pip.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following:

```bash
pip install OSGridConverter

pip install pandas

pip install requests

pip install beautifulsoup4
```



Please, if you have any trouble whatsoever running the program contact me at:
asacook@btinternet.com
or +44(0)7473483316




## Usage

```python
python foulbrood.py
```

- This will start a python webserver. Once you have copied in the "index.html" supplied separately into the project folder, one can access the data visualisation tool via  localhost:8000
- You can then load and inspect the data by choosing a file from the CSV's folder in the project directory.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
