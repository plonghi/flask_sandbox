1. --------------------------------------------------------------

To run the application `flask_example.py', just open a terminal in the folder where this file is located, and type:

run flask

If this is the first time that the program is run, proibably one needs to first give this command (just the 1st time)

export FLASK_APP=flask_example.py


2. --------------------------------------------------------------

Then open the browser at the URL given in the shell.
This will be an address like

http://127.0.0.1:5000/

To see the plot, you need to call the execution of a function,
which is done by going to the sub-folder / page

http://127.0.0.1:5000/demo

see the .py file to understand how this works.
Also see files in the subfolder `useful reference'

3. --------------------------------------------------------------

If you want to see all the output in the shell, you can enable debugging mode, by giving this command in the shell (but never do this on a public machine, because this enables arbitrary commands to be executed!)

export FLASK_ENV=development

otherwise the default is 

export FLASK_ENV=production

which doesn't allow debugging nor gives information from stdout in the shell.