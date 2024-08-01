This repository has source code for both, frontend and the backend. 

#### Backend
The backend of this application is written in python flask framework. It is using sqlite database as a backend database. All the database related migration commands can be found in `.vscode/launch.json` file. As the sqlite database is already in the pository, you won't need to apply migration commands etc.

To start the application, you will need to install all the python packages from `backend\requirements.txt` file. In vscode, you can use the following command from the 'debug and run' to start the application.

 `Flask: Run Local Flask App`

 If you prefer to use another IDE, please note that the environemnt variables are in .env.local file, in addition to ones specified in the `.vscode/launch.json: Flask: Run Local Flask App` configuration. 
 
 The backed swagger api documentation should be avilable at http://localhost:5000/api/docs#/

#### Frontend
The frontend of this application is written in React and it uses Material UI for the UI components. All the api requests to the backend are proxied using `poackage.json: 'proxy'` key, therefore it is dependant on backend being available. Once you have installed all the frontend modules using `npm install`, it should load the application when you run `npm start`.

The frontend should be available at http://localhost:3000/ 