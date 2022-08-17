class Clothing:
    def __init__(self, num_clothes):
        self.num_clothes = num_clothes
        self.item = []
        self.mintemp = []
        self.maxtemp = []
        self.current_temp = 0
        self.temp_formallity = ""
        self.formallity = []
        self.itemls = []
        for i in range(self.num_clothes):
            self.item.append(input("Please enter the clothing item: "))
            self.mintemp.append(int(input("Please enter the the minimum temp you would wear the item in: ")))
            self.maxtemp.append(int(input("Please enter the maximum temp you would wear the item in: ")))
            self.formallity.append(input("Would you wear this to a formal event: "))
        self.current_temp = int(input("Please enter the current temperature: "))
        self.temp_formallity = input("Is the item formal: ")
        self.temp = "You can wear these items: "
        for k in range(self.num_clothes):
            i = 0
            if self.mintemp[k] <= self.current_temp <= self.maxtemp[k] and self.temp_formallity == self.formallity[k]:
                self.temp += self.item[k]
                self.temp += " "

        print(self.temp)



if __name__ == "__main__":
    num = int(input("Please enter the number of clothes you would like to catalog:"))
    c1 = Clothing(num)
