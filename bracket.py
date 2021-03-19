import csv
import random

def compare(all_teams, keys):
	team1 = ""
	while team1 != 'quit':
		team1 = input('Input your first team, "quit" to quit, or "help" for help: ')
		if team1 == 'help':
			compare_help()
			team1 = input('Input your first team, "quit" to quit, or "help" for help: ')
		if team1 == "quit":
			return
		team2 = input('Input your second team: ')
		try:
			team1_dict = all_teams[team1]
			team2_dict = all_teams[team2]
			str1 = team1_dict['Seed']
			str1 += '. '
			str1 += team1 
			str1 += ' |'
			str2 = team2_dict['Seed'] 
			str2 += ' . '
			str2 += team2
			str1 = str1.rjust(50)
			str2 = str2.ljust(50)
			print(str1, str2)
			for i in range(0, len(keys)):
				key = keys[i]
				t1 = key
				t1 += ' --- '
				t1 += team1_dict[key]
				t1 += ' |'
				t2 = team2_dict[key]
				t2 += ' --- '
				t2 += key
				t1 = t1.rjust(50)
				t2 = t2.ljust(50)
				print(t1, t2)

			t1_o = float(team1_dict["Adj-O"])
			t1_d = float(team1_dict["Adj-D"])
			t1_t = float(team1_dict["Adj-T"])

			t2_o = float(team2_dict["Adj-O"])
			t2_d = float(team2_dict["Adj-D"])
			t2_t = float(team2_dict["Adj-T"])

			league_av_t = 68.18
			league_av_pp100 = 105.35
			possessions = (t1_t * t2_t) / league_av_t
			
			t1_ppp = (((t1_o + t2_d)/league_av_pp100) - 1) * possessions
			t2_ppp = (((t2_o + t1_d)/league_av_pp100) - 1) * possessions

			prob_t1 = (t1_ppp ** 10.25) / (t1_ppp**10.25 + t2_ppp**10.25) * 100
			prob_t2 = (t2_ppp ** 10.25) / (t1_ppp**10.25 + t2_ppp**10.25) * 100

			print_sepeartor(50)

			prob = "Percent Chance to win"
			p1 = prob
			p1 += ' --- '
			p1 += str(round(prob_t1,3)) + ' %'
			p1 += ' |'
			p2 = str(round(prob_t2, 3)) + ' %'
			p2 += ' --- '
			p2 += prob
			p1 = p1.rjust(50)
			p2 = p2.ljust(50)
			print(p1, p2)

			print_sepeartor(50)

			t1 = " Expected Score  --- "
			t1 += team1
			t1 += " - "
			t2 = str(int(round(t1_ppp))) + ' '
			t2 += team2
			t2 += ' - '
			t2 += str(int(round(t2_ppp)))
			t1 = t1.rjust(50)
			t2 = t2.ljust(50)
			print(t1 + t2)


		except:
			print('\n'+"Invalid team name(s), please try again")
	return

def compare_help():
	input_in = input('Input "teams" for all team spellings, or "credits" for credits: ')
	if input_in == 'teams':
		letter = input("Input the first leter of the team: ")
		for key in all_teams:
			if key[0] == letter:
				print(key)

def print_sepeartor(num):
	p1 = "-----"
	p2 = p1
	p1 = p1.rjust(num)
	p2 = p2.ljust(num)
	print(p1+p2)


