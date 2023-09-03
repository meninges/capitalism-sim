#capitalism sim

class shop:
    def __init__(self, input_name, input_type, input_price, input_salary, input_stock, input_phrase):
        self.name = input_name
        self.type = input_type
        self.price = input_price
        self.salary = input_salary
        self.initstock = input_stock
        self.stock = input_stock
        self.entrancephrase = input_phrase
        self.in_stock = True

#listing over each attribute of the store in an advertisement
    def __repr__(self):
        return "{name} is the best {kind} store in town! They have {stock} item(s) left in stock at the low low price of {price} rEEEbucks each. Buy now before they run out!" .format(name = self.name, kind = self.type, price = self.price, stock = self.stock)

#when stock is depleted (0) a shop is sold out
    def sold_out(self):
        self.in_stock = False

#when you work at a shop, you will restock the shelves
    def restock(self):
        self.in_stock = True
        self.stock == self.initstock

#store paying worker function- to use store attributes later in work function
    def pay_worker(self, time):
        j = float(self.salary * time)
        return(j)


class capitalist:
    def __init__(self, input_name, input_age):
        self.name = input_name
        self.age = input_age
        self.worktimes = 0
        self.happiness = 50
        self.money = 1000.
        self.time = 0
        self.day = 0
        self.inventory = []

#capitalist's stats + explanation
    def __repr__(self):
        return ("""This is you. 
{name}, a {age} year old productive member of a thriving capitalist society. Oink oink you capitalist pig.
You have {money} rEEEbucks. 
You have worked {times} times. 
You have used {time} hours.
Your happiness score is {happy}""" .format(name = self.name, age = self.age, money = self.money, times = self.worktimes, time = self.time, happy = self.happiness))

    #checking in prints stats + an additional phrase related to happiness level
    def checkin(self):
        print (repr(self))
        if self.happiness > 15:
            print ("What a lovely day to be alive!")
            return
        print ("...You're beginning to doubt capitalist society")
        if self.happiness > 5:
            return
        print ("Could you have made a mistake?")
        if self.happiness > 3:
            return
        print ("No... you're sure you haven't.")
        if self.happiness > 2:
            return
        print ("""Come to think of it, you actually aren't.
This seems more and more like a mistake with every passing day""")
        if self.happiness > 1:
            return
        print("It has to be a mistake.")

#function for capitalist to work, adding money and taking away happiness
    def work(self, store):
        t = 2
        if self.happiness >= ((store.salary*2)/3 + 10) and self.time + t <= 10:
            self.time += t
            self.money += store.pay_worker(t)
            shop.restock(store)
            self.happiness -= ((store.salary*2)/3 + 10)
            self.worktimes += 1
            print ("The shop has been restocked, Good work, see you Monday!")
            return()
        if self.time + t > 10:
            print ("Sorry, you don't have enough time today!")
            return()
        else:
            print ("Sorry, you don't have enough happiness points to do this!")
            return()

        #function for capitalist to buy things, taking away money, and adding item to inventory
    def buy(self, shop, number):
        self.money -= shop.price * number
        if shop.stock - number >= 0:
            shop.stock -= number
            self.happiness += shop.price * number
            while number > 0:
                self.inventory.append(shop.type)
                number -= 1
        else:
            print ("Sorry, you can't buy that many!")

#to list all the stores
magzalar = []

#creating objects, first capitalist player then stores
capitalist_no1 = capitalist("Brian", 21)
store_no1 = shop("Mom and Pop's Veg Shop", "produce", 5, 5, 30, """Hello dearie, how can we help you? (buy/work/leave)
""")
store_no2 = shop("Flaherty's Butchery", "meat", 15, 10, 20, """Whaddaya want today, big man? (buy/work/leave)
""")
store_no3 = shop("Linery", "clothing", 25, 15, 10, """You certainly look like you could use our help! What would you like to do today? (buy/work/leave)
""")
store_no4 = shop("Fragranté", "perfume", 50, 20, 5, """(...Oh god, I think I /smell/ a peasant.) 
Hi, how may I help you today? (buy/work/leave)
""")
store_no5 = shop("Upsilon Diamonds", "jewelry", 1000, 30, 1, """Are you sure you're rich enough to be in my presence? (buy/work/leave)
""")

#appending all shop class objects to the list
magzalar.append(store_no1)
magzalar.append(store_no2)
magzalar.append(store_no3)
magzalar.append(store_no4)
magzalar.append(store_no5)

#area:home
def Home(go_plaza):
    #ya gotta have time in the day to get up
    while capitalist_no1.time < 10 and capitalist_no1.happiness > 0:
        print("""You wake up to another productive day in your Home. What would you like to do? (Out/Stay)""")
        while True:
            x = input().lower()
            #annoying siri error message
            if x != "out" and x != "stay" and x!= "checkin":
                print("""Sorry, I didn't quite get that, could you say that again? (Out/Stay)""")
                continue
            #you stay at home? boring bitch that wastes t i m e
            if x == "stay":
                capitalist_no1.time += 1
                print ("""You decide to stay at home. What would you like to do? (Out/Stay)""")
            if capitalist_no1.time > 10.0:
                continue
            #checking your stats as soon as you wake up? sweat.
            if x == "checkin":
                capitalist.checkin(capitalist_no1)
                print ("""You wake up to another productive day in your Home. What would you like to do? (Out/Stay)""")
                continue
          #say inventory to see inventory, pretty simple
            if x == "inventory": 
                print (capitalist_no1.inventory)
                continue
          #go to plaza? calling plaza function which uses the functions Home and shop_inside
            else:
                go_plaza(Home, shop_inside)
                break
    return()

