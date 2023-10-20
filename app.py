from flask import Flask, render_template, request
from your_module_name import Youtube_Comment  # Replace with the actual module name containing your code

app = Flask(__name__)

@app.route('/interact', methods=['POST'])
def interact_with_youtube():
    video_id = request.form['video_id']
    comment_text = request.form['comment_text']

    my_comment = Youtube_Comment()
    my_comment.authenticate()  # Initialize the YouTube API authentication

    comment_info = my_comment.post_comment(video_id, comment_text)
    # Add more logic for replies and other interactions as needed

    return render_template('result.html', comment_info=comment_info)
if __name__ == '__main__':
    app.run(debug=True)
