"""masondash server."""

import os
from datetime import datetime
from jinja2 import StrictUndefined
from flask import Flask, Markup, render_template, redirect, request, flash, session, jsonify, url_for, abort
from flask_debugtoolbar import DebugToolbarExtension

from temp_data import create_widget_1, create_twitter_widget, create_photo_widget

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = os.environ['FLASK_SECRET_KEY'],
app.jinja_env.undefined = StrictUndefined

# TEMP VARIABLES
#################################################################################

me = {
    "first_name": "Mason",
    "last_name": "Hartman",
    "desc": "vaguely presentable female",
    "avatar_url": "../static/app/media/img/logos/avatar.png"
}

world = {
    "year": datetime.now().year
}

design = {
    "sidebar_items": { 0: {"title": "About",
                           "icon": "flaticon-user",
                           "slug": "about"
                          },
                       1: {"title": "Activity",
                           "icon": "flaticon-open-box",
                           "slug": "activity"
                          },
                       2: {"title": "Reading",
                           "icon": "flaticon-attachment",
                           "slug": "reading"
                          },
                       3: {"title": "Ideas",
                           "icon": "flaticon-cogwheel",
                           "slug": "ideas"
                          }
                     },
    "rows": { 0: { 0: "col-xl-8",
                   1: "col-xl-4"
                 },
              1: { 0: "col-xl-12" },
              2: { 0: "col-xl-4",
                   1: "col-xl-4",
                   2: "col-xl-4"
                 }
            }
          }

widgets = {}

# ROUTES
#################################################################################

@app.route('/')
def index():
    """Homepage."""

    widget1, widget1_items = create_widget_1()
    widgets[1] = {"name": widget1.name, "size": str(widget1.size), "data": widget1_items}

    widget2, widget2_items = create_twitter_widget()
    widgets[2] = {"name": widget2.name, "size": str(widget2.size), "data": widget2_items}

    widget3, widget3_items = create_photo_widget(3, "../static/app/media/img/photos/instagram1.jpg")
    widget4, widget4_items = create_photo_widget(4, "../static/app/media/img/photos/instagram2.jpg")

    widgets[3] = {"name": widget3.name, "size": str(widget3.size), "data": widget3_items}
    widgets[4] = {"name": widget4.name, "size": str(widget4.size), "data": widget4_items}


    return render_template('index.html', title='masondash',
                                         me=me, 
                                         world=world,
                                         design=design,
                                         widgets=widgets)



# RUN
#################################################################################

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = False

    # connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()