# coding = utf-8
#字典
Jay_songs = {
    '3eChar':'龙卷风', 
    '2Char': '搁浅',
    'twoChar': '晴天',
    'threeChar': '七里香',
    'fourChar': '千里之外',
    'fiveChar': '夜的第七章',
    }

favorate_Jay_songs = {
	'twoChar': '晴天',
    'threeChar': '七里香',
    'fourChar': '千里之外',
    'fiveChar': '夜的第七章',
    }

print ("My 1st favorate song is\n" + 
    favorate_Jay_songs['fiveChar'] + 
    ".\n")

for v in Jay_songs.values():
    if v in favorate_Jay_songs.values():
        print ("My favorate song is " + v + ".")
    else:
        print (v + " is not my favorate song.")

