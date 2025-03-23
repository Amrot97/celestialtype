# Running the Astrology Backend Locally Without Database

This guide explains how to run the astrology backend application locally without connecting to the production database.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup Instructions

1. **Clone the repository** (if you haven't already)

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application with local settings**:
   ```bash
   python run_local.py
   ```

   This will:
   - Use SQLite instead of MySQL
   - Create a local database file (db.sqlite3)
   - Run migrations automatically
   - Start the development server

5. **Access the application**:
   The application will be available at http://localhost:8000

## Limitations in Local Mode

- The natal chart functionality is disabled in local mode as it requires Python 3.10+
- AWS credentials are not required
- Some features that depend on the production database may not work
- This is intended for development and testing purposes only

## Troubleshooting

If you encounter any issues:

1. Make sure your virtual environment is activated
2. Ensure all dependencies are installed correctly
3. Check that the local_settings.py file exists in the backend directory
4. If you get database errors, try deleting the db.sqlite3 file and running again
5. If you need the natal chart functionality, you'll need to upgrade to Python 3.10+ 