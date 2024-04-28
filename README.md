# Project 5 - Purrfect Matches

[Purrfect Matches](https://purrfect-matches-06bb403f2068.herokuapp.com/)

A fictional cat sanctuary that allows users to view the current in house cats and complete adoption queries in order to hopefully adopt.

![initial_screen](documentation/screenshots/homepage.png)

The homepage for logged in staff members.

![advert_form](documentation/screenshots/create_advert.png)

A screenshot showing the form staff members can use to advertise current cats.

![comment_section](documentation/screenshots/comments.png)

When a user selects an advert, they are taken to that advert's page, where they can find the comment section.

## ERD's

|        Profile      |           |--|  Adverts   |               |           |             
| ------------------- | --------- |--| ---------- | ------------- | --------- |         
| owner               | OnetoOne  |--| ForeignKey | owner         | User      |
| created_at          | DateTime  |--|            | created_at    | DateTime  |
| updated_at          | DateTime  |--|            | updated_at    | DateTime  |
| name                | Char      |--|            | title         | Char      |
| age                 | Integer   |--|            | name          | Char      | 
| email               | Email     |--|            | age           | Char      | 
| mobile              | Char      |--|            | breed         | Char      |
| location            | Text      |--|            | sex           | Char      |
| previously_owned    | Char      |--|            | children      | Char      |
| currently_own       | Text      |--|            | other_animals | Char      |
| relationship_status | Char      |--|            | content       | Text      |
| children            | Char      |--|            | image         | Image     |
| housing             | Char      |--|            |               |           |
| hobbies             | Text      |--|            |               |           |
| preferred_breed     | Char      |--|            |               |           |
| preferred_age       | Char      |--|            |               |           |
| preferred_sex       | Char      |--|            |               |           |
| image               | Image     |--|            |               |           |

|  Comments  |             |           |--| Adoptions  |             |          |             
| ---------- | ----------- | --------- |--| ---------- | ----------- | -------- |        
| ForeignKey | owner       | User      |--| ForeignKey | owner       | User     |
| ForeignKey | advert      | Adverts   |--| ForeignKey | advert      | Adverts  |
|            | created_at  | DateTime  |--|            | created_at  | DateTime |
|            | updated_at  | DateTime  |--|            | name        | Char     |
|            | content     | Text      |--|            | email       | Email    |
|            |             |           |--|            | mobile      | Char     |
|            |             |           |--|            | content     | Text     |

|   Likes    |             |           |            
| ---------- | ----------- | --------- |       
| ForeignKey | owner       | User      |
| ForeignKey | advert      | Adverts   |
|            | created_at  | DateTime  |

## User Experience (UX)

### User Stories

- As a Site User:
  
  - As a site user, I can create a new account so that I can access all the features for signed-up users
  - As a site user, I can view the navbar from every page so that I can navigate easily between pages
  - As a site user, I can see sign-in and sign up options so that I can sign in or sign up
  - As a site user, I can see other user' avatars so that I can quickly identify the various users
  - As a site user, I can view the details of a single advert so that I can learn more about it, and read the comments
  - As a site user, I can view the most recent adverts, ordered by the most recent first so that I can stay up to date
  - As a site user, I can search for adverts with keywords so that I can find the adverts I am most interested in
  - As a site user, I can keep scrolling through the adverts on the site so that I don't have to click on "next page"
  - As a site user, I can find out more information about the adoption centre so that I can find out what they do to help the cats
  - As a site user, I can be informed that I need to sign in or sign up so that I can view the adoption form, and access other features

- As a Registered User:
  
  - As a registered user, I can sign in so that I can access functionality for logged-in users
  - As a registered user, I can like an advert so that I can show my support for the cats that interest me
  - As a registered user, I can view the adverts I liked so that I can easily find the adverts I was interested in
  - As a registered user, I can add comments to an advert so that I can share my thoughts about the ad
  - As a registered user, I can edit or delete my comments so that I can control the content of my comment
  - As a registered user, I can edit my profile so that I can change my profile picture and information
  - As a registered user, I can update my username and password so that I can change my display name and keep my profile secure
  - As a registered user, I can see the adoption form so that I can fill it out

- As a Staff Member:
  
  - As a staff member, I can create adverts so that I can share cats up for adoption to other users
  - As a staff member, I can view, edit, and delete adverts to keep information up to date
  - As a staff member, I can view user profiles so that I can see if they would be a good fir for the potential adoptions
  - As a staff member, I can see the details of completed adoption forms so that I can begin the adoption process

## Technologies Used

### Languages Used



### Frameworks, Libraries, and Programs Used




## Testing

### Validating the Code


### Manual Testing using User Stories from UX Section

### Automated Testing


## Deployment

### GitHub

### Heroku


## Credits

### Code

### Content

### Acknowledgements