NCAA Tournament Analysis by Andy Jiang

An interactive python program that allows the user to compare all 68 teams in the NCAA March Madness basketball tournament. Updated for 2018-2019.

To use, keep both txt files and the csv file in the same directory as bracket.py
And envoke in python with 

python bracket.py

to begin the interactive program.

There are currently 4 working modes

----comp----

This mode asks the user to input two teams, and then shows all their stats side-by-side.
Stats include tournament seed, Kenpon Ranking, Kenpom seed, Record, and all other Kenpom
Adjusted Efficiency stats.

Also prints the probability that each team would win against the other, as well
as an expected score based on both teams' adjusted offense, defense, and tempo.

The teams mode in help allows the user to give the first letter of a team they're trying
to spell, and the program will give the correct spelling for all teams starting with
that letter (since only a specific spelling for each team is accepted)

----sim-----

This mode simply sims a game between two give teams, with a simple weighted coin 
flip based on the caclutaed probability to win

----bracket----

This mode simulates and prints an entire bracket based on the same algorithm as sim.
It also compares its simulated bracket to the actual bracket, and prints its accuracy.

----mass----

This mode takes in a number of touraments to run, and runs that many touraments.
At the end, the number of tournaments won by each team will be printed.



All stats are taken from Kenpom.com, before the NCAA tournament began.

