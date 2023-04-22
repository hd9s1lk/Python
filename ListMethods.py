camping_stuff = "tent, sleeping bags, water, raspberry py, coffee, knife, ethernet cable, flash drive, beard oil, marshmallows"

camping_list = ["tent", "sleeping bags", "water", "raspberry py", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]

camp_site = ["Crystal Lake", 404, 26, True]

#camping_list.append("toilet paper")
#camping_list.append("bidet")

camping_list.extend(["toilet paper", "bidet"])

#camping_list = camping_list + ["toilet paper" , "bidet"]

camping_list.insert(0, "chocolate")
print(camping_list[-2])

#camping_list.clear()
camping_list.pop(1)
camping_list.pop(1)

print(camping_list)
