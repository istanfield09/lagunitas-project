# Homework Project

## Lagunitas Brewing Co.

*Disclaimer: The task we are asking you to perform is not going to provide us with any value. We are using this solely for purposes of evaluation job applicants.*

### Assignment
You have been given a Django web application that allows the user to create beer ratings. Please extend this to:

* Allow the user to edit an existing rating. Each rating in the list at `/home/` should have a link that can be clicked on that takes the user to a page where the rating can be edited and changes saved (as a group; you don’t need to support saving individual changes). Editing should be cancelable.
* Allow the user to delete a beer rating from the application.
* Add a field to the beer rating that lets the user set the brewery name for the beer being rated. This value is persisted in the database. This must also be editable. Note that Django has support for database schema changes, called "migrations".
* Change the functionality of the "New" button so that it shows the beer rating creation form on the same page, instead of linking to a different page. The form should be hidden until the button is pressed. 
* The form for entering rating information looks pretty bad. Can you make it look better? (This is obviously subjective.)
 
Some of this will likely involve client-side coding.

You will be graded on correctness, the cleanliness/readability of your code, and the computational complexity of your implementation.

This is open-book! Feel free to look up anything you want. The [Django documentation](https://docs.djangoproject.com/en/1.11/) is very thorough.

When you are done, please send an email to Matthew Wyatt with instructions for retrieving and running your submission. Emailed submissions won't be accepted. If your instructions direct us to clone a git repo - that's bonus points!

### Installation instructions
The instructions assume you are running on a *nix OS, either OS X or Linux (they were only tested on OS X). If you are running on Windows, contact Matthew Wyatt for support.

Prerequisites:

* Python 2.7.x
* Virtualenv (See [the installation page](https://virtualenv.pypa.io/en/latest/installation.html) for instructions). (Technically, virtualenv isn't required, but this can help prevent library version conflicts with whatever other python software is on your system, and is strongly recommended.)

Instructions

(These are assumed to be run from within the directory where this file is.)

1. Create a virtual environment: `virtualenv ./venv`
2. Activate the virtual environment: `source venv/bin/activate`
3. Install project dependencies: `pip install -r requirements.txt`
4. Run the database migrations: `python manage.py migrate`
5. Run the Django development server: `python manage.py runserver`
6. Navigate your browser to [http://127.0.0.1:8000/](http://127.0.0.1:8000/). You should see a table with two beer ratings already present.
7. You can also run the tests: `python manage.py test`

If you want to install any additional python libraries, please use the `pip` installed with virtualenv, and update the `requirements.txt` appropriately, so we can run the same code.

Included in this assignment are recent versions of Bootstrap and jQuery. These could be helpful for some of your requirements, but aren't mandatory. And if you want to use additional 3rd-party javascript or css, please download it and link to your local copy (rather than using a CDN, for example). Be sure to include it in your submission as well so we see what you see.

Have fun!


