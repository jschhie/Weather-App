# Skycast | Flask Weather Report
> - **Live Demo:** https://skycast.pythonanywhere.com/

---

## Tech Stack 
| Component | Tech Used |
| :--- | :--- |
| **Backend** | Python, Flask |
| **Frontend Logic** | JavaScript, Jinja Templating |
| **UI/Styling** | Bootstrap |
| **Deployment** | PythonAnywhere |

---

* A simple web application that displays weather reports for various cities using the <a href="https://openweathermap.org/">OpenWeatherMap</a> API.
* Users can optionally remove queried cities from their view.
* Designed with a responsive layout, styled using Bootstrap and CSS, providing an intuitive user experience.

---

# Visual Demos

| Desktop | Mobile |
| :---: | :---: |
| <img src="https://github.com/jschhie/weather-app/blob/main/demos/desktop-demo.png" width="600"> | <img src="https://github.com/jschhie/weather-app/blob/main/demos/new-mobile-demo.PNG" width="300"> |

---

# Running the App Manually
To launch the virtual environment and run the web application, follow these steps:

## 1. Clone this repository:
```bash
git clone https://github.com/jschhie/weather-app.git [folderNameHere]
```

## 2. Navigate into the folder:
```bash
cd [folderNameHere]
```

## 3. Create virtual environment to isolate project dependencies:
> This project assumes you have `python v3.11` or higher

```bash
/usr/local/bin/python3.11 -m venv venv
```

## 4. Configure environment variables: 

### 4a. Create a `.env` file in the root directory:
```bash
vim .env
```

### 4b. Open the `.env` file and define the following:

> [!NOTE]
> - You can get a free API key at <a href="https://home.openweathermap.org/api_keys">OpenWeatherMap.org</a>.
> - New accounts/keys may take 30–60 minutes to activate after creation.

```
FLASK_SECRET_KEY=any_random_string_here
WEATHER_API_KEY=your_openweathermap_api_key
```

## 5. Activate venv
```bash
source venv/bin/activate venv
```

## 6. Install the required packages as listed in `requirements.txt`:
```bash
pip3 install -r requirements.txt
```

## 7. Run the Flask app:
```bash
python3 main.py
```

This process will create a `weather.db` database in the `instance` directory. You can interact the web app at: http://127.0.0.1:5000 in any web browser.
