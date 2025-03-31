#!/bin/bash

# Exit on error
set -e

# Update system
echo "Updating system..."
sudo apt update && sudo apt upgrade -y

# Install required packages
echo "Installing required packages..."
sudo apt install python3-pip python3-venv nginx certbot python3-certbot-nginx -y

# Create application directory
echo "Creating application directory..."
sudo mkdir -p /var/www/celestialtype
sudo chown -R $USER:$USER /var/www/celestialtype

# Clone repository
echo "Cloning repository..."
git clone https://github.com/Amrot97/celestialtype.git /var/www/celestialtype
cd /var/www/celestialtype
git checkout test

# Create and activate virtual environment
echo "Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Create .env file
echo "Creating .env file..."
cat > .env << EOL
DJANGO_SECRET_KEY=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
DJANGO_SETTINGS_MODULE=backend.production_settings
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
CORS_ALLOWED_ORIGINS=https://your-domain.com,https://www.your-domain.com
EOL

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Configure Nginx
echo "Configuring Nginx..."
sudo cp celestialtype.conf /etc/nginx/sites-available/
sudo ln -sf /etc/nginx/sites-available/celestialtype.conf /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx

# Configure Gunicorn
echo "Configuring Gunicorn..."
sudo cp celestialtype.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start celestialtype
sudo systemctl enable celestialtype

# Set up SSL with Let's Encrypt
echo "Setting up SSL..."
sudo certbot --nginx -d your-domain.com -d www.your-domain.com

echo "Deployment completed successfully!"
echo "Please update the .env file with your actual domain names and any other required settings." 