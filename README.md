# SUPER-H OS 
A Hackathon simulator web game built (_vibe coded_) during a two and a half day AI hackathon, which includes a multi-purposes AI chat and a Lua interpreter using [fengari-web](https://github.com/fengari-lua/fengari-web) (Lua VM).

## Requirements
- **[Web browser](https://en.wikipedia.org/wiki/Web_browser)** (choose your favorite one!)
- **[Python](https://www.python.org)***
- **[Flask](https://flask.palletsprojects.com)***
- **[Mistral AI](https://docs.mistral.ai)** API key*

_*A Python Flask (Web Server Gateway Interface) server has been implemented in order for the AI chat "app" to handle the [Mistral AI API](https://docs.mistral.ai/api) calls from the web game._

## To provision

> [!NOTE]
> _The game can be run/played without the (AI) chat feature and its setup (steps 2,3 and 5) it's not required in this case_

1. Clone the repository, or download and extract the ZIP archive
2. Download and install **Python** from [here](https://www.python.org/downloads), or install it via your preferred package manager
3. Run the following commands in a Linux/macOS terminal (Windows support is untested):
    ```
    pip install flask requests
    ```
    Start the Flask server (_use **python3**, if needed_):
    ```
    python server.py
    ```
4. Open the **_index.html_** file on your browser and enjoy the game/simulator!
5. To use the AI chat feature, enter your Mistral AI API key in the game's settings — obtain the key [here](https://console.mistral.ai/home?profile_dialog=api-keys) after signing up
