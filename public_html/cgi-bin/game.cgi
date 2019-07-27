#!/usr/bin/perl
use CGI;
use warnings;

# **************************
# FROG DATING SIMULATOR GAME
# **************************

$swi = 0;

# BUTTON INFO PARSE

my $cgi = CGI->new();

if ($cgi->param('0')){
	$swi = 0;
}
elsif ($cgi->param('1')){
	$swi = 1;
}
elsif ($cgi->param('2')){
	$swi = 2;
}
elsif ($cgi->param('3')){
	$swi = 3;
}
elsif ($cgi->param('4')){
	$swi = 4;
}
elsif ($cgi->param('5')){
	$swi = 5;
}
elsif ($cgi->param('6')){
	$swi = 6;
}
elsif ($cgi->param('7')){
	$swi = 7;
}
elsif ($cgi->param('8')){
	$swi = 8;
}
elsif ($cgi->param('9')){
	$swi = 9;
}
elsif ($cgi->param('10')){
	$swi = 10;
}
elsif ($cgi->param('11')){
	$swi = 11;
}
elsif ($cgi->param('12')){
	$swi = 12;
}
elsif ($cgi->param('13')){
	$swi = 13;
}
elsif ($cgi->param('14')){
	$swi = 14;
}
elsif ($cgi->param('15')){
	$swi = 15;
}
elsif ($cgi->param('16')){
	$swi = 16;
}
elsif ($cgi->param('17')){
	$swi = 17;
}
elsif ($cgi->param('18')){
	$swi = 18;
}
elsif ($cgi->param('19')){
	$swi = 19;
}
elsif ($cgi->param('20')){
	$swi = 20;
}
elsif ($cgi->param('21')){
	$swi = 21;
}
elsif ($cgi->param('22')){
	$swi = 22;
}
elsif ($cgi->param('23')){
	$swi = 23;
}

print "Content-type: text/html\n\n";

# HTML PACKET

print "<html>";
print "<head><title> Date a Frog - Nathan Ladd </title>";
print "<link rel=\"icon\" href=\"../my_files/img/heart-icon.png\"></head>";
print "<body>";
print "<center>";
print "<div style=\"width: 500px;
	word-wrap: breakword;
	border: 1px solid black;\">";

