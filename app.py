from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = 'words'

debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template('home.html', stories=stories.story_list)

@app.route('/story_prompts')
def story_prompts():
    title = request.args['story']
    prompts = stories.story_list[title].prompts
    return render_template('story_prompts.html', story_title=title, prompts=prompts)

@app.route('/your_story')
def your_story():
    prompts = {}
    # for arg in request.args.keys():
    #     prompts[arg] = request.args[arg]
    #print("promts: ", prompts)
    story_select = ''
    args_keys = set(request.args.keys())
    for storyKey in stories.story_list.keys():
        #print ("story prompt set: ", set(stories.story_list[storyKey].prompts))
        if set(stories.story_list[storyKey].prompts) == args_keys:
            story_select = storyKey
            for arg in request.args.keys():
                prompts[arg] = request.args[arg]
            break
    #print("args keys: ", args_keys)
    print("promts: ", prompts)
    story_text = stories.story_list[story_select].generate(prompts)
    print(story_text)
    return render_template('your_story.html', story_text=story_text)