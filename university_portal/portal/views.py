from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Contact,Marks
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import os
import cv2
from .lbl import label
from django.views.generic import View
from .utils import render_to_pdf
from django.template.loader import get_template
from .utils import render_to_pdf
import pickle
import face_recognition
import numpy as np

def home(request):
    return render(request, 'home.html')

def gallery(request):
    return render(request, 'gallery.html')

def Courses(request):
    return render(request, 'test.html')

def contact(request):
    # messages.error(request,'Welcome to contact')
    if request.method =='POST':
        print("we are using post")
        name = request.POST['cname']
        email = request.POST['cemail']
        roll = request.POST['croll']
        query = request.POST['query']
        print(name, email, roll, query)

        if (len(name) < 2) or (len(email) < 3)  or (len(query)< 3):
            messages.error(request, 'Please fill the form correctly')
        else:
            contact = Contact(cname=name, cemail=email,query=query, croll = roll)
            contact.save()
            messages.success(request,'Your message has been sent')
    return render(request, 'contact.html')


def test(request):
    return render(request, 'test.html')


def handlesignup(request):
    if request.method == "POST":


        #get parameter
        username = request.POST['username']
        firstname = request.POST['firstname']
        lasttname = request.POST['lasttname']
        birthday = request.POST['birthday']
        userrollno = request.POST['userrollno']
        useremail = request.POST['useremail']
        userpassward = request.POST['userpassward']
        conuserpassward= request.POST['conuserpassward']

        #input validations
        if len(username) >15:
            messages.error(request, 'Username must  under 10 characters')
            return redirect('home')
        if len(username) <4:
            messages.error(request, 'Username must  greater than 4 characters')
            return redirect('home')
        # if username.isalnum():
        #     messages.error(request, 'Username should only contain characters and numbers')
        #     return redirect('home')
        if userpassward != conuserpassward :
            messages.error(request, 'Password do not match')
            return redirect('home')

        # create user
        # username=username.lower
        myuser = User.objects.create_user(username=username, email=useremail, password=userpassward)
        myuser.first_name = firstname
        myuser.last_name = lasttname
        myuser.save()
        Subject_Networking = -1
        Subject_java = -1
        Subject_c = -1
        Subject_python = -1


        student_marks = Marks(username=username, email=useremail, first_name=firstname, last_name=lasttname,
                              birthday=birthday, rollno=userrollno, Subject_c=Subject_c, Subject_java=Subject_java,
                              Subject_Networking=Subject_Networking, Subject_python=Subject_python)
        student_marks.save()

        messages.success(request, 'Your account has been successfully  created')

        # storing and registering the images for face recognition

        entry(username);
        # entry_image(username);
        # labal();
        # os.system('python label.py')
        # label();

        face_rec_id_pass = {username: userpassward}
        if os.path.isfile("dict.pickle"):
            pickle_in = open("dict.pickle", "rb")
            face_rec_id_pass = pickle.load(pickle_in)
            print(face_rec_id_pass)
            pickle_in.close()

        if len(face_rec_id_pass) == 0:
            face_rec_id_pass = {username: userpassward}
        else:
            f = {username: userpassward}
            face_rec_id_pass.update(f)

        pickle_out = open("dict.pickle", "wb")
        pickle.dump(face_rec_id_pass, pickle_out)
        pickle_out.close()
        return (redirect('home'))
    else:
        messages.error(request, 'Please fill the form correctly')


def handlelogin(request):

    if request.method == "POST":
        #get parameter


        username = request.POST['loginusername']
        psw = request.POST['loginuserpassward']
        user = authenticate(username=username, password=psw)
        if user is not None:
            login(request,user)
            messages.success(request, 'Successfully login')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials login failed,Please try again')
            return redirect('home')


def handlelogout(request):
        logout(request)
        messages.success(request, 'Successfully logout')
        return redirect('home')



def marks(request):
    all = Marks.objects.all()
    first_name = ""
    last_name = ""
    rollno = 0
    Subject_c = 0
    Subject_Networking = 0
    Subject_java = 0
    Subject_python = 0
    email = ""
    birthday = 0

    for student in all:

        if (str(student.username) == str(request.user) ):
            username = student.username
            first_name = student.first_name
            last_name = student.last_name
            rollno = student.rollno
            Subject_c = student.Subject_c
            Subject_Networking =student.Subject_Networking
            Subject_java =student.Subject_java
            Subject_python =student.Subject_python
            email =student.email
            birthday =student.birthday

            username = username.capitalize()
    content = {'username': username, 'first_name': first_name, 'last_name': last_name , 'rollno' : rollno, 'Subject_c': Subject_c , 'Subject_Networking': Subject_Networking ,
               'Subject_java' : Subject_java, 'Subject_python': Subject_python, 'email' : email ,'birthday' :birthday }


    # print(content)
    return render(request,'Report_card.html', {'a': content})


def face(request):

    if request.method == "GET":
        permistion = request.GET.get('face_recogn', 'off')

    if permistion == "on":
        # m = check();
        m=face_recogn();
        print(m)
        if m is not None:
            if os.path.isfile("dict.pickle"):
                pickle_in = open("dict.pickle", "rb")
                face_rec_id_pass = pickle.load(pickle_in)
                print(face_rec_id_pass)
                psaw = face_rec_id_pass[m]
                print(m)
                print(psaw)
                print(face_rec_id_pass)
                pickle_in.close()

                username = m
                psw = psaw
                print(psw)
                user = authenticate(username=username, password=psw)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'Successfully login')
                    return redirect('home')
                else:
                    return redirect('home')

        messages.error(request, 'm none ha')
        return redirect('home')

    else:
        messages.error(request, 'lol')
        return redirect('home')


