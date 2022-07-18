# Introduction

SpongeBob SquarePants has been an influential TV show for many people, spawning many memes and memories for people all over the world. However, it is evident that the show has changed dramatically across the 20+ years it's been on air, and as such, the episode ratings have fluctuated along with the different styles too. Therefore, my hope is to be able to use topic modeling to analyze whether certain topics in certain episodes typically earn higher ratings than others. Additionally, with SpongeBob episodes being so diverse in style and content, I will attempt to fine-tune a GPT3 model to generate new SpongeBob episodes based on a given title as input.

# Topic Modeling Results

Looking at the data, it is clear that my aforementioned statement about ratings fluctuations among SpongeBob episodes is true. The below graph illustrates this point very clearly.
<p align="center">
  <img src="https://user-images.githubusercontent.com/62823414/179449264-d9d1e635-260e-44c2-b46f-63b8dc23cb8c.png">
</p>
However, the results of the topic modeling are not as clear. Ultimately, most topics that the model found did not have average ratings that deviated too far from the mean episode rating. The few that were somewhat different appeard to really mostly only pertain to one or two episodes, which does not necessarily give a good indication of topics that perform well or poorly.

Overall, the modeling showed that there are likely many factors that go into an episode's rating, such as the quality of the plot and the jokes that go into the episode, and simply judging it based off the topics that were used is likely not really a good indication of how well the episode will perform. 

# Episode Generation Results

Using a fine-tuned GPT3 model, below are the outputs of some example inputs I ran.

```
"Krabs Goes Broke"
In the beginning of the episode, SpongeBob arrives at Mr. Krabs' Velma Cammobile to start his day at work. While helping Mr. Krabs open his safe with a crowbar, the crab tells SpongeBob that he needs to make sure no one borrows money from him during the next 24 hours. However, due to having spent most of his own funds on various things (including a kickback from Squidward's book rental), he can barely afford any food for himself for lunch.
It then shows Patrick buying all kinds of things at his convenience store without paying for them, such as 32 bags of sugar, a never-ending supply of coffee creamer and a bag of seaweed snacks without buying any actual food items. When Squidward objects and suggests that Patrick buys some hot dogs instead, the latter states he only has fifty cents and reveals that SpongeBob knows how to get that amount in less than twenty seconds in exchange for not telling anyone about this "secret."
Squidward suggests they go into business with each other until SpongeBob pays him back (however this will never happen), but Patrick just laughs at this before going back home with Gary. Trying to hide what he did from Mr. Krabs, SpongeBob goes to work, but the crab soon finds out and fires him.
After Squidward quits his job in protest, Mr. Krabs is left with no employees to run his business. This eventually leads to him being forced to sell the restaurant to a group of anchovies for $100 due to having no other choice (aside from declaring bankruptcy). 
The anchovies apparently do not know how to cook Krabby Patties, as they are revealed to be serving them frozen and burnt. This eventually leads to the customers revolting and chasing Mr. Krabs out of his own restaurant. 
Ending back at his office, an exhausted Mr. Krabs falls asleep on his desk with a tear running down his eye.
Later, Plankton is seen celebrating his victory as he now owns the Krusty Krab (due to buying it for a very low price) and has turned it into a mobile Chum Bucket food truck, much to the horror of the citizens of Bikini Bottom.
Patrick arrives outside Mr. Krabs' office window (using a fishing rod as a makeshift crane) with a bag of money and tells him that he managed to get it from SpongeBob in exchange for not telling anyone about their secret agreement (although he does not remember what it was). This finally allows Mr. Krabs to buy back the Krusty Krab from Plankton and re-open it as if nothing ever happened...although Gary is now working for Plankton as part of their deal (which Plankton does not know about).
Some time later, it is shown that due to Mr. Krabs being more careful with his money, the Krusty Krab is now more successful than ever before (with Squidward back as his cashier). Patrick then comes in, asking for a Krabby Patty but is informed by Squidward that they cost $7.99 now. SpongeBob arrives soon afterwards with a bag of money, revealing that he has been working for Mr. Krabs as a part-time security guard to help him out and make some extra money. 
This episode implies that Mr. Krabs went bankrupt and lost the Krusty Krab, but was able to buy it back from Plankton and re-open it.
===============================
"The Chum Monster"
As the episode begins, Squidward is watching television, until he hears a commercial for Reality Bites magazine about the newest monster known as The Chum Monster, which is terrorizing the Bikini Bottom fishing community. Due to his love of fish horror, Squidward assumes that it must be fun to be killed by a giant, rotten fish head monster and decides to go out on a quest to slay the beast. After constructing several cardboard boomerangs from his paper towel roll, he goes out into the streets and finds that Sandy has already warned everyone about The Chum Monster. He finds Patrick raking leaves and convinces him to come with him on his adventure. However, Patrick only wants to know how many blades are in Squidward's box "clip-clopping toward me." He then tells Patrick that he will tell him when they reach it and leaves while two fishing boats begin playing Annoying Annoying Song simultaneously once they are not paying attention.
He then goes into SpongeBob's pineapple house and tries to convince SpongeBob join on his quest but fails when Mrs. Puff interrupts them claiming she works out with weights while listening to a sound system until they accidentally destroy her house grabbing weights while trying to lift up her couch. Squidward leaves as Mrs. Puff tries to think of a way to get SpongeBob in trouble. 
Squidward and Patrick reach the spot where the fishing boats are playing the Annoying Song and find that they are getting closer to the Chum Monster. Squidward tries to throw a boomerang at it, but it just comes back and hits him in the face. The Chum Monster starts chasing them, and they run away until they run into a dead end. The Chum Monster catches up to them and starts eating them, but they are saved by Sandy who shows up riding on top of a giant clam.
===============================
"The New Zoo"
At the Krusty Krab one day, SpongeBob makes a new fish order, but when he sees that it's just a seal, he calls his coworkers to come and see. Squidward berates him for letting another customer go to the facility "the way it is" and makes it clear that he will be taking over SpongeBob's duties. This causes SpongeBob to argue with Squidward and run away crying.
SpongeBob goes out at night and cries next to a sea urchin test dig site, where he expresses his worry over what Squidward will do with the restaurant until Patrick says that everything will be fine in the morning. Afterwards, they decide to put on a show for Squidward as an apology for hurting his feelings while warning him of what they plan on doing (such as pulling knobs from their eyes and farting loudly) before assaulting him when he arrives at work the next morning.
Squidward panics as he tries to get things organized and asks Sandy for help, who reminds him of his condition "temporary subaquianetarian." She takes this statement literally and leaves causing him to do so as well. With no-one around but SpongeBob (who tried panicking Squidward on purpose), Squidward starts to feel better and learns that he was too hard on SpongeBob. He tries to get the Krusty Krab back to its former state, but things only get worse. 
In the end, SpongeBob and Patrick present a show to Squidward (of them cleaning the Krusty Krab), which makes him happy and allows him to take a break.
```

These outputs were discussed in the model-creation file.

# Data Sources

[The SpongeBob Wiki](https://spongebob.fandom.com/wiki/Encyclopedia_SpongeBobia)

[IMDb](https://www.imdb.com/)

