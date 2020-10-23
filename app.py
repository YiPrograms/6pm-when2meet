
from flask import Flask
from flask import redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db
from models import Events, Users, TimeRanges
from dotenv import load_dotenv
import os
import datetime
import random, string
import psycopg2
import math

times = [1605985200, 1606071600, 1606158000, 1606244400, 1606330800, 1606417200, 1606503600, 1605986100, 1606072500, 1606158900, 1606245300, 1606331700, 1606418100, 1606504500, 1605987000, 1606073400, 1606159800, 1606246200, 1606332600, 1606419000, 1606505400, 1605987900, 1606074300, 1606160700, 1606247100, 1606333500, 1606419900, 1606506300, 1605988800, 1606075200, 1606161600, 1606248000, 1606334400, 1606420800, 1606507200, 1605989700, 1606076100, 1606162500, 1606248900, 1606335300, 1606421700, 1606508100, 1605990600, 1606077000, 1606163400, 1606249800, 1606336200, 1606422600, 1606509000, 1605991500, 1606077900, 1606164300, 1606250700, 1606337100, 1606423500, 1606509900, 1605992400, 1606078800, 1606165200, 1606251600, 1606338000, 1606424400, 1606510800, 1605993300, 1606079700, 1606166100, 1606252500, 1606338900, 1606425300, 1606511700, 1605994200, 1606080600, 1606167000, 1606253400, 1606339800, 1606426200, 1606512600, 1605995100, 1606081500, 1606167900, 1606254300, 1606340700, 1606427100, 1606513500, 1605996000, 1606082400, 1606168800, 1606255200, 1606341600, 1606428000, 1606514400, 1605996900, 1606083300, 1606169700, 1606256100, 1606342500, 1606428900, 1606515300, 1605997800, 1606084200, 1606170600, 1606257000, 1606343400, 1606429800, 1606516200, 1605998700, 1606085100, 1606171500, 1606257900, 1606344300, 1606430700, 1606517100, 1605999600, 1606086000, 1606172400, 1606258800, 1606345200, 1606431600, 1606518000, 1606000500, 1606086900, 1606173300, 1606259700, 1606346100, 1606432500, 1606518900, 1606001400, 1606087800, 1606174200, 1606260600, 1606347000, 1606433400, 1606519800, 1606002300, 1606088700, 1606175100, 1606261500, 1606347900, 1606434300, 1606520700, 1606003200, 1606089600, 1606176000, 1606262400, 1606348800, 1606435200, 1606521600, 1606004100, 1606090500, 1606176900, 1606263300, 1606349700, 1606436100, 1606522500, 1606005000, 1606091400, 1606177800, 1606264200, 1606350600, 1606437000, 1606523400, 1606005900, 1606092300, 1606178700, 1606265100, 1606351500, 1606437900, 1606524300, 1606006800, 1606093200, 1606179600, 1606266000, 1606352400, 1606438800, 1606525200, 1606007700, 1606094100, 1606180500, 1606266900, 1606353300, 1606439700, 1606526100, 1606008600, 1606095000, 1606181400, 1606267800, 1606354200, 1606440600, 1606527000, 1606009500, 1606095900, 1606182300, 1606268700, 1606355100, 1606441500, 1606527900, 1606010400, 1606096800, 1606183200, 1606269600, 1606356000, 1606442400, 1606528800, 1606011300, 1606097700, 1606184100, 1606270500, 1606356900, 1606443300, 1606529700, 1606012200, 1606098600, 1606185000, 1606271400, 1606357800, 1606444200, 1606530600, 1606013100, 1606099500, 1606185900, 1606272300, 1606358700, 1606445100, 1606531500, 1606014000, 1606100400, 1606186800, 1606273200, 1606359600, 1606446000, 1606532400, 1606014900, 1606101300, 1606187700, 1606274100, 1606360500, 1606446900, 1606533300, 1606015800, 1606102200, 1606188600, 1606275000, 1606361400, 1606447800, 1606534200, 1606016700, 1606103100, 1606189500, 1606275900, 1606362300, 1606448700, 1606535100, 1606017600, 1606104000, 1606190400, 1606276800, 1606363200, 1606449600, 1606536000, 1606018500, 1606104900, 1606191300, 1606277700, 1606364100, 1606450500, 1606536900, 1606019400, 1606105800, 1606192200, 1606278600, 1606365000, 1606451400, 1606537800, 1606020300, 1606106700, 1606193100, 1606279500, 1606365900, 1606452300, 1606538700, 1606021200, 1606107600, 1606194000, 1606280400, 1606366800, 1606453200, 1606539600, 1606022100, 1606108500, 1606194900, 1606281300, 1606367700, 1606454100, 1606540500, 1606023000, 1606109400, 1606195800, 1606282200, 1606368600, 1606455000, 1606541400, 1606023900, 1606110300, 1606196700, 1606283100, 1606369500, 1606455900, 1606542300, 1606024800, 1606111200, 1606197600, 1606284000, 1606370400, 1606456800, 1606543200, 1606025700, 1606112100, 1606198500, 1606284900, 1606371300, 1606457700, 1606544100, 1606026600, 1606113000, 1606199400, 1606285800, 1606372200, 1606458600, 1606545000, 1606027500, 1606113900, 1606200300, 1606286700, 1606373100, 1606459500, 1606545900, 1606028400, 1606114800, 1606201200, 1606287600, 1606374000, 1606460400, 1606546800, 1606029300, 1606115700, 1606202100, 1606288500, 1606374900, 1606461300, 1606547700, 1606030200, 1606116600, 1606203000, 1606289400, 1606375800, 1606462200, 1606548600, 1606031100, 1606117500, 1606203900, 1606290300, 1606376700, 1606463100, 1606549500, 1606032000, 1606118400, 1606204800, 1606291200, 1606377600, 1606464000, 1606550400, 1606032900, 1606119300, 1606205700, 1606292100, 1606378500, 1606464900, 1606551300, 1606033800, 1606120200, 1606206600, 1606293000, 1606379400, 1606465800, 1606552200, 1606034700, 1606121100, 1606207500, 1606293900, 1606380300, 1606466700, 1606553100, 1606035600, 1606122000, 1606208400, 1606294800, 1606381200, 1606467600, 1606554000, 1606036500, 1606122900, 1606209300, 1606295700, 1606382100, 1606468500, 1606554900, 1606037400, 1606123800, 1606210200, 1606296600, 1606383000, 1606469400, 1606555800, 1606038300, 1606124700, 1606211100, 1606297500, 1606383900, 1606470300, 1606556700, 1606039200, 1606125600, 1606212000, 1606298400, 1606384800, 1606471200, 1606557600, 1606040100, 1606126500, 1606212900, 1606299300, 1606385700, 1606472100, 1606558500, 1606041000, 1606127400, 1606213800, 1606300200, 1606386600, 1606473000, 1606559400, 1606041900, 1606128300, 1606214700, 1606301100, 1606387500, 1606473900, 1606560300, 1606042800, 1606129200, 1606215600, 1606302000, 1606388400, 1606474800, 1606561200, 1606043700, 1606130100, 1606216500, 1606302900, 1606389300, 1606475700, 1606562100, 1606044600, 1606131000, 1606217400, 1606303800, 1606390200, 1606476600, 1606563000, 1606045500, 1606131900, 1606218300, 1606304700, 1606391100, 1606477500, 1606563900, 1606046400, 1606132800, 1606219200, 1606305600, 1606392000, 1606478400, 1606564800, 1606047300, 1606133700, 1606220100, 1606306500, 1606392900, 1606479300, 1606565700, 1606048200, 1606134600, 1606221000, 1606307400, 1606393800, 1606480200, 1606566600, 1606049100, 1606135500, 1606221900, 1606308300, 1606394700, 1606481100, 1606567500, 1606050000, 1606136400, 1606222800, 1606309200, 1606395600, 1606482000, 1606568400, 1606050900, 1606137300, 1606223700, 1606310100, 1606396500, 1606482900, 1606569300, 1606051800, 1606138200, 1606224600, 1606311000, 1606397400, 1606483800, 1606570200, 1606052700, 1606139100, 1606225500, 1606311900, 1606398300, 1606484700, 1606571100, 1606053600, 1606140000, 1606226400, 1606312800, 1606399200, 1606485600, 1606572000, 1606054500, 1606140900, 1606227300, 1606313700, 1606400100, 1606486500, 1606572900, 1606055400, 1606141800, 1606228200, 1606314600, 1606401000, 1606487400, 1606573800, 1606056300, 1606142700, 1606229100, 1606315500, 1606401900, 1606488300, 1606574700, 1606057200, 1606143600, 1606230000, 1606316400, 1606402800, 1606489200, 1606575600, 1606058100, 1606144500, 1606230900, 1606317300, 1606403700, 1606490100, 1606576500, 1606059000, 1606145400, 1606231800, 1606318200, 1606404600, 1606491000, 1606577400, 1606059900, 1606146300, 1606232700, 1606319100, 1606405500, 1606491900, 1606578300]
# for local .env imports
load_dotenv()

