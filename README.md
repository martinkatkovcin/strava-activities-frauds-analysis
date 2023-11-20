# Strava Activity Data Retrieval using Python

This Python script allows you to retrieve your activity data from Strava's API and store it in a local .csv file

## Configuration

1. Create a `.env` file in the project directory with the following content:

```
CLIENT_ID=XXXXXXXX
CLIENT_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
REFRESH_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Replace every field with your data.


## Usage

Run the Python script to retrieve your Strava activity data:

```bash
python main.py
```

Follow the on-screen instructions to authorize the application and retrieve your activity data. The data will be saved to a CSV file in the **data/** directory with current datetime suffix.
