# Folding@Home Client API
This package allows you to manage a Folding@Home client via mocking the same API
calls your browser makes when using the FAHViewer local web portal.
## Install

```env
# deactivate any virtual environments (venv, conda)
cd /tmp
git clone https://github.com/nitrag/folding-at-home-api-python.git
cd folding-at-home-api-python
python3 setup.py install
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