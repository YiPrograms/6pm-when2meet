
# 6pm-when2meet

<a href="https://travis-ci.org/ucsb-cs48-w19/6pm-when2meet">
<img src="https://travis-ci.org//ucsb-cs48-w19/6pm-when2meet.svg?branch=master" alt="Build Status">
</a>


## Project summary

### One-sentence description of the project

When-2-meet is a webapp to help groups find an optimal time to meet.

### Additional information about the project

The web app is a convenient way for people to setup the perfect meeting time. The UI/UX is intuitive and our algorithm takes into account even small gaps of availability to provide the user with the optimal time to meet.

## Installation

### Prerequisites
Python Flask
PostgreSQL
Pip

### Installation Steps
- Install pip/Python (pip comes with Python)
- Setup a virtual environment in your project folder and install dependencies
  - Make sure you have installed virtualenv on your computer: ```pip install virtualenv```
  - Check virtualenv version with: ```virtualenv --version```
  - Run the following:
	```bash
	$ cd my_project_folder
	$ virtualenv -p python3 venv
	$ source venv/bin/activate
	$ pip install -r requirements.txt #to install dependencies
	```
- Database setup instructions - PSQL 
	- Install Postgres: ```brew install postgres``` on Mac if you have Homebrew on download it through website on Windows.
		- If you do not have Homebrew, you can install Homebrew here: https://brew.sh/ or you can install postgres manually: https://postgresapp.com/
	- If you are using ubuntu 
	```
	$ sudo apt update
	$ sudo apt install postgresql postgresql-contrib
	$ sudo -u postgres psql
	```
	- Run postgres with: ```psql postgres``` or ```psql -d postgres``` or ```psql```
		- Run following commands to create test database:
			```psql
			CREATE USER when2meet WITH PASSWORD '1234';
			CREATE DATABASE when2meet_dev;
			```
	- On the terminal, run the following commands to do database migrations:
		```
		# python manage.py db init #run this line once to intialize ONLY IF no migrations folder exist
		python manage.py db migrate
		python manage.py db upgrade
		```
- To start the app, run:
	```bash
	$ export FLASK_APP=app.py
	$ flask run
	```
- The terminal should print out a local port to view the working web app.


## Functionality

- Meeting creator gos to the website.
- Meeting creator setups an event with a range of dates and a set period of time.
- Meeting creator shares the link with all the meeting attendees.
- The meeting attendees enter in their availablilities.
- Once all attendees have entered in their availabilities, the meeting creator will be given an optimal meeting time.

## Known Problems

- None so far.


## Contributing

TODO: Leave the steps below if you want others to contribute to your project.

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

If you haven't already, add a file called `LICENSE.txt` with the text of the appropriate license.
We recommend using the MIT license: <https://choosealicense.com/licenses/mit/>

The Value Exchange: users are happy with the result

Heroku Link: https://when2meet-6pm.herokuapp.com/
=======
