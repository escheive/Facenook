# Facenook

Citations
https://v1.tailwindcss.com/components/cards
https://flowbite.com/

## Wire Frames

<img width="778" alt="home page" src="https://media.git.generalassemb.ly/user/45843/files/da57cec0-be10-4a6d-88ab-134b47fffc2c">
<img width="776" alt="profile posts" src="https://media.git.generalassemb.ly/user/45843/files/e13e8383-bbe0-457a-8d70-6452097466a5">
<img width="777" alt="profile media" src="https://media.git.generalassemb.ly/user/45843/files/5d0c0617-d51f-4520-a93e-6233e493e06e">
<img width="778" alt="profile likes" src="https://media.git.generalassemb.ly/user/45843/files/757aee84-46da-414d-bef8-3daf0cb27fda">
<img width="776" alt="notifications" src="https://media.git.generalassemb.ly/user/45843/files/9b5f2bb4-5c06-48f9-b5f3-9fd9563bce71">
<img width="776" alt="search" src="https://media.git.generalassemb.ly/user/45843/files/8ed122af-028f-41ae-9f82-154ae22b6f2a">
<img width="772" alt="search results" src="https://media.git.generalassemb.ly/user/45843/files/cf48d351-ad03-470d-89ec-0ae44cf0c8fb">


## GitHub Repository
https://github.com/escheive/Facenook

## User Stories
As HR, I want to see the experience and skills of a candidate on full display
As an engineer, I want to see the full extent of a jumior devs skills so that I can properly evaluate their skills
As a professional connection, I want to know what my connections is capable of so that I can ask questions or recommend them for positions
As a friend, I want to see what my friend has accomplished
As a user, I want to be able to interact with others online, and keep up to date with friends


PROJECT IDEA

My idea is a social media app, somewhat similar to twitter. A place where users can share thoughts and maybe even media with eachother. Something simple where the user can know exactly what their options are on the app. 


MODELS

    Profile
        full crud, tied to that users posts, goal of tied to that users likes and comments(stretch), notifications will be linked to a profile(stretch)

    Post
        create/read/delete, tied to posting user and following users?(stretch), will trigger notifications when interacted with(stretch)

    Message(stretch)
        create/read/delete, tied from one profile to another

    Notification(stretch)
        read, will be tied to interactions with posts and sent to that users profile


- Table of Required Routes

    |       **URL**        | **HTTP Verb** | **CRUD Action** |         **View**        |
    | -------------------- | ------------- | --------------- | ----------------------- |
    | /                    | GET           | read            | home                    |
    | /profile/:id         | GET           | read            | viewprofile             |
    | /profile/:id/likes   | GET           | read            | likes                   |
    | /profile/:id/comments| GET           | read            | viewprofile             |
    | /profile/:id/edit    | PUT           | update          | editprofile             |
    | /profile/:id/delete  | DELETE        | delete          | deleteprofile           |
    | /createprofile       | POST          | create          | createprofile           |
    | /notifications       | GET           | read            | notifications           |
    | /messages            | GET           | read            | messages                |
    | /viewpost            | GET           | read            | viewpost                |
    | /createpost          | POST          | create          | home/profile/createpost |
    | /deletepost/:id      | DELETE        | delete          | viewpost                |
    | /explore             | GET           | read            | explore                 |
    | /deletepost/:id      | DELETE        | delete          | viewpost                |


STACK

Will be created using Django and Postgres
Want to learn Motion UI

MVP GOALS

Home page with a main feed with users posts
A profile page that shows all of that profile's content
Authentication that is necessary to interact with others, create an account
Option to like and comment on other user's content

STRETCH GOALS

Search option on nav that lets you search for other accounts, and even other posts
The option to follow users to receive their content on your page instead of general content, and move the universal content to an explore page
Add a notifications section for when people interact with your content
Add an option for direct messages from others
Have an option to view posts you have commented on or liked from your profile page
Various filter options for explore and viewing on main/profile pages
The ability for users to customize their view of the app