app = Flask(__name__, static_url_path='', static_folder='static') #/static folder to hold static files by default.

# if env db url exists (i.e. heroku)
DATABASE_URL = os.environ.get("DATABASE_URL")


# setting up default db user (for local use)
POSTGRES = {
	'user': 'when2meet',
	'pw': '1234',
	'db': 'when2meet_dev',
	'host': 'localhost',
	'port': '5432',
}

DATABASE_DEFAULT = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
if DATABASE_URL is not None:
	app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
	conn = psycopg2.connect(DATABASE_URL, sslmode='require')

db.init_app(app)


# route for returning index page
@app.route("/")
def index():
	return render_template('index.html')

# route for returning event page for users to create users
@app.route('/events/<event_token>', methods=['GET', 'POST'])
def event(event_token):
	# show the post with the given id, the id is an integer
	if request.method=='GET':
		e = db.session.query(Events).filter(Events.token==event_token).first()
		if e is None:
			return render_template('404.html')
		else:
			dateS = e.dateStart.strftime('%m/%d/%Y')
			dateE = e.dateEnd.strftime('%m/%d/%Y')
			users = db.session.query(Users).filter(Users.event_id==e.id).all()
			return render_template('event.html', event=e, users=users, dateS=dateS, dateE=dateE)
	if request.method=='POST':
		e = db.session.query(Events).filter(Events.token==event_token).first()
		username=request.form['username']
		u = Users(name=username, event=e)
		db.session.add(u)
		db.session.commit()
		return redirect(url_for('user', event_token=event_token, user_id=str(u.id), submission_success=False))

