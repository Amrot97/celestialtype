# CelestialType - Astrology Backend API

A Django-based backend API for generating and analyzing natal charts, providing detailed astrological insights and psychological analysis.

## Features

- **Natal Chart Generation**
  - Basic planetary positions
  - House calculations
  - Stellium detection

- **Element Analysis**
  - Fire, Earth, Air, and Water element distribution
  - Element balance analysis
  - Element relationships analysis
  - Psychological implications

- **Modality Analysis**
  - Cardinal, Fixed, and Mutable sign distribution
  - Modality balance insights
  - Behavioral patterns

- **Pattern Analysis**
  - Stellium detection and analysis
  - Element relationship patterns
  - Psychological pattern identification

## Prerequisites

- Python 3.10 or higher (required for natal chart functionality)
- pip (Python package manager)

## Installation

### Local Development Setup

1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application with local settings:
   ```bash
   python run_local.py
   ```

### Production Setup

1. Follow the local setup steps 1-3
2. Configure your production settings
3. Set up your production database
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the production server:
   ```bash
   python manage.py runserver
   ```

## Testing

The project includes an extensive test suite covering:
- Natal chart generation
- Element analysis
- Modality analysis
- Stellium detection
- Element relationships
- Edge cases and corner cases

Run the test suite:
```bash
python manage.py test
```

## API Documentation

The API provides endpoints for:
- Natal chart generation
- Element distribution analysis
- Modality analysis
- Stellium detection
- Element relationship analysis
- Pattern analysis

Detailed API documentation is available in the `docs/` directory.

## Project Structure

- `backend/` - Main Django application
- `natal_chart/` - Natal chart generation and analysis module
  - `views_methods/` - Core analysis implementations
  - `planet_descriptions/` - Planetary position descriptions
- `accounts/` - User management
- `templates/` - HTML templates
- `docs/` - Project documentation
- `tests/` - Test suite

## Development Notes

- Local development uses SQLite for simplicity
- Production should use a proper database (PostgreSQL recommended)
- Some features require Python 3.10+ for full functionality
- AWS credentials are required for production deployment

## License

[Your License Here] 