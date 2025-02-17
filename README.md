# ReviseScience Quiz Application 📘📗📙

## Overview  
The **ReviseScience Quiz Application** is an interactive web-based platform designed to help students test and improve their knowledge of **Biology, Chemistry, and Physics**. The application provides an engaging learning experience through carefully curated quiz questions, tracks user progress, and highlights areas for improvement.  

- 📍 Live Site: [ReviseScience](https://project-5-3klq.onrender.com/login/)  
- 📂 GitHub Repository: [Project_5](https://github.com/HKhawaja1/Project_5)  

---

## 🧩 Key Features  

### ✅ User Authentication and Profile Management  
- Secure user registration, login, and logout.  
- Password reset via email.  
- Profile management with quiz performance tracking.  

### ✅ Quiz System with Multiple Categories  
- Quizzes available in three major science disciplines:  
  - 📗 **Biology**  
  - 📘 **Chemistry**  
  - 📙 **Physics**  
- Option for category-specific or randomized quizzes.  
- Multiple-choice questions with an intuitive interface.  

### ✅ Instant Feedback and Scoring  
- Real-time feedback for answers.  
- Score summary at the end of each quiz.  
- Performance history tracking.  

### ✅ Progress Tracking and Leaderboard  
- Personalized dashboard for quiz scores and completion rates.  
- Leaderboard showcasing top-scoring users.  

### ✅ Responsive and User-Friendly Design  
- Built using Bootstrap for full responsiveness.  
- Mobile-friendly and easy-to-navigate interface.  

### ✅ Interactive Contact and About Pages  
- **About page** providing an overview of the application.  
- **Contact form** for inquiries and feedback submission.  

### ✅ Admin Dashboard  
- Full CRUD functionality (Create, Read, Update, Delete) for quiz questions.  
- User and quiz performance management.  
- Access user messages from the contact form.  
- Admin Login: [Admin Dashboard](https://project-5-3klq.onrender.com/admin/login/?next=/admin/)
- Admin Login info provided in the Admin.pdf file 

---

## 🛠️ Technical Highlights  

- **Backend:** Django (Python Web Framework) with PostgreSQL database.  
- **Frontend:** HTML, CSS, Bootstrap, and JavaScript.  
- **Authentication:** Django’s built-in authentication system.  
- **Database Management:** Django ORM (Object-Relational Mapper).  

---

## 🚀 Deploying The App  

### ✅ **Deployment Platform:** [Render](https://render.com/)  

### Steps to Deploy:  
1. Sign up on [Render](https://render.com/).  
2. Click Web Service, connect to your GitHub repository, fill in all the fields and enter the environment variables at the bottom so this doesn't have to be pushed to GitHub and leak your confidential information.
   ![Web Service](https://i.ibb.co/35LzzPsS/Render-1.png)
   ![Connect GitHub](https://i.ibb.co/LH6nsnT/Render-2.png)
3. Don’t forget to create the database. Give it any name you want, choose any of the plans and leave the optional fields empty so they can be randomly generated
   ![Database](https://i.ibb.co/VcmwS3Cm/Render-3.png)
   
   Here are the environment variables you should enter.
   
 - For DB_HOST enter the host name you see in the connections photo down below which is from creating the PSQL database on Render. 
 - For DB_PASSWORD enter the password you see in the PSQL database. 
 - For EMAIL_HOST_PASSWORD enter the app generated password from https://myaccount.google.com/apppasswords
 - For EMAIL_HOST_USER enter the gmail address that you used for the app generated password.
 - For SECRET_KEY enter the secret key you generated from https://djecrety.ir/ which should also be the same in the files on your local machine.
   ![Environment Variables](https://i.ibb.co/Pz58fXS0/Render-Env.png)
   ![Environment Variables](https://i.ibb.co/bRPDZdf8/Render-Env-2.png)

4. Once you have all of this sorted out deploy your web service and click on the link generated to see your app live.
   ![Render URL](https://i.ibb.co/d03PVhwj/Render-4.png)

---

## 📜 Conclusion  

The **ReviseScience Quiz Application** is a comprehensive tool designed to help students revise scientific concepts through interactive quizzes. It features secure authentication, real-time feedback, progress tracking, and a user-friendly interface, making it suitable for learners preparing for exams or seeking to improve their understanding of Biology, Chemistry, and Physics.  

This project demonstrates strong web development skills using Django, PostgreSQL, Bootstrap, and JavaScript, while prioritizing functionality and user experience. 🚀  

---

## 📝 References  

- GitHub Repository: [Project_5](https://github.com/HKhawaja1/Project_5)  
- Live Site: [ReviseScience](https://project-5-3klq.onrender.com/login/)  
- Django Documentation: [Django Official Site](https://www.djangoproject.com/)  
- Bootstrap: [Get Bootstrap](https://getbootstrap.com/)  
- PSQL Database: [Render](https://render.com/)  