# route for returning user page
@app.route('/events/<event_token>/<user_id>', methods=['GET', 'POST'])
def user(event_token, user_id):
	e = db.session.query(Events).filter(Events.token==event_token).first()
	if e is None:
		return render_template('404.html')
	u = db.session.query(Users).filter(Users.id==user_id).first()
	if request.method=='GET':
		submission_success = False
		if request.args.get('submission_success'):
			submission_success = request.args.get('submission_success')
		return render_template('userpage.html', event=e, user=u, token=event_token, submission_success=submission_success)
	if request.method == 'POST':
		start_time=request.form['start_time']
		end_time=request.form['end_time']
		t=TimeRanges(user=u, timeStart=start_time, timeEnd=end_time)
		db.session.add(t)
		db.session.commit()
		return redirect(url_for('user', event_token=event_token, user_id=str(u.id), submission_success=True))

# route for returning user personalized edit page
@app.route('/events/<event_token>/<user_id>/edit', methods=['GET', 'POST'])
def user_edit(event_token, user_id):
	e = db.session.query(Events).filter(Events.token==event_token).first()
	if e is None:
		return render_template('404.html')
	u = db.session.query(Users).filter(Users.id==user_id).first()
	if request.method=='GET':
		t = db.session.query(TimeRanges).filter(u.id==TimeRanges.user_id).all()
		return render_template('useredit.html', event=e, user=u, times=t)

# route for deleting time post method
@app.route('/deleteTime/<time_id>', methods=['POST'])
def delete_time(time_id):
	t = db.session.query(TimeRanges).filter(TimeRanges.id==time_id).first()
	if t is None:
		return render_template('404.html')
	u = db.session.query(Users).filter(Users.id == t.user_id).first()
	e = db.session.query(Events).filter(Events.id == u.event_id).first()
	if request.method == 'POST':
		db.session.delete(t)
		db.session.commit()
		return redirect(url_for('user_edit', event_token=e.token, user_id=str(u.id)))