def shop_inside(shop, go_plaza):
    while capitalist_no1.time < 10 and capitalist_no1.happiness > 0:
        #each store's phrase when you enter- they're input when defining the objects
        var = input(shop.entrancephrase).lower()
        #buying things using buy function of capitalist class
        if var == "buy":
          #input asking for number
            g = int(input("""How many would you like to purchase?
        """))
          #need number to be integer debugging
            while isinstance(g, int) == True:
                capitalist.buy(capitalist_no1, shop, g)
                print ("Thank you for choosing {store}!".format(store = shop.name))
                go_plaza(Home, shop_inside)
                break
        #working for that shop using work function of capitalist class
        if var == "work":
            capitalist.work(capitalist_no1, shop)
            go_plaza(Home, shop_inside)
            break
        #takes you back to Plaza area by restarting Plaza function
        if var == "leave":
            go_plaza(Home, shop_inside)
            break
        #you can check in anywhere, ok?
        if var == "checkin":
            capitalist.checkin(capitalist_no1)
            continue
        #type inventory to see your inventory anywhere
        if var == "inventory":
            print (capitalist_no1.inventory)
            continue
        #annoying siri error message part 2 electric boogaloo
        else:
            print("Sorry, I didn't quite get that, could you say that again?")
    return()

def Plaza(go_home, go_shop):
    while capitalist_no1.time < 10 and capitalist_no1.happiness > 0:
        #asks where you'd like to go, with list of store advertisements
        a = input("""You are now in the Plaza, choose to go home or which type of store to go to:
        (type 'help' for list)
        """).lower()
        #checks if input is equal to ANY of the store types
        if any(obj.type == a for obj in magzalar):
            for obj in magzalar:
                z = getattr(obj, "type")
                #checks to find out WHICH TYPE matches which store exactly
                if z == a:
                #runs function that takes you to store
                    go_shop(obj, Plaza)
            continue
        #prints all store advertisements using repr
        if a == "help":
            for obj in magzalar:
                print ("""
        """ + repr(obj))
            print("")
            continue
        #runs Home function to bring you back to the Home area
        if a == "home":
            go_home(Plaza)
            break
        #yes, ok, you CAN check in ANYWHERE
        if a == "checkin":
            capitalist.checkin(capitalist_no1)
            continue
        #you can see your inventory by typing inventory ANYWHERE
        if a == "inventory":
            print (capitalist_no1.inventory)
            continue
        #annoying siri error message 3 the return of the tapestry
        else:
            print("Sorry, I didn't quite get that, could you say that again?")
    return()

#game events start here, small tutorial section
print ("""Welcome to Capitalism Sim!""")
if input("""You can type skip in chat to skip the tutorial:
""").lower() != "skip":
    print ("Tutorial stuff")

#pick your difficulty (changes number of days to end)
h = input("""Modes: Easy, Intermediate, Difficult, GodMode, Sandbox
""").lower()
if h == "easy":
    t = 20
if h == "intermediate":
    t = 10
if h == "difficult":
    t = 5
if h == "godmode":
    t = 1
if h == "sandbox":
    t = 1000000000

#You start at home
c = capitalist_no1.day
while c <= t:
    #if not happy will end game
    if capitalist_no1.happiness > 0:
        #gives you happiness at start of every day based on what you own
        for item in capitalist_no1.inventory:
            for obj in magzalar:
                z = getattr(obj, "type")
                if z == item:
                    capitalist_no1.happiness += (obj.price/10)
        #just makes sure it can't go over 100
        if capitalist_no1.happiness > 100:
            capitalist_no1.happiness = 100
        capitalist_no1.time = 0
        #code for each day start
        print ("Day {number}/{total}".format(number = c, total = t))
        capitalist.checkin(capitalist_no1)
        Home(Plaza)
        c += 1
    else:
    #the true ending
        print ("""Your happiness score has dropped to zero.
    You have become depressed.
    Even getting out of bed is difficult most days, not to mention working.
    As an unproductive member of society now, instead of recieving the help you require, you lose your job.

    TRUE ENDING: CAPITALISM WINS""")
        break

#good ending
if capitalist_no1.worktimes > (4 + t/2) and capitalist_no1.money > (1200 + t*100):
    print ("""Congratulations!
You successfully participated in capitalist society without becoming depressed, that's actually pretty hard.""")

#neutral ending
else:
    print ("""You're really useless, you know that?
You do not earn enough money to succeed in capitalist society.
You have become homeless.

NEUTRAL ENDING""")



