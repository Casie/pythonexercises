# Extracting links
# Take the beginning of a tag/text
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.
# page = has the content of web page as a string

page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/">'''

start_link = page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote+1)
url = page[start_quote+1:end_quote]   
