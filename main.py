from flask.templating import render_template
import requests
from flask import Flask,redirect,render_template_string,request,g,session
import socket
app = Flask(__name__)
app.secret_key = "1234"
ip = socket.gethostbyname(socket.gethostname())
port = 80
def referral():
    url = request.referrer
@app.route("/283457/home")
def hhm():
     resp =  requests.get(session["domain"])
     an = resp.content
     resp.close()
     return an
    
@app.route('/<path:path>',methods = ["GET","POST"])
def hh(path):
    for x,i in enumerate(path):
        if i == "/":
            if path[0:x] == str(283457):
                path = path[x:]
                break
            else:
                break
    if "domain" not in session:
        return redirect("/")
    url = ""
    for i in request.args:
        url += i + "=" + request.args[i]+"&"
    if request.method == "GET":
        try:
            resp = requests.get(session["domain"]+"/"+path+"?"+url,cookies = session["cookies"])
        except:
            resp = requests.get(session["domain"]+"/"+path+"?"+url)
    else:
        try:
            resp = requests.post(session["domain"]+"/"+path+"?"+url,cookies = session["cookies"],data = dict(request.form))
        except:
            resp = requests.post(session["domain"]+"/"+path+"?"+url,data = dict(request.form))
        session["cookies"] = resp.cookies.get_dict()
    an = resp.content
    resp.close()
    return str(an) + session["domain"]+path+url

@app.route("/",methods = ["GET","POST"])
def main():
    if request.method == "POST":
         session["domain"]= "http://"+request.form["domain"]
         return redirect("/283457/home")
    return render_template("home.html")
    
if __name__ =="__main__":
    app.run(host=ip,port = port)