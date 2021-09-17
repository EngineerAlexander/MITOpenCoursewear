# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Alexander Ardalan
# Collaborators: Alexander Ardalan

import os
import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory():
    """Class for storing data from parsed RSS feeds."""
    def __init__(self, guid, title, description, link, pubdate):
        """
        Creates an instance of a NewsStory class object.
        Inputs: uniqueID, title, descritpion, link, publishdate.
        """
        
        assert isinstance(guid, str), 'UniqueID is not a string'
        assert isinstance(title, str), 'title is not a string'
        assert isinstance(description, str), 'description is not a string'
        assert isinstance(link, str), 'link is not a string'
        assert isinstance(pubdate, datetime), 'pubdate is not a datetime'
        
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        # will make calls to this fail if another class
        # forgets to define their own evaluate function
        # to remind team to implement the class correctly
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    """
    Child class of Trigger. Used for creating triggers based off of keywords or 'phrases'.
    """
    def __init__(self, phrase):
        """
        Creates a PhraseTrigger object to detect phrases in NewsStorys.
        Input: phrase
        """
        assert isinstance(phrase, str), 'phrase is not a string'
        
        self.phrase = phrase
        
    def is_phrase_in(self, input_text):
        """
        Checks if self.phrase is contained within text string.
        Input: text string
        Output: True or False
        """
        assert isinstance(input_text, str), 'input_text is not a string'
        
        # conditioning input text and creating words list
        input_text = str.lower(input_text)
        for char in string.punctuation:
            input_text = input_text.replace(char, ' ')
        input_text = ' '.join(input_text.split())
        input_text_words = input_text.split()
        
        # conditioning self.phrase and creating words list
        phrase = str.lower(self.phrase)
        for char in string.punctuation:
            phrase = phrase.replace(char, ' ')
        phrase_words = phrase.split()
        for phrase_word in phrase_words:
            # if search word is in parsed text words and search phrase is a subset of text string
            if phrase_word in input_text_words and phrase in input_text:
                pass
            else:
                return False
                
        return True

# Problem 3
class TitleTrigger(PhraseTrigger):
    """
    A child class of PhraseTrigger to search titles for phrases.
    """
    def __init__(self, phrase):
        """
        Instanciate a TitleTrigger object.
        Input: phrase for search
        """
        assert isinstance(phrase, str), 'phrase is not a string'
        
        PhraseTrigger.__init__(self, phrase)
         
    def evaluate(self, story):
        """
        Method for determining if story passed test of filter
        Input: story
        Returns: True or False
        """
        assert isinstance(story, NewsStory), 'story is not a NewsStory'
        
        return self.is_phrase_in(story.get_title())

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    """
    A child class of PhraseTrigger to search descriptions.
    Input: phrase for search
    """
    def __init__(self, phrase):
        """
        Creates an instance of a DescriptionTrigger.
        Input: phrase for searching descriptions
        """
        assert isinstance(phrase, str), 'phrase is not a string'
        
        PhraseTrigger.__init__(self, phrase)
         
    def evaluate(self, story):
        """
        Method for determining if story passed test of filter
        Input: story
        Returns: True or False
        """
        assert isinstance(story, NewsStory), 'story is not a NewsStory'
        
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS note can change timezone to any choosing
timezone = 'EST'

# Problem 5
class TimeTrigger(Trigger):
    """Class for time-based filtering of NewsStory's"""
    def __init__(self, time):
        """
        Creates a TimeTrigger object for date searching capabilities
        Input: Time string in EST format: "%d %b %Y %H:%M:%S" ex. "3 Oct 2016 17:00:10 "
        """
        assert isinstance(time, str), 'time is not a string'
        
        self.date = datetime.strptime(time, "%d %b %Y %H:%M:%S").replace(tzinfo=pytz.timezone(timezone))

