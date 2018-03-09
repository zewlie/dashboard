import random

from models import Widget, WidgetItem

COLOR_CLASSES = ["danger", "warning", "success", "info", "brand"]

def select_cc(score):
    if score <= 2:
        color = "brand"
    elif score <=4:
        color = "info"
    elif score <= 6:
        color = "success"
    elif score <= 8:
        color = "warning"
    else:
        color = "danger"
    return color


def create_widget_1():

    i1 = "Finish writing <b>my book</b>"
    i2 = "Make a pile of edible golden eggs, <a href='https://yhoo.it/2C6FpSm'>like these</a>"
    i3 = "Make a <b>wearable project</b> from/inspired by this book: <a href='http://amzn.to/2EsSDL2'><i>Make: Wearable Electronics</i></a>"
    i4 = "Volunteer @ Burning Man"
    i5 = "Fully document an <b>IVF cycle</b>"
    i6 = "Contribute to an open source project"
    i7 = "<b>Sky dive</b>, or something similarly terrifying"
    i8 = "<b>Teach Bert</b> to do an r/dogtraining trick of the month, e.g. <a href='http://bit.ly/2lB6GWg'>mirror me</a>"
    i9 = "Design an educational simulation"
    i10 = "Write a long-form essay"
    i11 = "Run a 5k"
    i12 = "Read <b>50 books</b> in a year"
    i13 = "Do a chin-up"
    i14 = "Write a song"
    i15 = "Grow & harvest a vegetable"
    i16 = "Throw a <b>big party</p>"
    i17 = "Complete a <b>doula training</b> course, e.g. <a href='http://bit.ly/2zXyrxc'>this one</a>"
    i18 = "Do a <b>10+ mile</b> hike"
    i19 = "Lead a training/seminar at work"
    i20 = "Make kombucha from scratch"
    i21 = "<b>Meditate</b> every day for a month"
    i22 = "<b>Repair</b> something currently too damaged to use"
    i23 = "Play D&D"
    i24 = "Attend a conference solo"
    i25 = "Design an <b>escape room</b>"
    i26 = "Attend <b>Sleep No More</b> or similar <a href='http://bit.ly/2wMtklZ'>(See: Sleep No More)</a>"
    i27 = "Host a dinner to connect interesting friends who've never met one another"
    i28 = "Write an interesting Twitter bot"
    i29 = "Finish a painting"
    i30 = "Create a <b>new recipe</b>"

    w1 = Widget(type_id=1, name="<30 Bucket List", size=4)

    i1 = WidgetItem(widget_id=1, text=i1, score=10, color_class=select_cc(10), progress=3)
    i2 = WidgetItem(widget_id=1, text=i2, score=4, color_class=select_cc(4))
    i3 = WidgetItem(widget_id=1, text=i3, score=8, color_class=select_cc(8))
    i4 = WidgetItem(widget_id=1, text=i4, score=7, color_class=select_cc(7))
    i5 = WidgetItem(widget_id=1, text=i5, score=8, color_class=select_cc(8))
    i6 = WidgetItem(widget_id=1, text=i6, score=3, color_class=select_cc(3))
    i7 = WidgetItem(widget_id=1, text=i7, score=5, color_class=select_cc(5))
    i8 = WidgetItem(widget_id=1, text=i8, score=6, color_class=select_cc(6))
    i9 = WidgetItem(widget_id=1, text=i9, score=5, color_class=select_cc(5))
    i10 = WidgetItem(widget_id=1, text=i10, score=4, color_class=select_cc(4))
    i11 = WidgetItem(widget_id=1, text=i11, score=4, color_class=select_cc(4))
    i12 = WidgetItem(widget_id=1, text=i12, score=10, color_class=select_cc(10))
    i13 = WidgetItem(widget_id=1, text=i13, score=6, color_class=select_cc(6))
    i14 = WidgetItem(widget_id=1, text=i14, score=2, color_class=select_cc(2))
    i15 = WidgetItem(widget_id=1, text=i15, score=2, color_class=select_cc(2))
    i16 = WidgetItem(widget_id=1, text=i16, score=5, color_class=select_cc(5))
    i17 = WidgetItem(widget_id=1, text=i17, score=9, color_class=select_cc(9))
    i18 = WidgetItem(widget_id=1, text=i18, score=5, color_class=select_cc(5))
    i19 = WidgetItem(widget_id=1, text=i19, score=4, color_class=select_cc(4))
    i20 = WidgetItem(widget_id=1, text=i20, score=3, color_class=select_cc(3))
    i21 = WidgetItem(widget_id=1, text=i21, score=5, color_class=select_cc(5))
    i22 = WidgetItem(widget_id=1, text=i22, score=3, color_class=select_cc(3))
    i23 = WidgetItem(widget_id=1, text=i23, score=2, color_class=select_cc(2))
    i24 = WidgetItem(widget_id=1, text=i24, score=3, color_class=select_cc(3))
    i25 = WidgetItem(widget_id=1, text=i25, score=6, color_class=select_cc(6))
    i26 = WidgetItem(widget_id=1, text=i26, score=1, color_class=select_cc(1))
    i27 = WidgetItem(widget_id=1, text=i27, score=5, color_class=select_cc(5), progress=10)
    i28 = WidgetItem(widget_id=1, text=i28, score=4, color_class=select_cc(4), progress=100)
    i29 = WidgetItem(widget_id=1, text=i29, score=3, color_class=select_cc(3))
    i30 = WidgetItem(widget_id=1, text=i30, score=3, color_class=select_cc(3))

    i = [i1, i2, i3, i6, i15, i8, i4, i9, i7, i10,
         i11, i12, i13, i14, i16, i17, i18, i19, i20,
         i21, i22, i23, i24, i25, i26, i27, i28, i29, i5, i30]

    return [w1, i]

def create_twitter_widget():

    w1 = Widget(type_id=2, name="@webdevMason", size=5)
    i1 = [WidgetItem(widget_id=2, text="<a class='twitter-timeline' href='https://twitter.com/webdevMason?ref_src=twsrc%5Etfw'>Tweets by webdevMason</a> <script async src='https://platform.twitter.com/widgets.js' charset='utf-8'></script>")]

    return [w1, i1]


def create_photo_widget(wid, img_url):

    w1 = Widget(type_id=3, name="Mason!", size=3)
    i1 = [WidgetItem(widget_id=wid, color_class=random.choice(COLOR_CLASSES), img_url=img_url)]

    return [w1, i1]

