# Foulbrood

Foulbrood is a simple Python tool to visualise the spread of European Foulbrood disease in honeybees in the UK.

European Foulbrood data and recorded incidents are available on "BeeBase" a website that tracks reports of the disease. However, the interactive map is
not particularly useful and difficult to immediately see the affected regions.

The datasets in 'datasets' folder were obtained from a simple copying of the data, for the purposes of the exercise. However, my aim is to use Python's request
library to gather this information directly via a GET request.

Note that this is not a web application, JavaScript is only being used to display the data.
 

## Installation

IMPORTANT: Please make sure you have been given the "index.html" file which has been emailed to the recruiter separately, since this contains a JavaScript
Google Maps API key which I will not push to the GIT repository, despite only accepting requests from "localhost:8000". Since I am displaying the data the old-fashioned way, there is no easy way to mask the API key.

Foulbrood uses an external library to convert OS Grid references to latitude and longitude.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install OSGridConverter.

```bash
pip install OSGridConverter

pip install requests
```



## Usage

```python foulbrood.py
```

This will start a python webserver. Once you have copied in the "index.html" file supplied separately, one can access the data visualisation tool via 

localhost:8000

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