if ($swi == 30){
	print "<img src=\"http://tinyurl.com/markkko\">";
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<br><strong>Why not try saying hello?</strong>";
	print "<br />"; print "<br />";
	print "<input type=\"submit\" name=\"0\" value=\" Hello. \"/>";
}
elsif ($swi == 0){
	print "<img src=\"http://tinyurl.com/markkko\">";
	print "<br />";	print "<br />";
	print "Hi... I am Froglisa. *sigh* I just got dumped by Frogman. Isn't that awful?";
	print "<br />"; print "<br />";
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"1\" value=\" Yeah what a jerk. \"/>";
	print "<br />"; print "<br />";
	print "<input type=\"submit\" name=\"2\" value=\" Not really. \"/>";
}
elsif ($swi == 1){
	print "<img src=\"https://tinyurl.com/lz9thd4\">";
	print "<br />";	print "<br />";
	print "I'm so glad that you agree, croaker! *RIBBIT* You could probably tell, but I happen 
	to be a princess. So I'm kind of a big deal. Who the heck are you?";
	print "<br />"; print "<br />";
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"3\" value=\" I am also a frog! The name's Froggy. \"/>";
	print "<br />"; print "<br />";
	print "<input type=\"submit\" name=\"4\" value=\" Who cares who I am? I want to hear more about you. \"/>";
	print "<br />"; print "<br />";
	print "<input type=\"submit\" name=\"5\" value=\" I am a human and I am not royalty. \"/>";
}
elsif ($swi == 2){ # LOSE
	print "<img src=\"https://tinyurl.com/kf4dfby\">";
	print "<br />";	print "<br />";
	print "Is that supposed to be a joke? That's no way to treat a fine lady, you fool! 
	Come back here once you've learned some manners. Now SCRAM!";
	print "<br />"; print "<br />";
	print "<form name=\"input\" action=\"../my_files/room.html\" method=\"post\">";
	print "<input type=\"submit\" value=\"SCRAM.\"/>";
} 
elsif ($swi == 3){
	print "<img src=\"https://tinyurl.com/kf4dfby\">";
	print "<br />";	print "<br />";
	print "... How dare you lie to me. I can clearly see that you are not a frog *RIBBIT*! You are 
	just as bad as Frogman. In fact, you two would be perfect for each other.";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"2\" value=\"You are ugly!\"/>";
	print "<br />"; print "<br />";
	print "<input type=\"submit\" name=\"6\" value=\"I am sorry.\"/>";
}
elsif ($swi == 4){
	print "<img src=\"https://tinyurl.com/klgn9z4\">";
	print "<br />";	print "<br />";
	print "Ooh la la. You certainly know how to make a froglady blush. *RIBBIT* I hope 
	you aren't being nice to me just because of my immense fortune?!";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"7\" value=\"A beautiful princess deserves to be treated well.\"/>";
	print "<br />"; print "<br />";
	print "<input type=\"submit\" name=\"5\" value=\"I am a bit of a gold digger.\"/>";
}
elsif ($swi == 5){
	print "<img src=\"https://tinyurl.com/klgn9z4\">";
	print "<br />";	print "<br />";
	print "*RIBBIT* I like that you're being honest. You know, honesty is a good quality in a partner. Heehee.";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"8\" value=\"I am afraid that you have the wrong idea, missy.\"/>";
	print "<br />"; print "<br />";
	print "<input type=\"submit\" name=\"7\" value=\"*RIBBIT* flirtatiously.\"/>";
}
elsif ($swi == 6){
	print "<img src=\"http://tinyurl.com/markkko\">";
	print "<br />";	print "<br />";
	print "*RIBBIT* Hmmm... You seem truly sorry so... I forgive you. If we're going to 
	be here awhile we should order a pizza. What's your favorite type of pizza?";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"9\" value=\"Cheese pizza.\"/>";
	print "<br />"; print "<br />";
	print "<input type=\"submit\" name=\"10\" value=\"Pineapple pizza.\"/>";
	print "<br />"; print "<br />";
	print "<input type=\"submit\" name=\"9\" value=\"Bug pizza.\"/>";
	print "<br />"; print "<br />";
	print "<input type=\"submit\" name=\"9\" value=\"Big pizzas.\"/>";
	print "<br />"; print "<br />";
	print "<input type=\"submit\" name=\"2\" value=\"Frog pizza.\"/>";
}
elsif ($swi == 7){
	print "<img src=\"https://tinyurl.com/klgn9z4\">";
	print "<br />";	print "<br />";
	print "Wow you're quite the croaker! I'd go as far as to say that you're the perfect package! 
	... Just kidding, of course! Aha ha ha *RIBBIT* ha ha. I'm in the mood for a good quality joke. Please tell me one.";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"11\" value=\"Why are frogs so happy? ~~ They eat whatever bugs them!\"/>";
	print "<br />"; print "<br />";
	print "<input type=\"submit\" name=\"2\" value=\"What's white on the outside, and green on the inside? ~~ A frog sandwich!\"/>";
	print "<br />"; print "<br />";
	print "<input type=\"submit\" name=\"11\" value=\"What's a frog's favorite time? ~~ Leap year!\"/>";
	print "<br />"; print "<br />";
	print "<input type=\"submit\" name=\"2\" value=\"What's green and ugly? ~~ You!\"/>";
}
elsif ($swi == 8){
	print "<img src=\"http://tinyurl.com/markkko\">";	
	print "<br />";	print "<br />";
	print "*RIBBIT* *ribbit* How rude. I think you owe me an apology.";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"6\" value=\"I am sorry.\"/>";
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"2\" value=\"I was just being honest...\"/>";
}
elsif ($swi == 9){
	print "<img src=\"https://tinyurl.com/la4qm4o\">";	
	print "<br />";	print "<br />";
	print "*RIBBIT* Yum! *RIBBIT* That's my favorite type of pizza too! We're learning so 
	much about each other. I can already tell that we're going to be best friends.";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"2\" value=\"I think I am going to be sick.\"/>";
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"12\" value=\"I want us to be more than friends.\"/>";
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"7\" value=\"You are already my best friend.\"/>";
}
elsif ($swi == 10){
	print "<img src=\"https://tinyurl.com/la4qm4o\">";
	print "<br />";	print "<br />";
	print "... Interesting. I thought everyone hated pineapple pizza.";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"12\" value=\"Well I like it.\"/>";
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"9\" value=\"Ha, kidding! I love veggie pizza.\"/>";
}
elsif ($swi == 11){
	print "<img src=\"https://tinyurl.com/lz9thd4\">";	
	print "<br />";	print "<br />";
	print "Oh! Ha ha ha ha ha *RIBBIT* ha ha *RIBBIT* ha! You're so funny. Listen... I 
	don't even know your name, but... I think that we should date... What do you think?";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"8\" value=\"I think I am going to barf.\"/>";
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"13\" value=\"I was just about to say the same thing.\"/>";
}
elsif ($swi == 12){
	print "<img src=\"http://tinyurl.com/kz76j54\">";	
	print "<br />";	print "<br />";
	print "You know what, croaker? I like you. Today must be your lucky day because I'm going 
	to let you date me... *rrriiibbbiiittt* But before we make it official, I want to 
	make sure you're not playing me. Do you remember my sweet name?";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"2\" value=\"She-Frog.\"/>";	
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"2\" value=\"Froggirl.\"/>";
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"2\" value=\"Pollifroggy.\"/>";
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"14\" value=\"Froglisa.\"/>";
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"2\" value=\"Lady Froglegs.\"/>";
}
elsif ($swi == 13){
	print "<img src=\"http://tinyurl.com/kz76j54\">";	
	print "<br />";	print "<br />";
	print "I'm so happy. Now... Before we date *rrriiibbbiiittt*... Do you remember my beautiful 
	name? I ask this to all of my potential dates to weed out the fakes.";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"2\" value=\"She-Frog.\"/>";	
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"2\" value=\"Froggirl.\"/>";
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"2\" value=\"Pollifroggy.\"/>";
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"14\" value=\"Froglisa.\"/>";
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"2\" value=\"Lady Froglegs.\"/>";
}
elsif ($swi == 14){
	print "<img src=\"http://tinyurl.com/kz76j54\">";
	print "<br />";	print "<br />";
	print "... Then it's official. We're now *rrriiibbbiiittt* dating! I most eagerly await our first 
	date as a couple. When shall we schedule it?";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"15\" value=\"I will call you.\"/>";	
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"16\" value=\"Right now!\"/>";
}
elsif ($swi == 15){
	print "<img src=\"https://tinyurl.com/lz9thd4\">";	
	print "<br />";	print "<br />";
	print "I haven't given you my number, silly. You don't have a very good memory, huh?";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"17\" value=\"Shut up!\"/>";	
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"18\" value=\"My memory sucks.\"/>";
}
elsif ($swi == 16){
	print "<img src=\"https://tinyurl.com/la4qm4o\">";	
	print "<br />";	print "<br />";
	print "... R-R-R-Right now??? O-Okay... I was not expecting you to be this spontaneous 
	*rrriiibbbiiittt*. What do you have in mind, my love? Keep in mind that I'm tough to please.";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"19\" value=\"I want to take you out to The Golden Frog.\"/>";	
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"20\" value=\"Let's play a math game.\"/>";
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"17\" value=\"I was thinking we could go to your place!\"/>";	
}
elsif ($swi == 17){
	print "<img src=\"http://tinyurl.com/markkko\">";
	print "<br />";	print "<br />";
	print "Careful croaker, I don't like your tone. *RIBBIT* But let's just call that strike one, okay?";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"18\" value=\"Understood.\"/>";	
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"22\" value=\"I want out of this relationship.\"/>";
}
elsif ($swi == 18){
	print "<img src=\"https://tinyurl.com/la4qm4o\">";
	print "<br />";	print "<br />";
	print "You are cute. I've been thinking of what our first child could be called. Now tell me 
	which one of these names sounds the most outstanding to you?";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"21\" value=\"Fungalina.\"/>";	
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"21\" value=\"Tad.\"/>";
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"21\" value=\"Lily.\"/>";
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"21\" value=\"Gunko.\"/>";
}
elsif ($swi == 19){
	print "<img src=\"https://tinyurl.com/lz9thd4\">";
	print "<br />";	print "<br />";
	print "The Golden Frog sounds l-o-v-e-l-y. Ooooh what a romantic date this will be!";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"23\" value=\"Romantic is my middle name.\"/>";	
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"22\" value=\"On second thought, I am not really into frogs, sorry.\"/>";
}
elsif ($swi == 20){
	print "<img src=\"http://tinyurl.com/markkko\">";	
	print "<br />";	print "<br />";
	print "..... Really? *rrrrrriiiiiibbbbbbiiiiiitttttt* Alright. Um... What does 7 times 8 equal, croaker?";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"23\" value=\"The number of times I love you to the moon and back.\"/>";	
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"17\" value=\"Fifty-six! Ha, next time give me a real challenge.\"/>";
}
elsif ($swi == 21){
	print "<img src=\"https://tinyurl.com/lz9thd4\">";
	print "<br />";	print "<br />";
	print "Ahhh I'm so glad you think so *RIBBIT*! It took me forever to come up with that name. 
	... This might be crazy, but you should come over to my palace and meet my family!";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"game.cgi\" method=\"post\">";
	print "<input type=\"submit\" name=\"22\" value=\"We are moving too fast. I think I should go.\"/>";	
	print "<br />"; print "<br />";	
	print "<input type=\"submit\" name=\"23\" value=\"What a brilliant idea!\"/>";
}
elsif ($swi == 22){ # LOSE
	print "<img src=\"https://tinyurl.com/kf4dfby\">";	
	print "<br />";	print "<br />";
	print "Et tu, brute? Do you think it's fun to play with a frog's heart? Leave me to linger in 
	*RRRIIIBBBIIITTT* despair!";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"../my_files/room.html\" method=\"post\">";
	print "<input type=\"submit\" value=\"SCRAM.\"/>";	
}
elsif ($swi == 23){
	print "<img src=\"http://tinyurl.com/kz76j54\">";	
	print "<br />";	print "<br />";
	print "*RIBBIT* *RIBBIT* You make me so happy! If this were a game, I'd say you won, hun! <3";
	print "<br />"; print "<br />";	
	print "<form name=\"input\" action=\"../my_files/room.html\" method=\"post\">";
	print "<input type=\"submit\" value=\"Go back and re-live the experience!\"/>";	
}
else{
	print "Uh oh there has been an error!";
	print "<form>";
}

print "</form>";	
print "</div>";

print "</center>";
print "<body>";	
print "</html>";
