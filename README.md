## event-manager
=====================

This is a simple event manager app - built to learn Django REST and React.


### Setup

To run the backend simply have Docker installed on your machine and run `make up`

If you are running the first time you will need to run `make migrate` to run the migrations

To run the frontend you can use:
- cd client
- npm install
- npm start

We will later move this into its own docker image.


### Scope

The scope of the application is very simple. We are looking to create a simple event management application, where our
local community leaders can manage their events, and notify anybody subscribed to an event or organisation with updates.
We will maintain tickets as issues


### Resources

Since we are all learning - it will be best to have a single place to document all the resources. I will add the initial
ones here, but we should update them as we learn new things and find additional resources.

#### Django

So a few things to know before diving in - we are mostly focused on Django REST API - not the standard Django framework
which normally does server side rendering. So the focus of learning should be how to create the models, and their
relationships. After that is all the API stuff like serialization, views, urls, authentication, permissions and migrations.

Another thing to note here is that many articles and tutorials are seriously dated, the video below is the only resource
I have found which is using the latest ViewSets available. Im not sure of the backward compatibility as yet so dont know
how well the old code works. This is Django2 with Django REST framework 3.8 and Python 3.6.

- http://www.django-rest-framework.org/tutorial/quickstart/
- http://blog.kevinastone.com/getting-started-with-django-rest-framework-and-angularjs.html
- https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ/videos
- https://teamtreehouse.com/library/django-rest-framework
- https://www.udemy.com/django-python/
- https://godjango.com/41-start-your-api-django-rest-framework-part-1/
- https://www.digitalocean.com/community/tutorials/how-to-scale-django-beyond-the-basics
- https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html
- https://thinkster.io/topics/django
- https://realpython.com/django-rest-framework-quick-start/
- https://www.andreagrandi.it/2016/09/28/creating-production-ready-api-python-django-rest-framework-part-1/


#### React

- https://www.youtube.com/watch?v=MhkGQAoc7bc&list=PLoYCgNOIyGABj2GQSlDRjgvXtqfDxKm5b
- https://egghead.io/courses/the-beginner-s-guide-to-react
- https://egghead.io/courses/getting-started-with-redux
- https://redux.js.org/basics/usage-with-react
- https://github.com/enaqx/awesome-react
- https://www.udemy.com/react-redux-tutorial/
- https://learnreact.com/lessons/2018-the-context-api-overview
- https://www.educative.io/collection/5687753853370368/5707702298738688
- https://github.com/markerikson/react-redux-links
- https://camjackson.net/post/9-things-every-reactjs-beginner-should-know
- https://engineering.siftscience.com/best-practices-for-building-large-react-applications/
- https://www.youtube.com/watch?v=PF0Vi-iIyoo&index=28&t=0s&list=PLb0IAmt7-GS3fZ46IGFirdqKTIxlws7e0
- https://tylermcginnis.com/courses/react-fundamentals-udacity/
