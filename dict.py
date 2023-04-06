val=input("ENTE 1234")
coust = {
    "1" : "sami",
    "2" : "hamza ",
    "3" : " sharf ",
    "4" : "aldeen"

}
out = ""
for ch in val :
   out += coust.get(ch,"valu not found ") + " "
print(out)