def simulate(all_teams, keys):
	team1 = ""
	while team1 != 'quit':
		team1 = input('Input your first team, "quit" to quit, or "help" for help: ')
		if team1 == 'help':
			compare_help()
			team1 = input('Input your first team, "quit" to quit, or "help" for help: ')
		if team1 == "quit":
			return
		team2 = input('Input your second team: ')
		try:
			team1_dict = all_teams[team1]
			team2_dict = all_teams[team2]
				
			t1_o = float(team1_dict["Adj-O"])
			t1_d = float(team1_dict["Adj-D"])
			t1_t = float(team1_dict["Adj-T"])

			t2_o = float(team2_dict["Adj-O"])
			t2_d = float(team2_dict["Adj-D"])
			t2_t = float(team2_dict["Adj-T"])

			league_av_t = 68.18
			league_av_pp100 = 105.35
			possessions = (t1_t * t2_t) / league_av_t

			#t1_ppp = (((t1_o * t2_d)/league_av_pp100) * possessions) / 100.0 
			#t2_ppp = (((t2_o * t1_d)/league_av_pp100) * possessions) / 100.0
			t1_ppp = (((t1_o + t2_d)/league_av_pp100) - 1) * possessions
			t2_ppp = (((t2_o + t1_d)/league_av_pp100) - 1) * possessions
			prob_t1 = (t1_ppp ** 10.25) / (t1_ppp**10.25 + t2_ppp**10.25) * 100
			prob_t2 = (t2_ppp ** 10.25) / (t1_ppp**10.25 + t2_ppp**10.25) * 100

			num = random.uniform(0.000, 100.000)
			print_sepeartor(25)
			x1 = team1_dict['Seed']
			x1 += '. '
			x1 += team1
			x1 += " v"
			x2 = "s "
			x2 += team2_dict['Seed']
			x2 += '. '
			x2 += team2
			x1 += x2
			le = (len(x1) /2) + 25
			x1 = x1.rjust(le)
			print(x1)
			win = ""
			if num <= prob_t1:
				win = team1 
				win += " wins!"
			else:
				win = team2 
				win += " wins!"
			leng = (len(win) / 2) + 25
			win = win.rjust(leng)
			print_sepeartor(25)
			print(win)
		except:
			print('\n'+"Invalid team name(s), please try again")

def sim(matchup):
	team1 = matchup[0]
	team2 = matchup[1]
	team1_dict = all_teams[team1]
	team2_dict = all_teams[team2]
				
	t1_o = float(team1_dict["Adj-O"])
	t1_d = float(team1_dict["Adj-D"])
	t1_t = float(team1_dict["Adj-T"])

	t2_o = float(team2_dict["Adj-O"])
	t2_d = float(team2_dict["Adj-D"])
	t2_t = float(team2_dict["Adj-T"])

	league_av_t = 68.18
	league_av_pp100 = 105.35
	possessions = (t1_t * t2_t) / league_av_t

	t1_ppp = (((t1_o + t2_d)/league_av_pp100) - 1) * possessions
	t2_ppp = (((t2_o + t1_d)/league_av_pp100) - 1) * possessions
	prob_t1 = (t1_ppp ** 10.25) / (t1_ppp**10.25 + t2_ppp**10.25) * 100
	prob_t2 = (t2_ppp ** 10.25) / (t1_ppp**10.25 + t2_ppp**10.25) * 100

	num = random.uniform(0.000, 100.000)
	if num <= prob_t1:
		return team1
	else:
		return team2	

def build_matchup(all_teams, team1, team2):
	team1_dict = all_teams[team1]
	team2_dict = all_teams[team2]
	x1 = team1_dict['Seed']
	x1 += '. '
	x1 += team1
	x1 += '---'
	x1 = x1.rjust(25)
	x2 = team2_dict['Seed']
	x2 += '. '
	x2 += team2
	x2 += '---'
	x2= x2.rjust(25)

	return x1, x2

def build_winner(all_teams, winner):
	buff = " "
	buff = buff * 25
	buff += '|---- '
	winner_dict = all_teams[winner]
	buff += winner_dict['Seed']
	buff += '. '
	buff += winner
	return buff

def build_check(buff, winner1, actual_winner, index, pred):
	if winner1 == actual_winner:
		buff += " ~~CORRECT~~"
		pred += 1
	else:
		buff += " ~~WRONG~~"
	return buff, pred

def print_bracket(x1, buff, x2):
	print(x1)
	print(buff)
	print(x2 + '\n')
	
	
