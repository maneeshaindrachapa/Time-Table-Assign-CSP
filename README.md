# Time-Table-Assignment
Simple time table generator according  to the data given, modelling as constraint satisfaction problem

Let’s assign<br>
Variables – Subject + Compulsory or Optional<br>
Input – 	<br>
`CS3018,c,Mo3,Mo2
CS3912,c,Tu1,We1
CS4201,c,Mo1,We2
MN1023,o,Mo2
EN1821,o,Mo2
EN1921,o,Mo2,Mo3
MT3100,c,Mo3, We2
R1,R2,R3` <br>
Input file contains Module Name, Compulsory or Optional and available time slots and final line of input file contain the rooms available
Compulsory modules should assigned in a time slot where it is not clashed with other modules and optional modules can be assigned in same time slot in different rooms

Output – <br>
`CS3018,Mo3,R1
CS3912,Tu1,R1
CS4201,Mo1,R1
MN1023,Mo2,R1
EN1821,Mo2,R2
EN1921,Mo2,R3
MT3100, We2,R1`<br>
Output will look like this where all the compulsory modules have been on R1 and optional modules varies according to the time slot and available rooms

Constraints – <br>
Constraints are provided if there is compulsory module in same time slots cannot be happen.

