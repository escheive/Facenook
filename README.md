

# Facenook
## By Erik Scheive


## Citations

### Used tailwind for my primary css needs
https://v1.tailwindcss.com/

### Flowbite is a library for tailwind
https://flowbite.com/

### For social media site basics I referenced this guide
https://realpython.com/django-social-forms-4/

### For help with making a comment reply section I referenced this guide
https://focusustech.com/blog/create-a-comment-and-reply-system-in-django

### For help with validation errors on signup and login I referenced this forum
https://stackoverflow.com/questions/67852134/how-to-see-if-username-already-exists-in-usercreationfield-django



## Wire Frames

<img width="778" alt="home page" src="https://media.git.generalassemb.ly/user/45843/files/da57cec0-be10-4a6d-88ab-134b47fffc2c">
<img width="776" alt="profile posts" src="https://media.git.generalassemb.ly/user/45843/files/e13e8383-bbe0-457a-8d70-6452097466a5">
<img width="777" alt="profile media" src="https://media.git.generalassemb.ly/user/45843/files/5d0c0617-d51f-4520-a93e-6233e493e06e">
<img width="778" alt="profile likes" src="https://media.git.generalassemb.ly/user/45843/files/757aee84-46da-414d-bef8-3daf0cb27fda">
<img width="776" alt="notifications" src="https://media.git.generalassemb.ly/user/45843/files/9b5f2bb4-5c06-48f9-b5f3-9fd9563bce71">
<img width="776" alt="search" src="https://media.git.generalassemb.ly/user/45843/files/8ed122af-028f-41ae-9f82-154ae22b6f2a">
<img width="772" alt="search results" src="https://media.git.generalassemb.ly/user/45843/files/cf48d351-ad03-470d-89ec-0ae44cf0c8fb">

## Live Site

<img width="1070" alt="Screen Shot 2023-01-23 at 4 38 55 AM" src="https://user-images.githubusercontent.com/115295094/214041723-db5842d1-6ba3-4f2f-a545-c012f9d4d45e.png">
<img width="1065" alt="Screen Shot 2023-01-23 at 4 39 38 AM" src="https://user-images.githubusercontent.com/115295094/214041873-b16de330-5139-45c3-838a-83d2364349a6.png">
<img width="1069" alt="Screen Shot 2023-01-23 at 4 39 54 AM" src="https://user-images.githubusercontent.com/115295094/214041925-035b503f-52c6-4158-b9bc-a571d74b4e0b.png">



## GitHub Repository where the project is stored
** Check out my other projects!**
https://github.com/escheive/Facenook



## User Stories
As HR, I want to see the experience and skills of a candidate on full display
As an engineer, I want to see the full extent of a jumior devs skills so that I can properly evaluate their skills
As a professional connection, I want to know what my connections is capable of so that I can ask questions or recommend them for positions
As a friend, I want to see what my friend has accomplished
As a user, I want to be able to interact with others online, and keep up to date with friends


## PROJECT IDEA

My idea is a social media app, somewhat similar to twitter or Facebook. A place where users can share thoughts and maybe even media with eachother. Something simple where the user can know exactly what their options are on the app, without a tutorial. I am a big fan of functionality and simplicity.


## MODELS

    - Profile
        full crud, tied to that users posts, goal of tied to that users likes and comments(stretch), notifications will be linked to a profile(stretch)

        -- Was able to set up the profile model and likes + comments
        -- No notifications as of now


    - Post
        create/read/delete, tied to posting user and following users?(stretch), will trigger notifications when interacted with(stretch)

        -- Posts are fully functional
        -- No notifications


    - Message(stretch)
        create/read/delete, tied from one profile to another

        -- No messaging system implemented yet

    - Notification(stretch)
        read, will be tied to interactions with posts and sent to that users profile

        -- No notifications as of now




- Table of Required Routes

    |       **URL**        | **HTTP Verb** | **CRUD Action** |         **View**        |
    | -------------------- | ------------- | --------------- | ----------------------- |
    | /                    | GET           | read            | home                    |
    | /about               | GET           | read            | about                   |
    | /profile/:id         | GET           | read            | view_profile            |
    | /profile/:id/edit    | PUT           | update          | editprofile             |
    | /profile/:id/delete  | DELETE        | delete          | deleteprofile           |
    | /accounts/signup     | POST          | create          | registration/signup     |
    | /profile_list/:id    | GET           | read            | profile_list            |
    | /viewpost            | GET           | read            | view_post               |
    | /post                | POST          | create          | Createpost              |
    | /deletepost/:id      | DELETE        | delete          | delete_post             |
    | /explore             | GET           | read            | explore                 |
    | /dashboard           | GET           | read            | dashboard               |
    | /view_comment/:id    | GET           | read            | vie_comment             |
    |                           Not Implemented Yet!!!                                 |
    | /notifications       | GET           | read            | notifications           |
    | /messages            | GET           | read            | messages                |


## STACK

- Was created using Django and Postgresql
- - Database hosted on bit.io
- Failed to implement motion ui with django and switched to tailwind and flowbite with django for the css


## MVP GOALS

- Home page with a main feed with users posts
- - Accomplished
- A profile page that shows all of that profile's content
- - Accomplished
- Authentication that is necessary to interact with others, create an account
- - Accomplished
- Option to like and comment on other user's content
- - Accomplished

## STRETCH GOALS

- Search option on nav that lets you search for other accounts, and even other posts
- - In Progress!
- The option to follow users to receive their content on your page instead of general content, and move the universal content to an explore page
- - Accomplished
- Add a notifications section for when people interact with your content
- - In progress!
- Add an option for direct messages from others
- - In progress!
- Have an option to view posts you have commented on or liked from your profile page
- - In progress!
- Various filter options for explore and viewing on main/profile pages
- - In progress!
- The ability for users to customize their view of the app
- - In progress!


## Key Takeaways

### Motion UI
- Motion UI doesn't have much documentation for use with Django. I decided to go a different route because I was not only new to Django when starting this project, I had never even touched Motion UI.

### Tailwind
- I chose to learn Tailwind instead of Motion UI because it has Django documentation that is easily accessible. Tailwind is great and very easy to use. Very similar to Bootstrap. There are a few snags regarding installing tailwind in an existing Django app that I had to do a couple extra steps to resolve

### Flowbite
- Flowbite is a library that I used for Tailwind. It extends its usage and functionality. I am a huge fan of it but I felt like there was a little more I expected and it seems that there are some known issues that users run into.

### Bulma
- Bulma seems to be the go to css framework to use with Django according to my research and I wish I would've went that route. When i stumbled upon Bulma I already had Tailwind going full speed in my project. If I start another Django project, I will go that route

### Django built-in Auth
- Django has some very handy built in features but changing them is fairly difficult. Overall, I found Django to be easier than express as far as authentication goes.

### Postgres
- Postgres is very easy to use and I prefer it over my experiences with MongoDB
