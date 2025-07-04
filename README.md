
# SUN Tray

A system tray icon for sunset enthusiasts to know about the quality of sunset for the day based on your location.

Note: The quality of sunset is always varying. Please note that this tool is just an indicator not an absolute source of truth.

## Demo

![Alt text](./images/sys-tray-icon.png?raw=true "Sun-Tray System Icon")
<br />
<br />
![Alt text](./images/sun-tray-dialog.png?raw=true "Sun-Tray Dialog")

__I know the design is bad but I am not an UI person person hehe__

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SUNSET_HUE_API_KEY` - Check Sunsethue's API [docs](https://documenter.getpostman.com/view/39964523/2sAYBUDY4W) for information

`LONGITUDE` - Longitude of the location (in WGS84)

`LATITUDE` - Latitude of the location (in WGS84)


## Installation and running the script

Requirements: Python3, pip

- Clone this repository and create virtual environment

```bash
    git clone https://github.com/manalan-km/sun-tray.git
    cd sun-tray
    python3 -m venv venv
```
- Activate virtual env 'venv' based on your platform.
- Install dependencies
```bash
    cd sun-tray
    pip install -r requirements.txt
```
- Run the script
```bash
python3 src/main.py
```
## Acknowledgements

 - [Sunsethue](https://sunsethue.com/)
 - [PySide6](https://github.com/matiassingers/awesome-readme)
 - [Flaticon](https://www.flaticon.com/free-icons/sunset)


