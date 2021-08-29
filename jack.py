print("LIST:")
print("About the jones family and what they like")
ava_info = "things about ava:\nCats\nFood\nBabies\nChilling/Playing on my tablet\nCoding\nPlayful."
jack_info = "things about jack:\nDinosaurs\nFreddy\nFood\nPlayful\nSomtimes annoying."
dad_info = "things about dad:\nHistory\nLearning with children\nIs a stay at home dad\nChilling\nReading."
mom_info = "things about mom:\nFlowers\nLoves kids\nDolphins\nnote i don't really know what mom likes."
print(ava_info)
print("")
print(jack_info)
print("")
print(dad_info)
print("")
print(mom_info)
print("")
#ava_info
#jack_info
#dad_info
#mom_info
i = input("do you like this code :)")
if i.lower().strip() == "yes":
    print("thank you :)")
elif i.lower().strip() == "no":
    print("oh ok :(")
else:
    print("please enter either [YES] [NO]")