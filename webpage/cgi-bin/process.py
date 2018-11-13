# Common Gateway Interface (https://docs.python.org/2/library/cgi.html)
# ==================================================
import cgi
import cgitb
cgitb.enable( display = 0, logdir = "./logs/" )


# Get Form Data
# ==================================================
form = cgi.FieldStorage()
if "hotel_query" not in form:
    print "<p>Please fill in the name and addr fields.</p>"
    return

hotel_result = form.getvalue( "hotel_query" )

# Output to Webpage
# ==================================================

# Headers
print("Content-Type: text/html")

print( '<div class="row">' )
print( '<div class="col-sm-3">' )
print( '<p>Result is {}.</p>'.format(hotel_result) )
print( '</div>' )
print( '<div class="col-sm-9">' )
print( '<p>Result is {}.</p>'.format(hotel_result) )
print( '</div>' )


# HTML Content