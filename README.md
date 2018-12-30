# digital-bookshelf
Keep a digital edition of your bookshelf using G Drive API and a google sheet as the database.

Setup:

Code requires you to setup Google Drive and Google Sheets APIs in Google API Manager. You then must create a crendential in the form of a json download.
Take the email from this file ("client_email") and share your google sheets document with this email (ensure editing permission).
For more detailed instructions (recommended) follow this link to a video by Twilio: https://www.youtube.com/watch?v=vISRn5qFrkM.
#variable names must be altered to match new spreadsheet names
#pip must be installed, following pip installation gspread and oauth2client must be installed
#json file generated from Google API manager must accompany this file

Code:

Using terminal interface and code utilizing Google Drive API, keep a virtual version of your bookshelf. Can easily be modified for any sort of database/list application.
Results in a standard fucntional Google Sheet that acts as the database for the py file. 
