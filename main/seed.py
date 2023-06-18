import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
    host="d6rii63wp64rsfb5.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
    user=os.environ.get('MYSQL_USER'),
    password=os.environ.get('MYSQL_PASSWORD'),
    database="n1505y0w8yse5obu"
)

mycursor = mydb.cursor()

edsql = "INSERT INTO experience_education VALUES (%s, %s, %s, %s)"
edval = [
    (1,'Old Dominion University','2014-05-10','Bachelor of Science degree in Criminal Justice'),
    (2,'Penn State University','2015-12-31','Graduate Level Coursework in Statistics'),
    (3,'Ada Developers Academy','2023','Software Development Bootcamp'),
]

mycursor.executemany(edsql, edval)

exsql = "INSERT INTO experience_experience VALUES (%s, %s, %s, %s, %s)"
exval = [
    (1,'Animal Emergency Critical Care','Customer Service Representative, Receptionist','09/2011 - 07/2014','Worked one on one with clients, in routine, unique and stressful situations, while ensuring their comfort. Performed various administrative and clerical duties such as: the use of Microsoft Office Suite, data entry, filing and invoicing. Peer training and other tasks that expanded on the principles of teamwork, integrity, and commitment to completing goals.'),
    (2,'FocusVision Worldwide','Client Services Representative','11/2014 - 09/2015','Monitored video and audio conferences, provided support for any potential problems. Worked to correct any connectivity, video/ audio or other computer issues. Provided excellent customer service in ensuring the smoothness of each session, and solving any problems which may have arisen.'),
    (3,'FocusVision Worldwide','InterVu Project Coordinator','09/2015 – 07/2021','Coordinated with Market research companies to schedule and organize online market research studies. Extensive data entry, requiring precise attention to detail and superior organizational skills. Troubleshooting, and problem solving for both technical and logistical issues. Provided customer service, by communication with clients, team members and respondents to ensure studies were efficient and without issue.'),
    (4,'Forsta (Formerly FocusVision)','Senior Project Coordinator','07/2021 - 07/2022','Coordinated with Market research companies to schedule and organize online market research studies. Extensive data entry, requiring precise attention to detail and superior organizational skills. Troubleshooting, and problem solving for both technical and logistical issues. Provided customer service, by communication with clients, team members and respondents to ensure studies were efficient and without issue. Assisted with training and onboarding of new team members. Performed complex tasks including difficult bookings, troubleshooting and problem solving with clients, and billing and invoicing questions. Used tools such as Excel VBA to increase productivity.'),
    (5,'Quest Diagnostics','Route Service Representative','12/2021 - 02/2023','Was responsible for the safe and timely transportation of specimens, supplies, reports, equipment and materials to the appropriate destination.'),
    (6,'Forsta','QA Engineer','07/2022 - Present','Tests new and old programs to ensure functionality, and desired effect. Coordinate with developers to ensure that new programs do not interfere with existing architecture, and work as expected. Deploy new code on a biweekly basis into production.'),
]

mycursor.executemany(exsql, exval)

sksql = "INSERT INTO skills_skills VALUES (%s, %s, %s)"
skval = [
    (1,'Technical Support','technical'),
    (2,'Data Entry & Analysis','technical'),
    (3,'Microsoft Office Suite','technical'),
    (4,'Team Leadership','soft'),
    (5,'Interpersonal Communication','soft'),
    (6,'Training','soft'),
    (7,'Staff Supervision','soft'),
    (8,'Python','programming'),
    (9,'C#/.NET/VBA','programming'),
    (10,'C#/.NET','programming'),
    (11,'JavaScript + React','programming'),
    (12,'HTML/CSS','programming'),
    (13,'Records Management','technical'),
    (14,'Java','programming'),
    (15,'Ruby: Rails','programming'),
    (16,'PHP: Laravel','programming')
]

mycursor.execute(sksql, skval)

# update1 = "UPDATE skills_skills SET skill = %s WHERE id = 8"
# update1_val = "Python: Flask, Django"
# mycursor.execute(update1, update1_val)

# update2 = "UPDATE skills_skills SET skill = %s WHERE id = 11"
# update2_val = "JavaScript: React, Vue, Angular"
# mycursor.execute(update2, update2_val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

# example for adding one:
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)