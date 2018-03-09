"""masondash server."""

import os
from datetime import datetime
from jinja2 import StrictUndefined
from flask import Flask, Markup, render_template, redirect, request, flash, session, jsonify, url_for, abort
from flask_debugtoolbar import DebugToolbarExtension

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

# ROUTES
#################################################################################

@app.route('/')
def index():
    """Homepage."""

    return render_template('index.html', title='masondash',
                                         me=me, 
                                         world=world,
                                         design=design)



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