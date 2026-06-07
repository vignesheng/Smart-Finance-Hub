<div align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black">
<img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white">

<br><br>

# 📊 Smart Finance Hub

### Real-Time Financial Analytics Platform with Linux Automation & Server Monitoring

[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)]()
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)]()
[![Flask](https://img.shields.io/badge/Flask-REST%20API-black?style=flat-square)]()
[![Database](https://img.shields.io/badge/Database-MySQL-orange?style=flat-square)]()
[![Automation](https://img.shields.io/badge/Automation-Cron%20Jobs-red?style=flat-square)]()
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)]()
[![Developer](https://img.shields.io/badge/Developer-Vignesh%20V-blueviolet?style=flat-square)]()

<br>

> A production-style full-stack financial analytics web application that aggregates
> real-time stock market data, precious metal prices, bank loan rates, EMI calculations
> and financial news into a unified dashboard — powered by a Python Flask REST API,
> MySQL database, Linux cron job automation and live server health monitoring.

<br>

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Professional Highlights](#-professional-highlights)
- [Live Features](#-live-features)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Database Design](#-database-design)
- [API Reference](#-api-reference)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [Automation Setup](#-automation-setup)
- [Server Monitoring](#-server-monitoring)
- [Screenshots](#-screenshots)
- [Future Enhancements](#-future-enhancements)
- [Developer](#-developer)
- [License](#-license)

---

## 🎯 Overview

**Smart Finance Hub** is a full-stack web application developed as a BCA Final Year Project during the academic year 2025–2026. The platform solves a real-world problem — financial data is scattered across multiple websites and platforms. This project consolidates live stock prices, precious metal rates, bank loan comparisons, EMI calculations and financial news into one clean, professional dashboard.

All development — including backend implementation, database design, Linux automation, API integration, monitoring scripts, testing, deployment setup and documentation — was completed independently by **Vignesh V**.

**Core goals of this project:**
- Build a working REST API backend using Python Flask
- Automate real-time data collection using Linux cron jobs
- Implement live server health monitoring using bash scripting
- Design a normalized MySQL database with 7 tables
- Deliver a complete full-stack web application as a solo developer

---

## 🏆 Professional Highlights

| Highlight | Details |
|-----------|---------|
| 🐧 Linux Automation | 3 Python scripts run automatically via cron jobs — no manual input required |
| 📡 REST API Design | 10 endpoints with Blueprint-based modular Flask architecture |
| 🖥️ Server Monitoring | Bash script reads `/proc/stat` directly for accurate CPU metrics every minute |
| 🗄️ Database Design | 7 normalized MySQL tables with foreign key relationships |
| 🔐 Security | Werkzeug password hashing — plaintext passwords never stored |
| 🔑 Secret Management | All API keys and DB credentials managed via `.env` file |
| 📊 Live Dashboard | Admin panel shows real CPU, RAM, Disk usage pulled from `server.log` via regex |
| 🏗️ Modular Codebase | Flask Blueprint architecture — each feature is an independent route module |

---

## ✨ Live Features

| Feature | Description | Data Source |
|---------|-------------|-------------|
| 📈 Stock Market | NIFTY50, SENSEX, BANKNIFTY + 10 top NSE stocks with live prices | Yahoo Finance (yfinance) |
| 🥇 Precious Metals | Gold, Silver, Platinum, Palladium prices in INR per 10g | GoldAPI.io |
| 🧮 EMI Calculator | Monthly EMI with principal, interest and total payment breakdown | Internal Formula |
| 🏦 Bank Rate Comparison | 10+ Indian banks — Home, Car, Bike and Personal loan rates | MySQL Database |
| 📰 Financial News | Latest market news and economic updates | NewsAPI.org |
| ⚙️ Admin Dashboard | Live CPU, RAM, Disk usage + Flask status + user statistics | server.log + MySQL |
| 🔐 Authentication | User registration and login with hashed password storage | MySQL Database |
| 🤖 Auto Data Fetch | Cron jobs fetch and update all market data automatically | Linux Cron |
| 📊 Charts | Interactive financial charts rendered using Chart.js | Chart.js |

---

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                         FRONTEND                             │
│               HTML5 + CSS3 + JavaScript                      │
│          Fetch API → Auto-refresh every 30 seconds           │
│                    Chart.js Visualizations                   │
└──────────────────────┬───────────────────────────────────────┘
                       │ HTTP JSON Requests
                       ▼
┌──────────────────────────────────────────────────────────────┐
│                   FLASK REST API                             │
│                                                              │
│   Blueprint Architecture — Modular Route Files              │
│                                                              │
│   /auth      /stocks    /metals    /news                    │
│   /bank-rates  /emi     /admin/stats  /admin/user-stats     │
│                                                              │
│                  SQLAlchemy ORM Layer                        │
└────────────┬─────────────────────────┬───────────────────────┘
             │                         │
             ▼                         ▼
┌────────────────────┐    ┌────────────────────────────────────┐
│   MySQL Database   │    │         AUTOMATION LAYER           │
│                    │    │                                    │
│  7 Tables:         │◄───│  fetch_stocks.py → every 30 min   │
│  USERS             │    │  fetch_metals.py → daily 6AM       │
│  STOCK_DATA        │    │  fetch_news.py   → daily 6AM       │
│  METAL_PRICES      │    │  monitor.sh      → every minute    │
│  BANK_RATES        │    │                                    │
│  FINANCE_NEWS      │    │  External APIs:                    │
│  EMI_CALC          │    │  → Yahoo Finance (yfinance)        │
│  CHATBOT_LOG       │    │  → GoldAPI.io                      │
│                    │    │  → NewsAPI.org                     │
└────────────────────┘    └────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

**Backend**
- Python 3 — core programming language
- Flask — REST API framework with Blueprint architecture
- SQLAlchemy — ORM for database operations
- Werkzeug — password hashing and security utilities
- PyMySQL — MySQL database connector

**Frontend**
- HTML5 + CSS3 — structure and styling
- JavaScript (Vanilla) — dynamic rendering and API calls
- Fetch API — asynchronous data fetching every 30 seconds
- Chart.js — interactive financial data visualizations

**Database**
- MySQL — primary relational database
- 7 normalized tables with primary and foreign key relationships

**Automation and Monitoring**
- Linux Bash — server health monitoring script
- Cron Jobs — scheduled task automation
- /proc/stat — kernel-level CPU usage reading
- Git + GitHub — version control and code hosting

**External APIs**
- yfinance (Yahoo Finance) — NSE/BSE live stock data
- GoldAPI.io — precious metal prices in INR
- NewsAPI.org — financial news aggregation

---

## 🗄️ Database Design

```
USERS (1) ──────────────────────── (Many) EMI_CALC
│
├── user_id        PK                      emi_id        PK
├── name                                   user_id       FK → USERS
├── email          UNIQUE                  loan_amount
├── password       HASHED                  interest_rate
├── role           user/admin              tenure
└── created_at                             emi_result
                                           created_at

USERS (1) ──────────────────────── (Many) CHATBOT_LOG
                                           chat_id       PK
                                           user_id       FK → USERS
                                           message
                                           response
                                           timestamp

Independent Market Data Tables (No FK — auto-populated by cron jobs)

STOCK_DATA          METAL_PRICES        BANK_RATES
──────────          ────────────        ──────────
stock_id  PK        metal_id  PK        rate_id    PK
symbol              type                bank_name
price               price               interest_rate
date                date                loan_type
                                        updated_at

FINANCE_NEWS
────────────
news_id     PK
title
description
date
```

---

## 📡 API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/auth/register` | Register a new user account |
| `POST` | `/auth/login` | Authenticate user and return user info |
| `GET` | `/auth/users/` | Fetch 10 most recent registered users |
| `GET` | `/stocks/` | Return 20 latest stock prices from DB |
| `GET` | `/metals/` | Return latest precious metal prices |
| `GET` | `/news/` | Return 10 latest financial news articles |
| `GET` | `/bank-rates/` | Return all bank rates grouped by bank name |
| `POST` | `/emi/calculate` | Calculate EMI and save result to DB |
| `GET` | `/admin/stats` | Return CPU, RAM, Disk from server.log |
| `GET` | `/admin/user-stats` | Return live user counts from database |

**Example — `/admin/stats` Response**
```json
{
  "cpu": "2.4%",
  "ram": "5403/15352 MB",
  "ram_percent": "35.19",
  "disk": "6%",
  "flask": "RUNNING"
}
```

**Example — `/stocks/` Response**
```json
[
  { "symbol": "TCS", "price": "3842.50", "date": "2026-06-05T12:00:00" },
  { "symbol": "RELIANCE", "price": "2910.75", "date": "2026-06-05T12:00:00" }
]
```

---

## 📁 Project Structure

```
smart-finance-hub/
│
├── run.py                      # Entry point — starts Flask on port 5000
├── requirements.txt            # All Python dependencies
├── monitor.sh                  # Bash script — logs CPU/RAM/Disk every minute
├── .gitignore                  # Excludes .env, venv/, logs/, __pycache__/
│
├── app/
│   ├── __init__.py             # App factory — DB init + Blueprint registration
│   ├── config.py               # Loads environment variables via python-dotenv
│   ├── models.py               # SQLAlchemy ORM — all 7 table definitions
│   │
│   └── routes/
│       ├── auth.py             # /auth/register  /auth/login  /auth/users/
│       ├── stocks.py           # /stocks/
│       ├── metals.py           # /metals/
│       ├── news.py             # /news/
│       ├── bank_rates.py       # /bank-rates/
│       ├── emi.py              # /emi/calculate
│       └── admin.py            # /admin/stats  /admin/user-stats
│
├── scripts/
│   ├── fetch_stocks.py         # Fetches from Yahoo Finance → STOCK_DATA
│   ├── fetch_metals.py         # Fetches from GoldAPI → METAL_PRICES
│   └── fetch_news.py           # Fetches from NewsAPI → FINANCE_NEWS
│
└── frontend/
    └── SFH_MATES-1.html        # Complete single-page financial dashboard
```

---

## 🚀 Getting Started

**Prerequisites**
- Python 3.8 or higher
- MySQL Server running locally
- Linux OS (recommended for cron automation)
- API Keys from GoldAPI.io and NewsAPI.org

**Installation**

```bash
# 1. Clone the repository
git clone https://github.com/vignesheng/Smart-Finance-Hub.git
cd Smart-Finance-Hub

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Create your .env file
nano .env
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root with the following:

```env
SECRET_KEY=your_flask_secret_key_here
DATABASE_URL=mysql+pymysql://your_username:your_password@localhost/smart_finance_hub
GOLD_API_KEY=your_goldapi_key_here
NEWS_API_KEY=your_newsapi_key_here
```

```bash
# 5. Initialize the database tables
python3 -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all(); print('Tables created successfully')"

# 6. Start the Flask server
python3 run.py
```

**Access the application:**
```
Flask API    →  http://localhost:5000
Frontend     →  Open frontend/SFH_MATES-1.html in your browser
Admin Stats  →  http://localhost:5000/admin/stats
```

---

## 🤖 Automation Setup

All market data is fetched automatically using Linux cron jobs.

```bash
# Open crontab editor
crontab -e

# Add these lines (update paths to match your system)
*/30 * * * * /home/law/smart-finance-hub/venv/bin/python3 /home/law/smart-finance-hub/scripts/fetch_stocks.py >> /home/law/smart-finance-hub/logs/cron.log 2>&1

0 6 * * * /home/law/smart-finance-hub/venv/bin/python3 /home/law/smart-finance-hub/scripts/fetch_metals.py >> /home/law/smart-finance-hub/logs/cron.log 2>&1

0 6 * * * /home/law/smart-finance-hub/venv/bin/python3 /home/law/smart-finance-hub/scripts/fetch_news.py >> /home/law/smart-finance-hub/logs/cron.log 2>&1

* * * * * /bin/bash /home/law/smart-finance-hub/monitor.sh
```

| Script | Schedule | Purpose |
|--------|----------|---------|
| fetch_stocks.py | Every 30 minutes | Yahoo Finance → STOCK_DATA table |
| fetch_metals.py | Daily at 6:00 AM | GoldAPI → METAL_PRICES table |
| fetch_news.py | Daily at 6:00 AM | NewsAPI → FINANCE_NEWS table |
| monitor.sh | Every minute | Logs CPU, RAM, Disk to server.log |

---

## 🖥️ Server Monitoring

The `monitor.sh` bash script runs every minute via cron and appends server health metrics to `logs/server.log`.

**Sample log entry:**
```
--------------------------------------------------
Timestamp: Fri Jun 5 12:45:14 PM IST 2026
CPU Usage: 2.4%
RAM Usage: 5403/15352 MB (35.19%)
Disk Usage: 6%
Flask Status: RUNNING
```

**How CPU is measured:**
```bash
# Reads directly from Linux kernel — reliable on all distributions
CPU=$(awk '/^cpu / {
  idle=$5
  total=$2+$3+$4+$5+$6+$7+$8
  usage=100*(total-idle)/total
  printf "%.1f", usage
}' /proc/stat)
```

The `/admin/stats` Flask route reads `server.log`, extracts the latest entry using Python regex, and serves it as JSON to the admin dashboard in real time.

---

## 📸 Screenshots

> Screenshots of the live application

| Dashboard | Stock Market | Admin Panel |
|-----------|-------------|-------------|
| ![Dashboard]() | ![Stocks]() | ![Admin]() |

| Metal Prices | EMI Calculator | Bank Rates |
|-------------|----------------|------------|
| ![Metals]() | ![EMI]() | ![Banks]() |

---

## 🔮 Future Enhancements

| Enhancement | Description |
|-------------|-------------|
| 🔑 JWT Authentication | Token-based session management for secure API access |
| 📱 Mobile Responsive | Fully responsive design for mobile and tablet devices |
| 📧 Price Alerts | Email/SMS notifications when stock or gold hits target price |
| 📈 Historical Charts | Store and visualize price history over weeks and months |
| 💼 Portfolio Tracker | Let users add and track their personal stock portfolio |
| 🐳 Docker Support | Containerize the app for easy deployment anywhere |
| ☁️ Cloud Deployment | Deploy to AWS EC2 or similar with Gunicorn + Nginx |
| 🔍 Advanced Search | Search and filter stocks, news and bank rates |
| 🌐 Currency Converter | Add INR to USD/EUR/GBP live conversion |
| 🤖 AI Chatbot | Integrate a smarter financial assistant using an LLM API |

---

## 👨‍💻 Developer

**Vignesh V**

All aspects of this project — Full Stack Development,Front End Website, Database Design, REST API architecture, Linux automation, Bash Scripting, Server Monitoring, External API Integration, Frontend Wiring, Testing and Documentation.
- 💼 GitHub: [vignesheng](https://github.com/vignesheng)

---

## 📄 License

This project is developed for educational purposes as a BCA Final Year Project.
Feel free to reference or learn from the code with attribution.

---

<div align="center">

**⭐ If you found this project useful, consider starring the repository!**

<br>

Built with 🔥 by **Vignesh V** — Cloud | DevOps | Python Dev

</div>
