import os
#import magic
from datetime import datetime, timedelta
import pickle
import os.path
import urllib.request
from app import app, UPLOAD_FOLDER
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from syllabus import parsetxt, parsepdf, pdfparser
#from gcal import get_calendar_service, postGcal
#from gcalevent import main
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

schedule=False

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
	schedule = False
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			schedule = True
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			path = UPLOAD_FOLDER + filename
			pfile = open(path, 'r')
			parse_dict = {}
			if 'txt' in path:
				parse_dict = parsetxt(pfile)
			if 'pdf' in path:
				parse_dict = parsepdf(pdfparser(filename))
			parse_array = []
			for key, value in parse_dict.items():
				parse_array.append(key + ": " + value)
			for assignment in parse_array:
				flash(assignment)
			return redirect('/authorize')
		else:
			flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
			return redirect(request.url)

@app.route('/authorize')
def authorize():
	SCOPES = ['https://www.googleapis.com/auth/calendar']
	creds = None
	# The file token.pickle stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				'credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)

	# Save the credentials for the next run
	with open('token.pickle', 'wb') as token:
		pickle.dump(creds, token)

	service = build('calendar', 'v3', credentials=creds)
	
	#service = get_calendar_service()

	d = datetime.now().date()
	tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
	start = tomorrow.isoformat()
	end = (tomorrow + timedelta(hours=1)).isoformat()
	for i in len(parse_array) {
		event_result = service.events().insert(calendarId='primary',
			body={
				"summary": key;
				"start.date": value
				"end.date": value
				"reminders": {
					"useDefault": True,
				}
			}
		).execute()
	}

	print("created event")
	print("id: ", event_result['id'])
	print("summary: ", event_result['summary'])
	print("starts at: ", event_result['start']['dateTime'])
	print("ends at: ", event_result['end']['dateTime'])
	return render_template('success.html')

if __name__ == "__main__":
    app.run()