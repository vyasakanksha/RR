from itertools import groupby, chain
from flask import current_app, Flask, render_template, request, jsonify, make_response
from robot import Robot

app = Flask(__name__)

# Add a root route. This is currently set to home.html
@app.route("/", methods=['GET', 'POST'])
def home():
   position = None  
   orientation = None

   # Errors, if any, else log for successful play
   message = None
   if request.method == 'POST':
      try:
         if request.form['button'] == 'place':
            data = request.form.to_dict(flat=True)
            test = Robot(int(data['x']), int(data['y']), data['f'])
            message = test.msg
         if request.form['button'] == 'move':
            message = test.move()
            message = test.msg
         if request.form['button'] == 'left':
            message = test.left()
            message = test.msg
         if request.form['button'] == 'right':
            message = test.right()
            message = test.msg

         position = test.pos
         orientation = test.orient

      except NameError:
         message = "Error: Place the Robot on the Board"
      except AttributeError:
         message = "Error: Place the Robot on the Board"
      
   return render_template('robot.html', pos=position, orient=orientation,msg=message)

if __name__ == "__main__":
    app.run(debug=True)
