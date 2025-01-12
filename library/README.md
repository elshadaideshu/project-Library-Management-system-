# Authentication Setup for Library Management API

## Overview

This library management API implements token-based authentication using Django REST Framework (DRF) and Django's built-in authentication system. Users can obtain a token by providing their username and password, which allows them to make authenticated requests to the API endpoints securely.

## Installation Instructions

To set up authentication in your Django project, follow these steps:

1. **Install Required Packages**:
   Ensure you have Django REST Framework and the token authentication module installed. You can install them using pip:

   ```bash
   pip install djangorestframework djangorestframework-authtoken
   