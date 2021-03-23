import cgi
form = cgi.FieldStorage()
sdate_form =  form.getvalue('sdate')

print("Start Date was " + sdate_form)
