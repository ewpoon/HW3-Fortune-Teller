# import the random module
import random

# create the class Fortune_Teller
class Fortune_Teller:
    
    def __init__(self, fortune_list):
        self.fortune_list = fortune_list
        self.history_list = []

    # create the constructor (__init__) method
    # it takes as input: 
    #   a list of possible fortunes and 
    # it sets this object's fortune_list (instance variable) to the passed list 
    # it sets this object's history_list to the empty list (instance variable)

    def tell(self):
        #does this include the last number at the end of fortune_list?
        num = random.randrange(0, len(self.fortune_list))
        self.history_list.append(num)
        return self.fortune_list[num]
    # create the tell method
    # it randomly picks an index from 0 to the number of items in the 
    #       fortune_list minus one
    # it adds that index to the end of the history_list 
    # it returns the fortune at that index in this object's fortune_list

    def __str__(self):
        if len(self.history_list) == 0:
            return "Last fortune: none yet"
        return "Last fortune: " + self.fortune_list[self.history_list[-1]]
    # create the __str__ method
    # if the length of history_list is 0 it returns "Last fortune: not given yet"
    # else it returns the fortune at the last index in the history_list as 
    # "Last fortune: fortune"
    
    def print_history(self):
        for i in self.history_list:
            print("[" + str(i) + "] " + self.fortune_list[i])
    # create the print_history method
    # prints "[index] fortune" for each of the indicies in the history_list 
    # from the first to the last with each on a single line

    def print_count_for_num(self, num):
        count = 0
        for number in self.history_list:
            if number == num:
                count += 1
        print("{} occurred {} times".format(num,count))
    # create the print_count_for_num method
    # it prints how many times the passed index is found in the history_list  
    
    def five_hundred(self):
        index_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}
        self.history_list = []
        max = 0
        ind = None
        for i in range(500):
            self.tell()
        for i in self.history_list:
            index_dict[i] += 1
        for k in index_dict:
            print("{}: {}".format(k, index_dict[k]))
        for k in index_dict:
            if index_dict[k] > max:
                max = index_dict[k]
                ind = k
        print("The most frequent index after 500 was: {}".format(ind))
        #????
    # EXTRA POINTS
    # create the five_hundred method
    # it tells a fortune 500 times, prints the counts for each index, and 
    # prints the most frequently occurring index

# main funtion for testing
def main():
    # you can change these possible fortunes
    fortune_list = ["Win the lottery", \
                    "Slip and fall", \
                    "Snow day on Wednesday",  \
                    "Frostbite on Wednesday",  \
                    "Snow day on Thursday", \
                    "Get an A in SI 206"]    
    
    #Create a fortune-teller and test it
    print("Testing the first fortune-teller:")
    teller = Fortune_Teller(fortune_list)
    print("Fortune : " + teller.tell())
    print("Testing the print of the last fortune")
    print(teller)
    print("Fortune : " + teller.tell())
    print("Testing the print of the last fortune")
    print(teller)
    print("Printing the full history:")
    teller.print_history()
    print("Printing the number of times index 1 occured")
    teller.print_count_for_num(1)
    print()

    #Create another fortune-teller
    print("Testing the second fortune-teller:")
    teller2 = Fortune_Teller(fortune_list)
    print("Testing when no fortunes have been told yet")
    print(teller2)
    print("Fortune : " + teller2.tell())
    print(teller2)
    for x in range(5):
        print("Fortune : " + teller2.tell())
    print("Printing the full history:")
    teller2.print_history()
    print("Printing the number of times index 2 occured")
    teller2.print_count_for_num(2)
    teller2.five_hundred()
    #EXTRA POINTS
    #Try telling 500 fortunes

# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
