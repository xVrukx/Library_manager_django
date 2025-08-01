📚 Library Manager (Django)
A simple Library Management System built with Django that allows managing books, members, borrowing, and returning books efficiently.
Includes a Bootstrap-powered UI for a clean and responsive interface.

🚀 Features
✅ User Profile – Edit and update user details (username, email, password, contact).
✅ Book Management – Add new books with title, author, quantity, and auto-generated publish date.
✅ Member Management – Add and view library members.
✅ Borrow & Return – Borrow books and handle returns with automatic quantity updates.
✅ Bootstrap UI – Clean, responsive design with modals for actions (add book, add member, borrow/return).
✅ Real-Time Tables – Display current books and members dynamically.
✅ Django Messages – Success, error, and warning alerts for user actions.

🛠️ Tech Stack
Backend: Django (Python)

Frontend: HTML, CSS, Bootstrap 5

Database: SQLite (default, can be configured to MySQL/PostgreSQL)

Template Engine: Django Templates

📂 Project Structure
LibraryManager/
├── Library/               # Main app with views, models, urls
│   ├── models.py          # Models: Book, Member, Borrow
│   ├── views.py           # Views for profile, books, members, borrow & return
│   ├── urls.py            # URL routing for app
│   └── templates/
│       └── app.html       # Main UI template
├── LibraryManager/        # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3             # Database (default SQLite)
└── manage.py

⚙️ Installation & Setup
```bash
1️⃣ Clone the repository:
git clone https://github.com/your-username/library-manager.git
cd library-manager

2️⃣ Create and activate virtual environment:
python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

3️⃣ Install dependencies:
pip install -r requirements.txt

4️⃣ Run migrations:
python manage.py migrate

5️⃣ Create superuser (for Django admin):
python manage.py createsuperuser

6️⃣ Run the development server:
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

🔑 Default URLs
Library Dashboard: /Library

Admin Panel: /admin
<img width="1366" height="768" alt="Screenshot (202)" src="https://github.com/user-attachments/assets/0932ecc4-a85f-4703-8ad1-7a3229d00686" />
<img width="1366" height="768" alt="Screenshot (201)" src="https://github.com/user-attachments/assets/42a43508-315c-4813-a776-317d762fea46" />

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss.

📜 License
This project is licensed under the MIT License – feel free to use and modify.
