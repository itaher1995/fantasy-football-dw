# fantasyfootball.ai

## About

The following repository consists of the experiments and analysis I ran regarding fantasy football. This repository also serves as the groundwork for a product I like to call fantasyfootball.ai. I plan to analytics and machine learning to develop models and tools that can be effective for making week to week discussions.

Currently most of the work is being done on data regarding PPR, but when the groundwork is laid out for at least one feature, I plan to expand it such that we can analyze data regarding HPPR, Standard, DraftKings, FanDuel, etc.

## Types of Data

One of the biggest hurdles for this effort has been data collection. I have collected data from a variety of third party resources. These resources have given me information about historical fantasy performances at the aggregate and week by week level and historical regular season statistics. 

## Experiment I: Drafting Importance

One of the first analysis done for this project was draft strategy. I generated 3000 random teams using 2017 outputs of 1 QB, 1 RB, 1 WR, 1 TE. I took the aggregate fantasy points of those teams and decided to use the 75th percentile as the cutoff for what is a good team and what is not a good team. Afterwards, I ran a logistic regression analysis to see which variable was weighted the most in my analysis. The order of weight (in descending order) was RB, QB, TE, WR. What stood out as extremely interesting was how TE was weighed higher than WR.

I then broke each position into several sub-positions. So for example RB was broken up into "Feature Backs", "Pass Catching Backs", "Rotational Backs" and finally "Other." Using these groups I discovered that in the 3000 random teams, I discovered that certain sub-positions were over represented compared to other positions. So for example "Pocket Passers" were found in these better groups more often than "Hybrid QBs".

* Using this information I developed a draft strategy that followed positional importance and then sub-position representation. While this drafting strategy led to some good pick ups, I mismanaged my use of WR. I got my first wide receiver in the fourth round, which was Golden Tate.

* This strategy didn't account for later round sleeper picks and did not use previous record of play as an indicator. Devonta Freeman was high on my draft strategy board, even though he's been injured weeks at a time in the past. In future draft implementations, reliability of a player and their previous scores should be weighed (Devonta Freeman should not be drafted in the top 20, even though he can be a talented back.)

* This strategy also overvalued rotational backs over the pass catching backs. Players like Christian McCafferey went under the radar where as players like Marshawn and Devonta shined. 

* By breaking this up by sub position, Zach Ertz did not fall into the same category as Rob Gronkowski and Travis Kelce. Ertz was available after Kelce and hasn't been much worse than Kelce. I could have picked up a WR in the third round and hoped that Ertz would available in the fourth.

