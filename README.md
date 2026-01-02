Demo Project
📌 Overview

This project is a Django REST API that implements user authentication and authorization using JWT. It provides secure user registration, login, and profile access, along with protected routes that can only be accessed by authenticated users.

🚀 Features

User registration with secure password hashing

User login with JWT token generation

Profile API for authenticated users

Token-based authorization for protected routes

Modular app structure (Authentication & Property apps)

🛠️ Tech Stack

Python

Django

Django REST Framework

JWT Authentication

🔐 Authentication Flow

User registers using the register API

User logs in and receives a JWT token

Token is sent in the Authorization header

Authorized routes validate the token and allow access

