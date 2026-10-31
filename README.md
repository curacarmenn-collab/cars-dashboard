# Cars Dashboard

A simple Streamlit app for CIS 3590 that explores how a car's specifications relate to its price.

- **GitHub repository:** _add link after publishing_
- **Live app:** _add link after deploying_

## Purpose

A table of 205 cars and 26 columns is hard to read on its own. This app lets a user filter the cars, see them on an interactive chart, and read short findings calculated from the data.

## Dataset

The app uses `cars.csv`, the dataset supplied with the course files. Its original source is not documented, so it is unknown. The app reads the file as it is and does not change it.

- 205 cars and 26 columns, with no missing values and no duplicated rows
- Text columns include `CarName`, `fueltype`, `carbody` and `drivewheel`
- Number columns include `price`, `horsepower`, `enginesize`, `curbweight`, `citympg` and `highwaympg`

Things to know about the data:

- The file does not state its units. The app assumes `price` is in dollars.
- Some brand names in `CarName` are misspelled, such as `maxda` and `toyouta`. The app shows names as written and does not group by brand, so this does not affect its results.
- There is no year column, so the app cannot show changes over time.

## How to Use the App

| Tab | What it shows |
| --- | --- |
| Overview | What the app does and the size of the dataset |
| Data | The matching cars and their descriptive statistics |
| Chart | An interactive scatter plot of a chosen parameter against price, colored by fuel type |
| Insights | The number of cars, average price, average city MPG, the most expensive car, and the correlation between the chosen parameter and price |

Controls:

- **Select a body style** (sidebar dropdown): show all cars or one body style.
- **Select a price range** (sidebar slider): show cars within a price range.
- **Select a parameter** (Chart tab dropdown): choose what to compare with price, which also updates the correlation in the Insights tab.

Hover over a point on the chart to see that car's name and values. Click a fuel type in the legend to hide or show it. If no cars match the filters, the app shows a message asking for a wider price range.

## Running the App Locally

You need Python 3 and pip. The app uses `streamlit`, `pandas` and `plotly`, which are listed in `requirements.txt`.

Run these commands from the folder that contains `cars.csv`, because the app loads the file with a relative path.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run cars_dashboard.py
```

On Windows, activate the environment with `.venv\Scripts\activate` and use `python` instead of `python3`.

If `streamlit` is not found, try `python -m streamlit run cars_dashboard.py`.

## Agile Approach

This was a solo project built in small iterations. It used a prioritized task list and acceptance criteria. It did not use formal Scrum, team meetings or stakeholder reviews.

**Goal:** give a student a simple way to explore how car specifications relate to price.

**User stories**

1. As a student, I want to read what the app and dataset are about, so that I know what I am looking at.
2. As a car shopper, I want to filter cars by body style and price, so that I only see cars I care about.
3. As a student, I want to change what the chart compares with price, so that I can look for patterns.
4. As a reader, I want short findings based on the data, so that I can understand the chart without doing the calculations.

**Task list, in priority order**

| # | Task | Acceptance criteria | Status |
| --- | --- | --- | --- |
| 1 | Load and display `cars.csv` | All 205 cars appear when no filters are set | Done |
| 2 | Add filters | The body style dropdown and price slider work together and update every tab | Done |
| 3 | Add a Plotly chart | The chart has a title, axis labels and a legend, and changes with the selected parameter | Done |
| 4 | Add insights | Values are calculated from the filtered cars | Done |
| 5 | Handle empty and small results | No errors appear with zero or one matching car | Done |
| 6 | Write the README and `requirements.txt` | The steps and dependencies match the app | Done |
| 7 | Publish to GitHub and deploy | The live app opens from a public link | Not started |

**How the work was done**

1. Inspected `cars.csv` and the course examples.
2. Built a first version with many charts and several modules, then decided it was more complex than the assignment needed.
3. Removed that version and rebuilt it as one file that follows the course example `water_dashboard2.py`.
4. Tested the rebuilt app. Testing covered the filters, chart labels, calculated values, empty results, a single matching car, and a copy of the data with missing values.

## Publishing and Deployment

The app needs no API keys or secrets. `cars.csv`, `cars_dashboard.py` and `requirements.txt` must all be in the same repository.

**Publish to GitHub**

1. Use a GitHub repository that you own, such as a fork of the course repository.
2. Commit `cars_dashboard.py`, `requirements.txt`, `README.md`, `.gitignore` and `cars.csv`.
3. Push the commit to your repository and add the link at the top of this file.

**Deploy on Streamlit Community Cloud**

1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
2. Click **Create app**, then choose the option for an app you already have.
3. Choose your repository and the `main` branch.
4. Set the main file path to `cars_dashboard.py`.
5. Optionally choose an app URL, then click **Deploy**.
6. Copy the public `streamlit.app` link and add it at the top of this file.
