# Lam Dang 

# this programs gives the estimated one rep max of the athlete inserted
# https://articles.reactivetrainingsystems.com/wp-content/uploads/2015/11/E1RM-TABLE-1024x322.png
# logic based off of reactive training systems rate of exertion chart
class Athlete:
    def __init__ (self,name,max_squat,max_bench,max_deadlift):

        self.name =  name 
        self.max_squat = max_squat
        self.max_bench = max_bench
        self.max_deadlift = max_deadlift
        
    
    def get_lift(self):
        print(self.max_squat)
        print(self.max_bench)
        print(self.max_deadlift)

    def estimated_lift(self):
        mydict  = {}
        mydict['squat'] = self.max_squat
        mydict['bench'] = self.max_bench
        mydict['deadlift'] = self.max_deadlift

        print("squat\nbench\ndeadlift \n")
        lift = input("Enter the lift you want to compute: ")
        rpe = int(input("Enter the rpe you are aiming for: "))
        reps = int(input("Enter the amount of reps you want to hit: "))
        if lift in mydict:

            if reps != 0 or rpe != 0:
                hashmap =  {} # gets the starting position of each rep
                count = 1
                percentage = 1
                

                while count <= 10:
                    if count == 1:
                        hashmap[count] = percentage 
                        count += 1
                        percentage -= .045
                    elif count == 2:
                        hashmap[count] = percentage 
                        count += 1
                        percentage -= .03

                    else:
                        hashmap[count] = percentage
                        count += 1
                        percentage -= .03
                        
                # print(hashmap)
                # {1: 1, 2: 0.955, 3: 0.9249999999999999, 4: 0.8949999999999999, 5: 0.8649999999999999,
                #  6: 0.8349999999999999, 7: 0.8049999999999998, 8: 0.7749999999999998, 9: 0.7449999999999998, 10: 0.7149999999999997}
                
                if reps in hashmap:
                    # checks the two case scenario in which a user choosees to go for 100% or if they decided to go for a single at rpe 9
                    if rpe == 10:
                        print(hashmap[reps]*mydict[lift])
                    elif reps ==1 and rpe == 9:
                        print(hashmap[2]*mydict[lift])
                    elif reps == 1:
                        diff = ((10 - rpe -1) *.03) + .045
                        print((hashmap[reps] - diff) * mydict[lift])

                    else:
                        diff = (10 - rpe) * .03
                        print((hashmap[reps] - diff) * mydict[lift])

    # Allows the user to update the obj lifts 
    def update_squat(self,x):
        self.max_squat = x
        print(self.max_squat)
    def update_bench(self,x):
        self.max_bench = x 
    def update_deadlift(self,x):
        self.max_deadlift = x






        
if __name__ == "__main__":

    a1 = Athlete("Quang",275,245,405)
    a1.get_lift() # gets the return of the lifts 

    # a1.estimated_lift()

    a1.update_squat(285) 
    a1.get_lift()









    








