![pypi](https://img.shields.io/pypi/v/folding-at-home) ![versions](https://img.shields.io/badge/python-3.6%2B-green)

# Folding@Home Client API
This package allows you to manage a Folding@Home client via mocking the same API
calls your browser makes when using the FAHViewer local web portal.

## Install

```
pip3 install folding-at-home
```

## Usage

| Arguments 	| Description                                   	|
|-----------	|-----------------------------------------------	|
| --host    	| Hostname or IP Address                        	| 
| --https    	| Default is to use HTTP, use HTTPS instead     	| 
| --port    	| If you want to override the default port (80) 	| 
| --pause   	| Pauses FAH                                    	| 
| --resume  	| Resume's FAH                                  	| 

### CLI Examples

Pause
```
folding-at-home --host 192.168.1.176 --pause 
```
Resume
```
folding-at-home --host 192.168.1.176 --resume 
```
Full Power
```
folding-at-home --host 192.168.1.176 --power FULL 
```

### Python examples

```.py
from folding_at_home.api import FAHClientAPI
folding = FAHClientAPI(host=host)
folding.resume()
folding.set_power(power_level='LIGHT')
```