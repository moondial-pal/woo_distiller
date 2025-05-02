# Woo Distiller

A lightweight Flask app that connects to a WooCommerce store, displays products and orders, and optionally stores data to a Google Cloud Storage bucket.

---

## 🚀 Features

* Fetches product and order data from WooCommerce
* Uses mock data when API credentials are not provided
* Displays:

  * Products at `/`
  * Multiple orders at `/orders`
  * A single order at `/single-order`
* Prepares data for optional cloud upload (GCP storage bucket)

---

## 💠 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/woo_distiller.git
cd woo_distiller
```

### 2. Create and activate a virtual environment with Astral UV

#### macOS/Linux (bash/zsh/fish)

```bash
uv venv
source venv/bin/activate
```

#### Windows (PowerShell or cmd)

```powershell
uv venv
venv\Scripts\Activate.ps1  # PowerShell
```

```cmd
venv\Scripts\activate.bat   # Command Prompt
```

### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```

---

## 🧪 Mock Mode (No Credentials Needed)

If `CONSUMER_KEY` or `CONSUMER_SECRET` is not set, the app will automatically fall back to mock data stored in `mock_data/`:

* `mock_order.py` — used at `/single-order`
* `mock_orders.py` — used at `/orders`

---

## 🌐 Usage

### Run the Flask development server

With the included `.flaskenv` file, you can simply run:

```bash
flask run
```

Then visit the following routes in your browser:

* [`/`](http://localhost:5000) — Display product list (live or mock)
* [`/orders`](http://localhost:5000/orders) — Display multiple orders
* [`/single-order`](http://localhost:5000/single-order) — Display a single order

---

## ☁️ Google Cloud Integration (Optional)

To upload data to a GCP bucket, you must:

* Set `GCP_BUCKET_NAME` in your `.env`
* Authenticate using a service account with proper IAM permissions
* Add your upload logic to the app (not included by default)

---

## 📁 Project Structure

```text
woo_distiller/
├── app.py
├── .env.example
├── mock_data/
│   ├── mock_order.py
│   └── mock_orders.py
├── templates/
│   ├── index.html
│   └── orders.html
├── requirements.txt
└── README.md
```

---

## 📄 License

MIT License
