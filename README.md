# Password Generator
#### Video Demo: https://youtu.be/ukeyvRPy9ZU
#### Description:
My project arises because I plan to follow two paths, the first cybersecurity and the second software development, but in principle it was a more complete project for a venture, but I thought I ran the risk of not completing it and enter burnout given the complexity, so I decided to divide it into smaller parts, but still with doubts so I made a consultation to ChatGPT on what was the most appropriate according to the path I want to take, his suggestion was to develop in the first instance the password generator.

I asked ChatGPT for the frontend with a prompt where I described in detail what kind of visual and user interface features I wanted, and then I made the pertinent changes according to my idea. The backend was made by me with the help of web searches, documentation and ChatGPT.

The web app is built using HTML, CSS, JS and Jinja for the frontend and Flask for the backend. The structure of the project follows the one commonly used in web projects elaborated with Flask, which is composed as follows:

    Directories:
    - project -> root or main directory.
    - Static -> for .css and .js files
    - Templates -> for .html files

    Files:
    - app.py as the main backend file, located in the main directory.
    - helpers.py as a support file to have the functions grouped, although in the current version the project only required one function so it was not necessary, but thinking in the further development I consider necessary to have the file ready.
    - styles.css as visual properties and effects file for the frontend, located in the static directory.
    - layout.html as HTML base file where the head, body and in case for future developments the navigation bar and a footer are placed in a fixed way.
    - Index.html where all the frontend code that is shown to the user when generating the password is located.

#### Frontend

For the frontend I had the idea of limiting the generation options based on the NIST recommendations about secure passwords, which should have more than 8 characters, not follow composition rules, among others. So the frontend shows as initial value for the password length the minimum value suggested by NIST, which would be 8 characters and not to follow composition rules allowing the user to decide if he wants numbers, uppercase, lowercase and special characters through checkboxes.

#### Backend

For the backend, in first instance I thought of a function that takes as arguments length, include_numbers, include_uppercase, include_lowercase, include_special. All this to make a verification that the user selected, if there was no selection it would generate the password with the minimum length and all the components (numbers, uppercase, lowercase and special characters), which would represent the default option. Then extending the function I continued with the following verifications such as, for example, if they only wanted numbers or any other possible combination according to the given options.

With all the options I had to generate a secure password, so I started to study how to generalize the randomness following the NIST recommendations (do not follow composition rules), then documenting myself on the web the Python language has a library called secrets which is used to generate secure passwords. In addition, Python also has a library that allows to make use of only numbers, only uppercase or lowercase and special characters, which is called strings, it worked perfect to generate the password using the options offered by the secrets library. All this is in the file helpers.py.

Then in app.py, the operation of the web app as such is defined, where there are two defined paths, which are "/index" and "/generate". In index, the first visual of the password generator is found in principle and in generate the whole process of checking the method used in the request is performed. In order to maintain security and privacy standards, it is verified that the password generation is done through the POST method.

After checking the request.method we proceed to receive the input from the user, in order to pass the arguments to the function generate_password imported from helpers.py. However, I had an error problem in the method, so to understand what was happening I had to use the logging library.
Once the user input is validated and if it is according to the specifications, the generated password is displayed on the screen and the options are unchecked to return to the starting point.


