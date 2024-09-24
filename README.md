# Flask Weather Web App

* A simple web application that displays weather reports for various cities using the <a href="https://openweathermap.org/">OpenWeatherMap</a> API.
* Users can optionally remove queried cities from their view.
* Designed with a responsive layout, styled using Bootstrap and CSS, providing an intuitive user experience.

# Visual Demo
<img src="https://github.com/jschhie/weather-app/blob/master/new-demo.png" alter="Demo of weather web app">

# Running the App Manually
To launch the virtual environment and run the web application, follow these steps:

1. Clone this repository:
```bash
git clone https://github.com/jschhie/weather-app.git [folderNameHere]
```

2. Navigate into the folder:
```bash
cd [folderNameHere]
```
  
3. Install the required packages as listed in the `Pipfile`:
```bash
pipenv install
```

4. Activate the virtual environment:
```bash
pipenv shell
```

5. Run the Flask app:
```bash
python3 main.py
```

This process will create a `weather.db` file inside the `instance` directory. You can interact the web app at: http://127.0.0.1:5000 in any web browser.
