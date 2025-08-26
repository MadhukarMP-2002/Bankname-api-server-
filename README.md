# Bank API Server 🏦

Hey there! 👋 This is a simple API I built to provide bank branch details. It's a fun project that shows how to fetch data and serve it up with a modern tech stack.

## What's Inside

I used these tools to build the API:
- **Flask**: The Python web framework that powers the API.
- **SQLAlchemy** with **Neon DB**: This is my database duo. They work together to securely store the bank data in the cloud.
- **Gunicorn** and **Render**: These handle the deployment, making sure the API is always up and running for you.

---

## How It Works

The API has two main functions:

### 1. Find a Bank
- **Route**: `GET /banks`
- **What it does**: Gives you a list of all the banks.
- **Example**: `https://your-render-url.onrender.com/banks`

### 2. Find a Branch
- **Route**: `GET /branches/<ifsc>`
- **What it does**: Provides all the details for a specific branch using its IFSC code.
- **Example**: `https://your-render-url.onrender.com/branches/SBIN0001234`

---

## Want to Run This Yourself?

1.  **Clone the project** from GitHub:
    ```bash
    git clone [https://github.com/MadhukarMP-2002/Bankname-api-server-.git](https://github.com/MadhukarMP-2002/Bankname-api-server-.git)
    cd Bankname-api-server-
    ```
2.  **Set up your environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install all the tools**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Connect to a database** by creating a `.env` file and adding your own connection string:
    ```
    DATABASE_URL=your_db_link
    ```
5.  **Fire up the server**:
    ```bash
    python app.py
    ```
    The app will automatically populate the database for you before starting the server.

---

## Did it work? Test it!

I included a set of automated tests in `test.py` to make sure the API endpoints are functioning correctly. To run them, just use this command:
```bash
python test.py

```
## Render link - https://bankname-api-server.onrender.com/ 
