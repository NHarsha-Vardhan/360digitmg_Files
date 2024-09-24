# String Manipulation

##### String Manipulation
##### 1.	Create a string “Grow Gratitude”.

# a)	How do you access the letter “G” of “Growth”?
Name = "Grow Gratitude"
print(Name[0])

# b)	How do you find the length of the string?
print(len(Name))

# c)	Count how many times “G” is in the string.
count = Name.count('G')
count

##### 2.	Create a string “Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else.”

# a)	Count the number of characters in the string.

string = "Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else."
string

def count_chars(txt):
	result = 0
	for char in txt:
		result += 1     # same as result = result + 1
	return result
count_chars(string)

#or
print(len(string))

##### 3.	Create a string "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"

idea = "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"
idea
# a)	get one char of the word
print(idea[0])
# b)	get the first three char
print(idea[0:3])
# c)	get the last three char
print(idea[-3:])

##### 4.	create a string "stay positive and optimistic". 

create = "stay positive and optimistic"
print(create)
# Now write a code to split on whitespace.
print(create.split(' ', 3 ))
# Write a code to find if:
# a)	The string starts with “H”
create.startswith("H")
# b)	The string ends with “d”
create.endswith("d")
# c)	The string ends with “c”
create.endswith("c")

##### 5.	Write a code to print " 🪐 " one hundred and eight times. (only in python)"

code = " 🪐 " * 108
code

##### 7.	Create a string “Grow Gratitude” and write a code to replace “Grow” with “Growth of”"

c = "Grow Gratitude"
c.replace("Grow","Growth of")

##### 8.	A story was printed in a pdf, which isn’t making any sense. i.e.:"“.elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A”
###### You have noticed that the story is printed in a reversed order. Rectify the same and write a code to print the same story in a correct order.

story = ".elgnuj eht otni ffo deps meht fo htoB .eerf noil eht tes ot sepor eht no dewang dna nar eh ,ylkciuQ .elbuort ni noil eht deciton dna tsap deklaw esuom eht ,nooS .repmihw ot detrats dna tuo teg ot gnilggurts saw noil ehT .eert a tsniaga pu mih deit yehT .meht htiw noil eht koot dna tserof eht ot ni emac sretnuh wef a ,yad enO .og mih tel dna ecnedifnoc s’esuom eht ta dehgual noil ehT ”.em evas uoy fi yademos uoy ot pleh taerg fo eb lliw I ,uoy esimorp I“ .eerf mih tes ot noil eht detseuqer yletarepsed esuom eht nehw esuom eht tae ot tuoba saw eH .yrgna etiuq pu ekow eh dna ,peels s’noil eht debrutsid sihT .nuf rof tsuj ydob sih nwod dna pu gninnur detrats esuom a nehw elgnuj eht ni gnipeels ecno saw noil A"
print(story)

print('\n',story[::-1])

