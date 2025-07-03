# airline-demand-dashboard


# ✈️ Airline Market Demand Dashboard

This is a simple, interactive dashboard built with **Python and Streamlit** to help visualize **airline market demand trends**. It fetches real-time flight data using the [AviationStack API](https://aviationstack.com/) and provides easy-to-understand insights like popular routes, high-demand dates, and top airlines.

It also includes a fun bonus: an **AI-generated summary** of the data using [Cohere AI](https://cohere.com/).

> 📌 This project was created as a test task for **PS Fin Solutions** to demonstrate skills in Python, APIs, data analysis, and web app development.

---

## 🔍 What the App Does

* ✅ Fetches live flight data (arrival, departure, airline, status, etc.)
* ✅ Allows filtering by **origin** and **destination**
* ✅ Shows:

  * **Top 10 most popular routes**
  * **Dates with the highest number of flights**
  * **Airline-wise distribution**
* ✅ Uses AI to summarize the key insights in simple words
* ✅ Built with **free & open tools** like Streamlit, Plotly, and Pandas

---

## 🎥 What It Looks Like

![Dashboard Preview](https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg)

> Interactive filters, charts, and summaries — no coding required!

---

## 🛠️ How to Set It Up

### 1. Clone the project

```bash
git clone https://github.com/urjamodi24/airline-demand-dashboard.git
cd airline-demand-dashboard
```

### 2. (Optional) Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Add your API keys

Create a `.env` file in the root folder like this:

```env
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
COHERE_API_KEY=your_cohere_api_key
```

You can get these keys by signing up at:

* [https://aviationstack.com/](https://aviationstack.com/)
* [https://cohere.com/](https://cohere.com/)

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Your browser will open with the dashboard running locally 🚀

---

## 📊 Example Output

```text
Popular Routes:
From   To     Count
SYD    MEL      12
BNE    CNS      10

High Demand Days:
Date         Count
2025-07-03     100
2025-07-02      90
```

---

## 🧠 AI-Powered Insight

The app uses Cohere's free AI to read the top routes, demand trends, and airline data, and then creates a short summary like this:

> “Most flights were between Sydney and Melbourne. July 3rd was the busiest travel day. Qantas Airways and Jetstar had the highest flight counts.”

Pretty cool, right?

---

## 💼 Tech Stack

* [Streamlit](https://streamlit.io/) – for the dashboard UI
* [AviationStack API](https://aviationstack.com/) – for live flight data
* [Pandas](https://pandas.pydata.org/) – for data processing
* [Plotly](https://plotly.com/) – for interactive visualizations
* [Cohere AI](https://cohere.com/) – for natural language insight generation
* [python-dotenv](https://pypi.org/project/python-dotenv/) – for managing API keys

---

## 📁 Project Structure

```
.
├── app.py                # Streamlit app UI
├── fetch_data.py         # Data fetching and processing
├── .env                  # API keys (keep this private!)
├── requirements.txt
└── README.md
```

---

## 🙋‍♀️ Why This Project?

This dashboard was built as part of a task for **PS Fin Solutions** to demonstrate:

* Real-world API integration
* Clean and structured data processing
* Meaningful visualizations
* Simple UX for non-technical users
* Bonus use of generative AI for summarization

---

## ✅ Next Steps

* [ ] Add historical pricing trends (future scope)
* [ ] Deploy on Streamlit Cloud or Render
* [ ] Add a `.env.example` file for easier setup

---


