# 🎬 Film Casting System

A full-stack web application for managing film productions, casting actors, assigning roles, and tracking audition history. Built with **Flask**, **MySQL**, and a modern **Bootstrap-based frontend**.

## 🚀 Features

- Add, edit, and delete **films** and **actors**
- Assign **actors to roles** in films
- Search for actors based on **role requirements**
- View **casting history** for each actor
- Responsive and attractive Bootstrap 5 UI
- Organized database structure with normalized relationships

## 🧩 ER Diagram Overview

Entities:
- **Film** (ID, Title, Genre, Release Year)
- **Actor** (ID, Name, Age, Gender, Experience, Contact Info)
- **Role** (ID, Role Name, Description, Requirements)
- **Casting** (Film ID, Actor ID, Role ID, Audition Date, Status)
- **Director** (ID, Name, Contact Info)
- **Crew** (ID, Name, Department, Role in Production)

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: MySQL
- **ORM**: PyMySQL

Clone the Repository

```bash
git clone https://github.com/aryanrajrcotba/Film-Casting-System.git
cd Film-Casting-System

## Create a Virtual Environment
python -m venv venv
venv\Scripts\activate  

## Install Dependencies
pip install -r requirements.txt

## To Run 
python app.py