# func: converting time in minutes to nice stringified format
def intToTime(t,e):
	eStartDate=e.dateStart
	eEndDate=e.dateEnd
	minYear = eStartDate.year
	minMonth = eStartDate.month
	minDay = eStartDate.day

	timeTag=""
	time=""
	y = math.trunc(t/525600)
	t=t-y*525600
	m=math.trunc(t/43800)
	t=t-m*43800
	d=math.trunc(t/1440)
	t=t-d*1440

	year=y+minYear
	month = m+minMonth
	day=d+minDay

	if t <60:
		if t %60 <10:
			return "12:0"+str(t) + " AM"
		else:
			return "12:"+str(t) + " AM"
	if t <12*60:
		timeTag=" AM"
		if t %60 <10:
			time = str(month)+"/"+str(day)+"/"+str(year)+" "+str(math.trunc(t/60))+":0"+str(t % 60)+timeTag
		else:
			time = str(month)+"/"+str(day)+"/"+str(year)+" "+str(math.trunc(t/60))+":"+str(t % 60)+timeTag

	if t>=12*60:
		timeTag=" PM"
		if t %60 <10:
			time = str(month)+"/"+str(day)+"/"+str(year)+" "+str(math.trunc(t/60)-12)+":0"+str(t % 60)+timeTag
		else:
			time = str(month)+"/"+str(day)+"/"+str(year)+" "+str(math.trunc(t/60)-12)+":"+str(t % 60)+timeTag

	if t>=12*60 and t<13*60:
		timeTag=" PM"
		if t %60 <10:
			time = str(month)+"/"+str(day)+"/"+str(year)+" "+str(math.trunc(t/60))+":0"+str(t % 60)+timeTag
		else:
			time = str(month)+"/"+str(day)+"/"+str(year)+" "+str(math.trunc(t/60))+":"+str(t % 60)+timeTag



	return str(time)


# func: calculates overlaps over times given list of user times (assuming each element tList is a user's list of times)
def overLap(tList,e):
	masterSet=[]
	userSets=[]


	eStartDate=e.dateStart
	eEndDate=e.dateEnd

	minYear = eStartDate.year
	minMonth = eStartDate.month
	minDay = eStartDate.day

	for i in range(len(tList)):
		tset=set()
		for tr in tList[i]:
			st = tr[0]
			et = tr[1]
			smin = (st.year-minYear)*525600+(st.month-minMonth)*43800+(st.day-minDay)*1440+st.hour*60+st.minute
			emin = (et.year-minYear)*525600+(et.month-minMonth)*43800+(et.day-minDay)*1440+et.hour*60+et.minute
			for i in range(smin,emin+1):
				tset.add(i)

		userSets.append(tset)

	masterSet=userSets[0]
	for i in range (1,len(tList)):

		masterSet=masterSet.intersection(userSets[i])


	masterList= list(masterSet)
	masterList.sort()

	returnList=[]
	prev=0

	for i in range (len(masterList)):
		if i != len(masterList)-1 and masterList[i] != (masterList[i+1]-1):
			t=masterList[prev:i+1]
			prev=i+1
			returnList.append(t)
		if i == len(masterList)-1:
			t=masterList[prev:i+1]
			returnList.append(t)
	cleanRetList=[]
	for l in returnList:
		tup = (min(l),max(l))
		cleanRetList.append(tup)

	return cleanRetList

# route for returning optimal time to meet
@app.route('/events/<event_token>/getTime', methods=['GET'])
def get_time(event_token):
	# show the post with the given id, the id is an integer
	if request.method=='GET':
		e = db.session.query(Events).filter(Events.token==event_token).first()
		if e is None:
			return render_template('404.html')
		else:
			users = db.session.query(Users).filter(Users.event_id==e.id).all()
			users = db.session.query(Users).filter(Users.event==e).all()
			timeList=[]
			for u in users:
				uid=u.id
				t=(db.session.query(TimeRanges).filter(TimeRanges.user_id==uid).all())
				for time in t:
					timeList.append((time.timeStart,time.timeEnd))

			occurrances = dict.fromkeys(times, 0)
			for start, end in timeList:
				for t in times:
					if start <= datetime.datetime.fromtimestamp(t) and \
					   datetime.datetime.fromtimestamp(t) + datetime.timedelta(minutes=15) <= end:
					   occurrances[t] += 1
			colors = {}
			max_val = max(occurrances.values())

			for t, o in occurrances.items():
				colors[t] = "rgba(0, 150, 0, {})".format(0 if max_val == 0 else o/max_val)

			return render_template('getTime.html',colors=colors)

# route for creating an event
@app.route('/create_event', methods=['GET','POST'])
def create_event():
	print('in-create')
	if request.method=='GET':
		return render_template('create.html')
	if request.method=='POST':
		print('in post')
		print(request.form)
		event_name=request.form['event_name']
		start_date=request.form['start_date']
		end_date=request.form['end_date']
		#end_date=start_date
		timeblock=int(request.form['timeblock_hours'])*60+int(request.form['timeblock_min'])
		#10 Digit/Char long Alphanumeric token generated randomly
		token= ''.join(random.choices(string.ascii_letters + string.digits, k=10))
		e = Events(name=event_name, timeblock=timeblock, dateStart=start_date, dateEnd=end_date, token=token)
		db.session.add(e)
		db.session.commit()
		return render_template('token.html', token=token)
