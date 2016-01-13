#Using the SIGFOX API with Python

Basic API call to the SIGFOX API, using Python + the [Requests](http://docs.python-requests.org/en/latest/) library

##Prerequisite

* Python ...
* [Install](http://docs.python-requests.org/en/latest/user/install/#install) the Requests lib
	* `pip install requests`

##Get your API credentials

* Log on your SIGFOX Account
* Browse to your _Group_
* Retrieve your API credentials from the _Api access_ menu

##Env vars

Set the 3 following env vars
* API_USER
* API_PASSWORD
* DEVICEID

##Run

```
$ API_USER=xxxx API_PASSWORD=xxx DEVICEID=1234ABC python deviceMessages.py
```


