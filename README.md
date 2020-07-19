# folding-at-home-api-python
Console application (python) to which wraps Folding@Home API for Pause/Restart/Power commands

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
| --http    	| Default is to use HTTPS, use HTTP instead     	| 
| --port    	| If you want to override the default port (80) 	| 
| --pause   	| Pauses FAH                                    	| 
| --resume  	| Resume's FAH                                  	| 

```

folding-at-home --host 192.168.1.176 --pause --http
```
