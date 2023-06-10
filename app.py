from flask import Flask,jsonify

app = Flask(__name__)


coureses = [{'name': "Python programing certification",
		    'course_id': "0",
             'Description': "Python programming certification helps you learn"
             "Python in the structured learning path with innovation"
             "Out of the box projeccts maching the industry standrds",
             'price': "visit Google.com to know more"},
             
            {'name': "Java programing certification",
		    'course_id': "1",
             'Description': "Java programming certification helps you learn"
             "Java in the structured learning path with innovation"
             "Out of the box projeccts maching the industry standrds",
             'price': "visit Google.com to know more"}, 

		   {'name': "Java script programing certification",
		    'course_id': "2",
             'Description': "Java script programming certification helps you learn"
             "Java script in the structured learning path with innovation"
             "Out of the box projeccts maching the industry standrds",
             'price': "visit Google.com to know more"},	
            ]


@app.route('/')
def index():
    return "Welcome To The Python Flask REST API"


@app.route("/courses", methods=['GET'])
def get():
    return jsonify({'Courses':coureses})


@app.route("/courses/<int:course_id>", methods=['GET'])
def get_course(course_id):
    return jsonify({'Courses':coureses[course_id]})


@app.route("/courses", methods=['POST'])
def create():
    course =  {'name': "HTML programing certification",
		    'course_id': "3",
             'Description': "HTML programming certification helps you learn"
             "HTML in the structured learning path with innovation"
             "Out of the box projeccts maching the industry standrds",
             'price': "visit Google.com to know more"}
    courses.append(course)
    return jsonify({'Created':course})



if __name__ == "__main__":
    app.run(debug=True)
    