# Problem 6
class BeforeTrigger(TimeTrigger):
    """
    Child class of TimeTrigger.
    Used for detecting if a NewsStory's pubdate was before a certain date.
    """
    def __init__(self, timecutoff):
        """
        Creates a TimeTrigger object for date searching capabilities
        Input: Time string in EST format: "%d %b %Y %H:%M:%S" ex. "3 Oct 2016 17:00:10 "
        """
        assert isinstance(timecutoff, str), 'timecutoff is not a string'
        
        TimeTrigger.__init__(self, timecutoff)
        
    def evaluate(self, story):
        """
        Method for determining if story passed test of filter
        Input: story
        Returns: True or False
        """
        assert isinstance(story, NewsStory), 'story is not a NewsStory'
        
        story_date = story.get_pubdate()
        
        # handling for if no timezone information is present in datetime object
        # (for comparison reasons)
        if story_date.tzinfo == None:
            story_date = story_date.replace(tzinfo=pytz.timezone(timezone))
        else:
            story_date = story_date.astimezone(pytz.timezone(timezone))

        return self.date > story_date
    
class AfterTrigger(TimeTrigger):
    """
    Child class of TimeTrigger.
    Used for detecting if a NewsStory's pubdate was after a certain date.
    """
    def __init__(self, timecutoff):
        """
        Creates a TimeTrigger object to filter for stories published after a given date
        Input: Time string in EST format: "%d %b %Y %H:%M:%S" ex. "3 Oct 2016 17:00:10 "
        """
        assert isinstance(timecutoff, str), 'timecutoff is not a string'
        
        TimeTrigger.__init__(self, timecutoff)

    def evaluate(self, story):
        """
        Method for determining if a story meets filter critera
        Input: NewsStory
        Returns: True or False
        """
        assert isinstance(story, NewsStory), 'story is not a NewsStory'
        
        story_date = story.get_pubdate()
        
        if story_date.tzinfo == None:
            story_date = story_date.replace(tzinfo=pytz.timezone(timezone))
        else:
            story_date = story_date.astimezone(pytz.timezone(timezone))

        return self.date < story_date

# COMPOSITE TRIGGERS
# Problem 7
class NotTrigger(Trigger):
    # note can't change what parameters evaluate takes in cause it'll break polymorphism.
    # evaluate still needs to take in story object
    """
    A subclass of Trigger. Used for creating composite not triggers (negating other triggers)
    """
    def __init__(self, trigger):
        """
        Define a NotTrigger instance. Negates how another trigger works.
        Input: trigger
        """
        self.trigger = trigger
        
    def evaluate(self, story):
        """
        Input: story
        Return: True or False
        """
        assert isinstance(story, NewsStory), 'story is not a NewsStory'
        
        return not self.trigger.evaluate(story) # note don't need to pass self here since trigger is another object type

# Problem 8
class AndTrigger(Trigger):
    """
    A subclass of Trigger. Used for creating composite and triggers.
    """
    def __init__(self, trigger1, trigger2):
        """
        Define an AndTrigger instance. Alters how two other triggers work with an AND operator
        Input: trigger1, trigger2
        """
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, story):
        """
        Input: story
        Return: True or False
        """
        assert isinstance(story, NewsStory), 'story is not a NewsStory'
        
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)

