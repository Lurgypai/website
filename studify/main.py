from flask import Flask, request, flash, render_template
from werkzeug.utils import secure_filename
import os
import os.path
import glob

from Studify.studify import studify
from Studify.getpieces import getpieces

app = Flask(__name__)

UPLOAD_FOLDER = 'temp'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

free_slots = []
curr_slot = 0

# this system will get overwhelmed if lots of people connect, but that shouldn't be an issue
def get_slot():
    if len(free_slots) == 0:
        ret = curr_slot
        curr_slot += 1
        return ret
    else:
        return free_slots.pop()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route('/studify/<palette>', methods=['POST'])
def post_img(palette):

    # clear temp
    files = glob.glob('temp/*')
    for f in files:
        os.remove(f)
    
    # check if the post request has the file part
    if 'file' not in request.files:
        return {'res': 'err', 'msg': 'Invalid file type, expected PNG, JPG or JPEG'}
    file = request.files['file']

    if file.filename == '':
        return {'res': 'err', 'msg': 'Invalid file'}
    if file and allowed_file(file.filename):
        palette = secure_filename(palette)
        filename = secure_filename(file.filename)
        filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filename)
        stud_list, output = studify(filename, 'Studify/palettes/' + palette + '.png', getpieces())
        if not stud_list:
            return {'res': 'err', 'msg': 'Invalid image format, expected RGB'}
        return render_template("studify_rendered.html", output = output, pieces = stud_list)

if __name__ == '__main__':
    # this should be modified with host='0.0.0.0' to make the server publicly available
    app.run()
