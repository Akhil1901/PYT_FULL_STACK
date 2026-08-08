"welcome to the cinema booking"
print("**********LOGIN FORM**********")
#user id and passwords and admin id passwords
Admin=['owner','cashier',]
admin_password=['owner@123','cashier@123']
user=['user1','user2','user3','user5','user4']
user_password=['@123','@143','145','@146']
#theatre movie details
Movies=['Og2','kalki2','varanasi','dragon']
show_times=['9:30 am to 11:30 am','2:30 pm to 5:00 pm','6:30 pm to 9:00 pm','9:30 pm to 12:30 am']
seats=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10'
       'B1','B2','B3','B4','B5','B6','B7','B8','B9','B10',
        'C1','C2','C3','C4','C5','C6','C7','C8','C9','C10']
bookings=[]
cart_data=[]
#choosing role 
while(True): 
    role=input("enter your role USER OR ADMIN or new user:")
    if(role=="user"):
        count=5
        #user Login 
        while(count>3):
            name=input("enter your name or user id:")
            #checking user existed or not
            if(name not in user):
                print("user not registered")
            else:
                count=3
                #checking the user password
                while(count>0):
                    password=input("enter your password:")
                    count=count-1
                    if(password not in user_password and count!=0):
                       print("you have",count,"attempts")
                    elif(count==0):
                        print("your attempts overed try  after 15s  again")
                        exit()
                    else:
                        print("password sucessfully")
                        count=0
                        print("*******Welcome Dear customer **********")
                        print("*****************choose your interested movie***********************")
                        #displaying the movies 
                        for select_movies in Movies:
                            print(select_movies)
                        select_movie=input("enter your interested movie ")
                        #displaying the show times
                        print("Displaying the show times")
                        for show_times in show_times:
                            print(show_times)
                        #selecting the show time 
                        show_time=input("enter your show time: ")
                        print("displaying the seat layout")
                        for i in seats:
                            print(i, end=" ")
                        print()
                        seat_selection_list=[]
                        #select yo
    elif(role=='admin'):
        count=5
        while(count>3):
            admin_id=input("enter your admin id: ")
            if(admin_id not in Admin):
                print("you are not admin")
            else:
                count=3
                while(count>0):
                    password=input("enter your password:")
                    count=count-1
                    if(password not in admin_password and count!=0):
                        print("you have",count,"attempts")
                    elif(count==0):
                        print("your attempts overed try  after 15s  again")
                        exit()
                    else:
                        count=0
                        while(True):
                            print("login sucessfully")
                            print("*******Welcome Admin **********")
                            print("**********Displaying admin menu section**********")
                            print("add movies")
                            print("add shows")
                            print("manage seats")
                            print("delete shows or movies")
                            print("view bookings")
                            print("exit")
                            admin_choice=input("enter your option: ")
                            if(admin_choice=='addmovies'):
                                movie_name=input("enter movie name to be added: ")
                                Movies.append(movie_name)
                                print("**************Displaying the all movies**********")
                                for i in Movies:
                                    print(i)
                            elif(admin_choice=='addshows'):
                                show_time = input("enter show time")
                                if(len(show_time)==4):
                                    print("shows are full")
                                else:
                                    show_time.append(show_time)
                                    #updated the show_times
                                    for i in show_times:
                                        print(i)
                            elif(admin_choice=='manageseats'):
                                print("manage seats")
                            elif(admin_choice=='delete shows or movies'):
                                print("delete shows or movies")
                            elif(admin_choice=='view bookings'):
                                print("view bookings")
                            elif(admin_choice=='exit'):
                                print("exit")
                                break
    else:
        name=input("create your user id : ")
        password=input("create your password: ")
        user.append(name)
        user_password.append(password)
        print("registration sucessfully")