# Problem 9
class OrTrigger(Trigger):
    """
    A subclass of Trigger. Used for creating composite or triggers.
    """
    def __init__(self, trigger1, trigger2):
        """
        Define an OrTrigger instance. Alters how two other triggers work with an OR operator
        Input: trigger1, trigger2
        """
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, story):
        """
        Input: story
        Return: True or False
        """
        assert isinstance(story, NewsStory), 'story is not a NewsStory'
        
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Function for taking in a list of NewsStories and a list of Triggers
    then returning a list of stories that passed the filters.
    Input: stories (list), triggerlist (list)
    Returns: filtered_story_list
    """
    assert isinstance(stories, list), 'stories must be a list'
    assert isinstance(triggerlist, list), 'triggerlist must be a list'
    
    stories_to_return = []
    
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                stories_to_return.append(story)
                break
    
    return stories_to_return # just return stories here for no filtering



#======================
# User-Specified Triggers
#======================
# Problem 11

def read_trigger_config():
    """
    FILENAME: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # config file for triggers
    FILENAME = 'triggers.txt'
    
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = '\\' + FILENAME
    file_path = dir_path + file_name
    
    trigger_file = open(file_path, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    trigger_dict = {}

    for string in lines:
        # common code for TITLE DESCRIPTION BEFORE AND AFTER TRIGGERS
        line_split = string.split(',')
        
        t = line_split[0]
        trigger_type = line_split[1]
        trigger_string = line_split[2]
        
        # build all non-composite triggers first
        if (trigger_type == 'TITLE') or (trigger_type == 'DESCRIPTION') or (trigger_type == 'BEFORE') or (trigger_type == 'AFTER'):
            trigger_dict[t] = build_trigger(t, trigger_type, trigger_string)       

    for string in lines:
        # common code for NOT AND OR TRIGGERS
        line_split = string.split(',')
        t = line_split[0]
        trigger_type = line_split[1]
        trigger1 = line_split[2]
        
        # build all composite triggers using non-composite triggers we built first
        if (trigger_type == 'NOT'):
            trigger_dict[t] = build_trigger_from_trigger(t, trigger_type, trigger_dict[trigger1])

        elif (trigger_type == 'AND') or (trigger_type == 'OR'):
            trigger2 = line_split[3]
            trigger_dict[t] = build_trigger_from_trigger(t, trigger_type, trigger_dict[trigger1], trigger_dict[trigger2])
    
    # assemble final list from add line
    implement_triggers = []
    for string in lines: # questionable O but not many triggers
        line_split = string.split(',')
        if line_split[0] == 'ADD':
            for i in range(1, len(line_split)):
                implement_triggers.append(trigger_dict[line_split[i]])
    
    return implement_triggers

# Can use variable or default arguments here to combine functions

def build_trigger(t, trigger_type, trigger_string):
    """
    Function to build a non-composite trigger.
    Inputs: t (trigger ID), trigger_type (TITLE, DESCRIPTION, AFTER, BEFORE), trigger_string
    Output: Trigger of trigger_type
    """
    assert isinstance(t, str), 'Input for t (identity) number is not a string'
    assert isinstance(trigger_type, str), 'Input for Trigger Type is not a string'
    
    assert isinstance(trigger_string, str), 'Input for Trigger String is not a string or Nonetype'
    
    if str.upper(trigger_type) == 'TITLE':
        return TitleTrigger(trigger_string)
        
    elif str.upper(trigger_type) == 'DESCRIPTION':
        return DescriptionTrigger(trigger_string)
    
    elif str.upper(trigger_type) == 'AFTER':
        return AfterTrigger(trigger_string)
    
    elif str.upper(trigger_type) == 'BEFORE':
        return BeforeTrigger(trigger_string)
    
    else:
        raise Exception("Trigger class has no subclass of type '%s'" % trigger_type)
    
def build_trigger_from_trigger(t, trigger_type, trigger1, trigger2 = None):
    """
    Function to build a composite trigger (derivative of other triggers).
    Inputs: t (trigger ID), trigger_type (NOT, AND, OR), trigger1, trigger2
    Output: Trigger of trigger_type
    """
    assert isinstance(t, str), 'Input for t (identity) number is not a string'
    assert isinstance(trigger_type, str), 'Input for Trigger Type is not a string'
    
    assert isinstance(trigger1, Trigger), 'Input for Trigger1 is not a Trigger instance or Nonetype'
    assert isinstance(trigger2, Trigger or None), 'Input for Trigger2 is not a Trigger instance or Nonetype'
    
    if str.upper(trigger_type) == 'NOT':
        return NotTrigger(trigger1)
    
    elif str.upper(trigger_type) == 'AND':
        return AndTrigger(trigger1, trigger2)
    
    elif str.upper(trigger_type) == 'OR':
        return OrTrigger(trigger1, trigger2)
    
    else:
        raise Exception("Trigger class has no subclass of type '%s'" % trigger_type)


SLEEPTIME = 30 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        # code to test
        t1 = TitleTrigger("police")
        #t2 = DescriptionTrigger("Afghanistan")
        #t3 = DescriptionTrigger("Afghanistan")
        #t4 = AndTrigger(t2, t3)
        #triggerlist = [t1, t4]
        triggerlist = [t1]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        #triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            # needs edit to function since some items in yahoo new's rss feed don't contain description
            # updated version of feedparser does not fix
            # edit later and post as new stock ticker tracking project
            #stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