def face_Detection(test_img):
    gray_img =cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
    face_haar_cascade =cv2.CascadeClassifier('/Users/DELL/Desktop/university_portal/cascades/data/haarcascade_frontalface_default.xml')
    face = face_haar_cascade.detectMultiScale(gray_img,scaleFactor=1.5,minNeighbors=5)
    return face, gray_img


def entry(name):
    cap = cv2.VideoCapture(0)
    count = 0
    i = 0
    no = 0
    f = 0

    # os.chdir('/Users/DELL/Desktop/university_portal/train')
    # os.mkdir(name)
    os.chdir('/Users/DELL/Desktop/university_portal')

    while True:
        ret, test_img = cap.read()
        if not ret:
            continue
        face_detected, gray_img = face_Detection(test_img)
        gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
        face_haar_cascade = cv2.CascadeClassifier(
            '/Users/DELL/Desktop/university_portal/cascades/data/haarcascade_frontalface_default.xml')
        face = face_haar_cascade.detectMultiScale(gray_img, scaleFactor=1.5, minNeighbors=5)


        for face in face_detected:
            (x, y, w, h) = face

            if face.all() != 0:
                f = 1
                no = no + 1
                print(no)
            else:
                f = 0

        resized_img = cv2.resize(test_img, (1000, 700))
        cv2.imshow('testing', resized_img)
        if cv2.waitKey(10) == ord('q'):
            break
        if f == 1:
            cv2.imwrite("train/"+ "/%s.jpg" % name, test_img)
            count += 1
            f = 0
        if no == 1:
            break

    cap.release()
    cv2.destroyAllWindows()
    os.chdir('/Users/DELL/Desktop/university_portal')


def check():
    cam = cv2.VideoCapture(0)
    reccognizer = cv2.face.LBPHFaceRecognizer_create()
    face_haar_cascade = cv2.CascadeClassifier(
        '/Users/DELL/Desktop/university_portal/cascades/data/haarcascade_frontalface_default.xml')
    reccognizer.read('/Users/DELL/Desktop/university_portal/trainner.yml')

    final = []
    lable = {}
    no = 0
    with open("/Users/DELL/Desktop/university_portal/labes.pickle", "rb") as f:
        lables = pickle.load(f)
        print(lables)
        lable = {v: k for k, v in lables.items()}

    while True:
        ret, img = cam.read()
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_haar_cascade.detectMultiScale(gray_img, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            roi_gray = gray_img[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            id_, conf = reccognizer.predict(roi_gray)
            if conf >= 50:  # and conf <=85:
                final.append(id_)
                print(id_)
        if cv2.waitKey(2) == ord('q'):
            break
        for face in faces:
            (x, y, w, h) = face

            if face.all() != 0:
                no = no + 1
                print(1)

        if no == 20:
            break

    cam.release()
    cv2.destroyAllWindows()
    print(final)
    m = max(final)
    # try:
    #     m = max(final)
    #     print(final)
    # except:
    #     print("Something went wrong")
    #     return (None)

    # return (lable[m])
    if m is not None:
        l = final.count(m)
        if l >= 18:
            print(m)
            print(lable)
            return (lable[m])
        else:
            return (None)
    else:
        return (None)



class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('Result.html')
        all = Marks.objects.all()
        first_name = ""
        last_name = ""
        rollno = 0
        Subject_c = 0
        Subject_Networking = 0
        Subject_java = 0
        Subject_python = 0
        email = ""
        birthday = 0

        for student in all:

            if (str(student.username) == str(request.user) ):
                username = student.username
                first_name = student.first_name
                last_name = student.last_name
                rollno = student.rollno
                Subject_c = student.Subject_c
                Subject_Networking =student.Subject_Networking
                Subject_java =student.Subject_java
                Subject_python =student.Subject_python
                email =student.email
                birthday =student.birthday
            Qualified =  "Pass"

        data = {'username': username, 'first_name': first_name, 'last_name': last_name , 'rollno' : rollno, 'Subject_c': Subject_c , 'Subject_Networking': Subject_Networking ,
                'Subject_java' : Subject_java, 'Subject_python': Subject_python, 'email' : email ,'birthday' :birthday ,"Qualified" : Qualified}


        
        # data = {

        #      'username': '39.99',
        #     'first_name': 'Cooper Mann',
        #     'last_name': "1233434",
        # }
        pdf = template.render( {'a': data} )
        pdf = render_to_pdf('Result.html', {'a': data} )
        if pdf:
            response = HttpResponse(pdf,content_type='application/pdf')
            filename  = "invoice_%s.pdf" %("1234")
            content = "inline; filename ='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename= '%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
        
        # return HttpResponse(pdf,content_type='application/pdf')
        # return render(request , 'invoice.html', {'a': data} )





def face_recogn():
    path = '/Users/DELL/Desktop/university_portal/train'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    count=[]
    i=0
    no=0
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList


    encodeListKnown = findEncodings(images)
    cap = cv2.VideoCapture(0)
     
    while True:
        success, img = cap.read()
        #img = captureScreen()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
     
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
     
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            #print(faceDis)
            matchIndex = np.argmin(faceDis)
     
            if matches[matchIndex]:
                name = classNames[matchIndex].lower()
                # print(name)
                count.append(name)
                i=i+1
        if i == 10:
            break
        no = no +1
        if no == 50:
            break
    # print(count)
    try:
        m = max(count)
        return(m)
    except:
        return None


