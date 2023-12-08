from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    video_path = 'basilio.mp4'
    return send_file(video_path, mimetype='video/mp4', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
