"welcome to the cinema booking"
print("**********LOGIN FORM**********")
#user id and passwords and admin id passwords
Admin=['owner','cashier',]
admin_password=['owner@123','cashier@123']
user=['user1','user2','user3','user5','user4']
user_password=['@123','@143','145','@146']
#theatre movie details
movies=['Og2','kalki2','varanasi','dragon']
shows=[]
seats=[]
bookings=[]
cart_data=[]
booked_seats=[]
#choosing role 
while(True): 
    print("1.user")
    print("2.Admin")
    print("3.new user")
    role=input("enter your role 1 or 2 or 3:")
    if(role=="1"):
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
                        count=0
                        print("login sucessfully")
                        while(True):
                            print("displaying the User menu section")
                            print("1.view movies")
                            print("2.view shows")
                            print("3.select seats")
                            print("4.book ticket")
                            print("5.view booking")
                            print("6.exit")
                            user_ch=int(input("enter your choice (1/2/3/4/5/6): "))
                            if(user_ch==1):
                                for i in movies:
                                    
                                    print(i)
                            elif(user_ch==2):
                                print("view shows")
                            elif(user_ch==3):
                                print("select seats")
                            elif(user_ch==4):
                                print("book ticket")
                            elif(user_ch==5):
                                print("view booking")
                            elif(user_ch==6):
                                print("exiting")
                                break
                            else:
                                print("invalid")
                                
    elif(role=='2'):
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
                            print("1.add movies")
                            print("2.add shows")
                            print("3.manage seats")
                            print("4.delete shows or movies")
                            print("5.view bookings")
                            print("6.exit")
                            admin_choice=input("enter your option(1/2/3/4/5/6): ")
                            if(admin_choice=='1'):
                                add_movies=input("enter the movie name to be added: ")
                                if(add_movies in movies):
                                    print("movie already exist")
                                else:
                                    print("available movies")
                                    movies.append(add_movies)
                                    shows.append([])
                                    seats.append([])
                                    for movie in movies:
                                        idx = movies.index(movie)
                                        print(idx,".",movie)
                                    print(add_movies,"Movie added Sucessfully.")
                            elif(admin_choice=='2'):
                                #displaying the available movies
                                for movie in movies:
                                    idx = movies.index(movie)
                                    print(idx,".",movie)
                                movie_name=int(input("enter the movie name to add shows:"))
                                if(movie_name>=0 and movie_name<len(movies)):
                                    add_shows=input("enter the show timings to be added: ")
                                    shows[movie_name].append(add_shows)
                                    for i in shows[movie_name]:
                                        print(i)
                                else:
                                    print("Invalid movie choice")
                            elif(admin_choice=='3'):
                                print("manage seats")
                            elif(admin_choice=='4'):
                                print("delete shows or movies")
                            elif(admin_choice=='5'):
                                print("view bookings")
                            elif(admin_choice=='6'):
                                print("exit")
                                break
                            else:
                                print("invalid")
    elif(role=="3"):
        name=input("create your user id : ")
        password=input("create your password: ")
        user.append(name)
        user_password.append(password)
        print("registration sucessfully")
    else:
        print("invalid")