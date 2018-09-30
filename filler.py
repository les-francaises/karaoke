#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import csv, unicodedata, re
from slugify import slugify

def strip_accents(text):
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)


def text_to_id(text):
    """
    Convert input text to id.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    text = strip_accents(text.lower())
    text = re.sub('[ ]+', '_', text)
    text = re.sub('[^0-9a-zA-Z_-]', '', text)


with open(r'karaoke.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';', quotechar='"')
    for r in reader:
        title=strip_accents(r[0])
        artist=strip_accents(r[1])
        title_slug=slugify(title)
        artist_slug=slugify(artist)
        complete=str(artist+' '+title)
        slug_complete=slugify(complete)
        first_letter=ord(slug_complete[0])
        print complete, slug_complete, str(first_letter)

        file = open("_posts/" + str(first_letter) + "-01-01-" + slug_complete + ".md","w")

        file.write("---\r\n")
        file.write("layout: post\r\n")
        file.write("title: "+title+"\r\n")
        file.write("author: "+artist+"\r\n")
        file.write("language: \"Français\"\r\n")
        file.write("image:\r\n")
        file.write("  artist: "+artist_slug+".png\r\n")
        file.write("---")

        file.close()
