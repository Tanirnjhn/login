from flask import Flask,render_template,request
import random,string
a=str(random.randrange(0,9))+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+str(random.randrange(0,9))
app=Flask(__name__)
@app.route('/')
def cap():
    return render_template('captcha.html',captcha=a)
@app.route('/login',methods=['GET','POST'])
def check():
    email=['Tani','Sona','Jhalak']
    pas=['xy','yz','av']
    if(request.method=='POST'):
        x=request.form['email']
        y=request.form['pass']
        z=request.form['captcha']
        if ((x in email and y in pas) and email.index(x)==pas.index(y) and z==a):            
            l='Welcome '+x
            return render_template('captcha.html',output=l)
        elif(x not in email):
            return render_template('captcha.html',Email='Invalid Username')
        elif(y not in pas):
            return render_template('captcha.html',Password='Invalid Password')
        else:
            return render_template('captcha.html',cap='Invalid Captcha')
    return cap()      
if __name__=='__main__':
    app.run()