def bracket(all_teams, keys, m, check):
	first4 = []
	first4_w = []
	r64 = []
	r32 = []
	r16 = []
	r8 = []
	r4 =[]
	r2 = []

	r64_winners = []
	r32_winners = []
	r16_winners = []
	r8_winners = []
	r4_winners = []
	r2_winner = ""

	prediction = ["Round of 32",0,"Sweet 16",0,"Elite Eight",0,"Final Four",0,"Championship Game",0,"Champion",0]
	nums = [32,0,16,0,8,0,4,0,2,0,1,0]
	with open('winners.txt', 'r') as file1:
		all_winners_ordered = file1.readlines()
		all_winners_ordered = [x.rstrip() for x in all_winners_ordered]
		for i in range(0,32):
			r64_winners.append(all_winners_ordered[i])
		for i in range(32,48):
			r32_winners.append(all_winners_ordered[i])
		for i in range(48,56):
			r16_winners.append(all_winners_ordered[i])
		for i in range(56,60):
			r8_winners.append(all_winners_ordered[i])
		for i in range(60,62):
			r4_winners.append(all_winners_ordered[i])
		r2_winner = all_winners_ordered[62]	

	pairingsFile = 'data/' + year + '/pairings.txt'
	with open(pairingsFile, 'r') as file:
		all_teams_ordered = file.readlines()
		all_teams_ordered = [x.rstrip() for x in all_teams_ordered]
	for i in range (0,8,2):
		team1 = all_teams_ordered[i]
		team2 = all_teams_ordered[i + 1]
		first4.append((team1, team2))
	for i in range (0, 4):
		first4_w.append(sim(first4[i]))

	#Do Play-in
	playInNum = 0
	for x in range(8, 72, 2):
			team1 = all_teams_ordered[x]
			team2 = all_teams_ordered[x + 1]
			if team2 == "Play-in":
				team2 = first4_w[playInNum]
				playInNum += 1
			matchup_t = (team1, team2)
			r64.append(matchup_t)
			
	#Do Round of 64		
	header = "ROUND OF 64"
	header = header.rjust(len(header)//2 + 25)
	print(header)
	print_sepeartor(25)
	r64i = 0;
	for i in range(0, len(r64), 2):
		#Do first matchup
		team1 = r64[i][0]
		team2 = r64[i][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner1 = sim(r64[i])
		buff = build_winner(all_teams, winner1)
		if(check):
			buff, prediction[1] = build_check(buff, winner1, r64_winners[r64i], prediction[1])
			r64i += 1
		print_bracket(x1, buff, x2) 

		#Do Second matchup
		team1 = r64[i+1][0]
		team2 = r64[i+1][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner2 = sim(r64[i+1])
		buff = build_winner(all_teams, winner2)
		if(check):
			buff, prediction[1] = build_check(buff, winner2, r64_winners[r64i], prediction[1])
			r64i += 1
		print_bracket(x1, buff, x2)
		
		r32.append((winner1,winner2))
	
	#Do Round of 32
	header = "ROUND OF 32"
	header = header.rjust(len(header)//2 + 25)
	print(header)
	print_sepeartor(25)
	r32i = 0
	for i in range(0, len(r32), 2):
		#Do first matchup
		team1 = r32[i][0]
		team2 = r32[i][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner1 = sim(r32[i])
		buff = build_winner(all_teams, winner1)
		if(check):
			buff, prediction[3] = build_check(buff, winner1, r32_winners[r32i], prediction[3])
			r32i += 1
		print_bracket(x1, buff, x2) 

		#Do Second matchup
		team1 = r32[i+1][0]
		team2 = r32[i+1][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner2 = sim(r32[i+1])
		buff = build_winner(all_teams, winner2)
		if(check):
			buff, prediction[3] = build_check(buff, winner1, r32_winners[r32i], prediction[3])
			r32i += 1
		print_bracket(x1, buff, x2)
		
		r16.append((winner1,winner2))

	#Do Sweet 16		
	header = "SWEET 16"
	header = header.rjust(len(header)//2 + 25)
	print(header)
	print_sepeartor(25)
	r16i = 0
	for i in range(0, len(r16), 2):
		#Do first matchup
		team1 = r16[i][0]
		team2 = r16[i][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner1 = sim(r16[i])
		buff = build_winner(all_teams, winner1)
		if(check):
			buff, prediction[5] = build_check(buff, winner1, r16_winners[r16i], prediction[5])
			r16i += 1
		print_bracket(x1, buff, x2) 

		#Do Second matchup
		team1 = r16[i+1][0]
		team2 = r16[i+1][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner2 = sim(r16[i+1])
		buff = build_winner(all_teams, winner2)
		if(check):
			buff, prediction[5] = build_check(buff, winner1, r16_winners[r16i], prediction[5])
			r16i += 1
		print_bracket(x1, buff, x2)
		
		r8.append((winner1,winner2))
		
	#Do Elite 8
	header = "ELITE 8"
	header = header.rjust(len(header)//2 + 25)
	print(header)
	print_sepeartor(25)
	r8i = 0
	for i in range(0, len(r8), 2):
		#Do first matchup
		team1 = r8[i][0]
		team2 = r8[i][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner1 = sim(r8[i])
		buff = build_winner(all_teams, winner1)
		if(check):
			buff, prediction[7] = build_check(buff, winner1, r8_winners[r8i], prediction[7])
			r8i += 1
		print_bracket(x1, buff, x2) 

		#Do Second matchup
		team1 = r8[i+1][0]
		team2 = r8[i+1][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner2 = sim(r8[i+1])
		buff = build_winner(all_teams, winner2)
		if(check):
			buff, prediction[7] = build_check(buff, winner1, r8_winners[r8i], prediction[7])
			r8i += 1
		print_bracket(x1, buff, x2)
		r4.append((winner1,winner2))
		
	#Do Final 4
	header = "FINAL 4"
	header = header.rjust(len(header)//2 + 25)
	print(header)
	print_sepeartor(25)
	r4i = 0
	for i in range(0, len(r4), 2):
		team1 = r4[i][0]
		team2 = r4[i][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner1 = sim(r4[i])
		buff = build_winner(all_teams, winner1)
		if(check):
			buff, prediction[9] = build_check(buff, winner1, r4_winners[r4i], prediction[9])
			r4i += 1
		print_bracket(x1, buff, x2) 

		#Do Second matchup
		team1 = r4[i+1][0]
		team2 = r4[i+1][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner2 = sim(r4[i+1])
		buff = build_winner(all_teams, winner2)
		if(check):
			buff, prediction[9] = build_check(buff, winner1, r4_winners[r4i], prediction[9])
			r4i += 1
		print_bracket(x1, buff, x2)
		r2.append((winner1,winner2))
		
	#Do Championship
	header = "CHAMPIONSHIP"
	header = header.rjust(len(header)//2 + 25)
	print(header)
	print_sepeartor(25)

	team1 = r2[0][0]
	team2 = r2[0][1]
	x1, x2 = build_matchup(all_teams, team1, team2)
	winner1 = sim(r2[0])
	buff = build_winner(all_teams, winner1)
	
	if(check):
		buff, prediction[11] = build_check(buff, winner1, r2_winner, prediction[11])
		r4i += 1
	print_bracket(x1, buff, x2)
		
	if check:
		print("--Final Prediction State --")
		for i in range(0,8,2):
			print("The predicted", end=" ")
			print(prediction[i], end=" ")
			print("field was", end=" ")
			strin = str(prediction[i+1]) + "/" + str(nums[i])
			doubl = round((float(prediction[i+1])/float(nums[i])) * 100, 2)
			strin += " correct for "
			strin += str(doubl)
			strin += "%"
			print(strin)
		for i in range(8,12,2):
			print("The predicted", end=" ")
			print(prediction[i], end=" ")
			print("was", end=" ") 
			strin = str(prediction[i+1]) + "/" + str(nums[i])
			doubl = round((float(prediction[i+1])/float(nums[i])) * 100, 2)
			strin += " correct for "
			strin += str(doubl)
			strin += "%"
			print(strin)

	if m == 1:
		start_input()
	else:
		return winner1

def sim_mutliple(matchup):
		team1 = matchup[0]
		team2 = matchup[1]
		team1score = 0
		team2score = 0
		for i in range(0, 2):
			winner1 = sim(matchup)
			if team1 == winner1:
				team1score += 1
			else:
				team2score += 1
		if team1score > team2score:
			return(team1)
		elif team1score < team2score:
			return(team2)
		else:
			return(sim(matchup))
		
def bracket_maker(all_teams, keys):
	first4 = []
	first4_w = []
	r64 = []
	r32 = []
	r16 = []
	r8 = []
	r4 =[]
	r2 = []


	prediction = ["Round of 32",0,"Sweet 16",0,"Elite Eight",0,"Final Four",0,"Championship Game",0,"Champion",0]
	nums = [32,0,16,0,8,0,4,0,2,0,1,0]

	pairingsFile = 'data/' + year + '/pairings.txt'
	with open(pairingsFile, 'r') as file:
		all_teams_ordered = file.readlines()
		all_teams_ordered = [x.rstrip() for x in all_teams_ordered]
	for i in range (0,8,2):
		team1 = all_teams_ordered[i]
		team2 = all_teams_ordered[i + 1]
		first4.append((team1, team2))
	for i in range (0, 4):
		first4_w.append(sim(first4[i]))

	#Do Play-in
	playInNum = 0
	for x in range(8, 72, 2):
			team1 = all_teams_ordered[x]
			team2 = all_teams_ordered[x + 1]
			if team2 == "Play-in":
				team2 = first4_w[playInNum]
				playInNum += 1
			matchup_t = (team1, team2)
			r64.append(matchup_t)
			
	#Do Round of 64		
	header = "ROUND OF 64"
	header = header.rjust(len(header)//2 + 25)
	print(header)
	print_sepeartor(25)
	for i in range(0, len(r64), 2):
		#Do first matchup
		team1 = r64[i][0]
		team2 = r64[i][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner1 = sim_mutliple(r64[i])
		buff = build_winner(all_teams, winner1)
		print_bracket(x1, buff, x2) 

		#Do Second matchup
		team1 = r64[i+1][0]
		team2 = r64[i+1][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner2 = sim_mutliple(r64[i+1])
		buff = build_winner(all_teams, winner2)
		print_bracket(x1, buff, x2)
		
		r32.append((winner1,winner2))
	
	#Do Round of 32
	header = "ROUND OF 32"
	header = header.rjust(len(header)//2 + 25)
	print(header)
	print_sepeartor(25)
	for i in range(0, len(r32), 2):
		#Do first matchup
		team1 = r32[i][0]
		team2 = r32[i][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner1 = sim_mutliple(r32[i])
		buff = build_winner(all_teams, winner1)
		print_bracket(x1, buff, x2) 

		#Do Second matchup
		team1 = r32[i+1][0]
		team2 = r32[i+1][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner2 = sim_mutliple(r32[i+1])
		buff = build_winner(all_teams, winner2)
		print_bracket(x1, buff, x2)
		
		r16.append((winner1,winner2))

	#Do Sweet 16		
	header = "SWEET 16"
	header = header.rjust(len(header)//2 + 25)
	print(header)
	print_sepeartor(25)
	for i in range(0, len(r16), 2):
		#Do first matchup
		team1 = r16[i][0]
		team2 = r16[i][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner1 = sim_mutliple(r16[i])
		buff = build_winner(all_teams, winner1)
		print_bracket(x1, buff, x2) 

		#Do Second matchup
		team1 = r16[i+1][0]
		team2 = r16[i+1][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner2 = sim_mutliple(r16[i+1])
		buff = build_winner(all_teams, winner2)
		print_bracket(x1, buff, x2)
		
		r8.append((winner1,winner2))
		
	#Do Elite 8
	header = "ELITE 8"
	header = header.rjust(len(header)//2 + 25)
	print(header)
	print_sepeartor(25)
	for i in range(0, len(r8), 2):
		#Do first matchup
		team1 = r8[i][0]
		team2 = r8[i][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner1 = sim_mutliple(r8[i])
		buff = build_winner(all_teams, winner1)
		print_bracket(x1, buff, x2) 

		#Do Second matchup
		team1 = r8[i+1][0]
		team2 = r8[i+1][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner2 = sim_mutliple(r8[i+1])
		buff = build_winner(all_teams, winner2)
		print_bracket(x1, buff, x2)
		r4.append((winner1,winner2))
		
	#Do Final 4
	header = "FINAL 4"
	header = header.rjust(len(header)//2 + 25)
	print(header)
	print_sepeartor(25)
	for i in range(0, len(r4), 2):
		team1 = r4[i][0]
		team2 = r4[i][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner1 = sim_mutliple(r4[i])
		buff = build_winner(all_teams, winner1)
		print_bracket(x1, buff, x2) 

		#Do Second matchup
		team1 = r4[i+1][0]
		team2 = r4[i+1][1]
		x1, x2 = build_matchup(all_teams, team1, team2)
		winner2 = sim_mutliple(r4[i+1])
		buff = build_winner(all_teams, winner2)
		print_bracket(x1, buff, x2)
		r2.append((winner1,winner2))
		
	#Do Championship
	header = "CHAMPIONSHIP"
	header = header.rjust(len(header)//2 + 25)
	print(header)
	print_sepeartor(25)

	team1 = r2[0][0]
	team2 = r2[0][1]
	x1, x2 = build_matchup(all_teams, team1, team2)
	winner1 = sim_mutliple(r2[0])
	buff = build_winner(all_teams, winner1)
	print_bracket(x1, buff, x2)
		

def mass(all_teams, keys):
	times = input("Enter number of times to run: ")
	winners = {}
	for i in range(0, int(times)):
		win = bracket(all_teams, keys, 0, 0)
		if win in winners:
			winners[win] += 1
		else:
			winners[win] = 1
	results = sorted(winners.items(),  key=lambda item: item[1], reverse=True)
	for k, v in results:
		print(k + ": " + str(v) + " (" + percentage(v, times) + ")")

def percentage(part, whole):
  percent = 100 * float(part)/float(whole)
  return str(percent) + "%"

def start_input():
	ask = "Please enter a mode: "
	mode = input(ask)

	if mode == "comp":
		compare(all_teams, keys)
		print("Quitting....")
	elif mode == "sim":
		simulate(all_teams, keys)
	elif mode == "bracket":
		bracket(all_teams, keys, 1, 0)
	elif mode == "mass":
		mass(all_teams, keys)
	elif mode == "bracket_maker":
		bracket_maker(all_teams, keys)
	else:
		print("Invalid mode, Quitting...")
# MAIN 
all_teams = {}
year = "2021"
keys = ['Kenpom Rank', 'Kenpom Seed','Record','Adj-O','Adj-O Rank','Adj-D','Adj-D Rank','Adj-T','Adj-T Rank','Luck','Luck Rank','SOS','SOS Rank','OppO','OppO Rank','OppD','OppD Rank','Non-Con SOS','Non-Con SOS Rank']
statsFile = 'data/' + year + '/team-stats.csv'
with open(statsFile, 'r') as csvfile:
	reader = csv.DictReader(csvfile, dialect='excel')
	for row in reader:
		all_teams[row["Team"]] = row

print("Welcome to Interactive Stats for March Madness " + year)
start_input()
