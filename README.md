# Examination-Portal

Welcome to our Online Examination System! This web-based platform allows for seamless online examinations, whether over the internet or intranet, using a computer system.

## Project Overview

Our main goal is to efficiently evaluate students through a fully automated system. This approach not only saves time but also delivers quick and accurate results.

## Tech Stack
- **Database:** MySQL
- **Frontend:** HTML, CSS
- **Backend:** Flask (Python)

## Features

Our examination portal offers a user-friendly interface for both students and staff. Here's a quick look at some key features:

1. **Secure Login:** Ensures only authorized users can access the system.
2. **Student Dashboard:** A personalized space for students to manage their exams.
3. **Staff Dashboard:** Empowers staff to oversee and manage examinations.
4. **Results Page:** Provides instant and accurate exam results.

## Database Structure
We use MySQL for our database, following a carefully designed schema. Check out our schema diagram for a visual representation of the database structure:

### Schema Diagram - 
![Relational Scheme](https://github.com/user-attachments/assets/955ae248-f83a-4eb7-9f95-dab23c278db6)

## User Interface Previews
Get a sneak peek of our intuitive user interfaces:

### Login Page - 
![Login Page](https://github.com/user-attachments/assets/7925a07f-0349-4301-9750-49bb170e4ef7)

### Student Dashboard - 
![Student Dashboard](https://github.com/user-attachments/assets/adfed251-5446-4ce0-b855-b55df83d30b1)

### Staff Dashboard - 
![Staff Dashboard](https://github.com/user-attachments/assets/f553775f-b6d4-4902-8067-ede4601bf048)

### Results Page - 
![Results](https://github.com/user-attachments/assets/c457f5a3-af48-4dc0-bccc-cd65065d0f5f)


## Getting Started
Follow these steps to set up and run the Examination Portal:
1. Set up MySQL tables according to the provided schema. (For examples, check out the `tables` folder)
2. Run `app.py` and access the webpage via localhost.
3. To add new questions to a quiz, insert them into the `questions` table using the appropriate quiz ID.
4. To create a new quiz, add it to the `quiz` table with a new quiz ID.
