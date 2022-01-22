# note_app
Test Django App MVC

A CRUD application that is used to manage notes.
To run it with docker, create a file named <code>.env</code> in the root folder and add in it:
<ul>
  <li>POSTGRES_PORT=5432</li>
  <li>POSTGRES_HOST='db'</li>
  <li>RUN_DOCKER=1</li>
  <li>POSTGRES_DB=Database Name</li>
  <li>POSTGRES_USER=Database User</li>
  <li>POSTGRES_PASSWORD=Database Password</li>
</ul>
And run the <code>docker-compose up</code> command. <br />
If you want to run locally
install the dependencies with the <code>pip install -r requirements.txt</code> command, <br />
then do the migration with the <code>python manage.py migrate</code> command, <br />
finally run the server with the <code>python manage.py runserver</code> command. <br />
The main view is the list of notes at <a href='http://127.0.0.1/notes/note_list/' target='_blank'>Link</a>.
